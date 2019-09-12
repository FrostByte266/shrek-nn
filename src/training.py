from neupy.layers import *
from neupy import algorithms
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import dill
import io
import base64

from preprocessing import *

def add_padding(data):
    n_sampels = len(data)
    max_seq_length = max(map(len, data))

    data_matrix = np.zeros((n_sampels, max_seq_length))
    for i, sample in enumerate(data):
        data_matrix[i, -len(sample):] = sample

    return data_matrix

def train_network(num_pages=1):
    training_set, vectorizer = vectorize(make_training_set(num_pages))
    examples = training_set[:, :-1]
    labels = training_set[:, -1:]
    new_examples = np.array([example[0] for example in examples])
    np.set_printoptions(threshold=np.inf)
    new_examples = (np.pad(new_examples, 0, mode='constant', constant_values=0))
    # new_examples = add_padding(new_examples)
    # print(new_examples)
    # assert False
    print(new_examples)
    size=len(new_examples[0])
    new_labels = labels
    input_size = len(new_examples[0])
    parsig = Sigmoid(100) >> Sigmoid(100)
    partan = Tanh(100) >> Tanh(100)
    parelu = Elu(100) >> Elu(100)
    parchain_negative = Tanh(100) >> Elu(100)
    parchain_zero = Sigmoid(100) >> Relu(100)

    network = Input(input_size) >> Linear(100) >> (
    		parsig | partan | parelu | parchain_negative | parchain_zero) >> \
    						Concatenate() >> Tanh(100) >> Relu(1)

    optimizer = algorithms.Adam(
        network,
        batch_size = None,
        shuffle_data=True,
        loss='binary_crossentropy',
        verbose=True,
        regularizer=algorithms.l2(0.00001)
    )

    optimizer.train(new_examples, new_labels, epochs=1000)
    optimizer.plot_errors(show=False)
    bytes = io.BytesIO()
    plt.savefig(bytes)
    bytes.seek(0)
    encoded = base64.b64encode(bytes.read())

    return optimizer, vectorizer, [new_examples[0]], encoded
