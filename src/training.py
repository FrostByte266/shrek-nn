from neupy.layers import *
from neupy import algorithms
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from preprocessing import *

def train_network(num_pages=1):
    training_set, vectorizer = vectorize(make_training_set(num_pages))
    examples = training_set[:, :-1]
    labels = training_set[:, -1:]
    new_examples = np.array([example[0] for example in examples])
    new_examples = (np.pad(new_examples, 0, mode='constant', constant_values=0)).flatten()
    size = np.size(new_examples)
    new_labels = [label for label in labels]
    input_size = len(new_examples)
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
        regularizer=algorithms.l2(0.0005)
    )

    optimizer.train(new_examples, new_labels, epochs=500)
    optimizer.plot_errors(show=False)
    plt.savefig('/data/graph.png')

    return optimizer, vectorizer, size
