from neupy.layers import *
from neupy import algorithms
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import dill
import io
import base64

from preprocessing import *

def train_network(num_pages=1):
	training_set, vectorizer = vectorize(make_training_set(num_pages))
	examples = training_set[:, :-1]
	labels = training_set[:, -1:]
	new_examples = np.array([example[0] for example in examples])
	new_examples = add_padding(new_examples)
	input_size = len(new_examples[0])
	scale = int(input_size/10 * (2/3))+1
	concat_noisynormdrop_one = Concatenate() >> GaussianNoise(std=2) >> BatchNorm() >> Dropout(proba=.7)
	concat_noisynormdrop_two = Concatenate() >> GaussianNoise(std=2) >> BatchNorm() >> Dropout(proba=.9)
	concat_noisynormdrop_three = Concatenate()>> GaussianNoise(std=2) >> BatchNorm() >> Dropout(proba=.8)
	concat_noisynormdrop_four = Concatenate() >> GaussianNoise(std=2) >> BatchNorm() >> Dropout(proba=.7)
	noisy_para_seq = Input(input_size)>>\
						Linear(scale)>>\
						(Tanh(scale)|Elu(scale)|LeakyRelu(scale)|Sigmoid(scale))>>\
						concat_noisynormdrop_one>>\
						(Tanh(scale)|Elu(scale)|LeakyRelu(scale)|Sigmoid(scale))>>\
						concat_noisynormdrop_two>>\
						(Tanh(scale)|Elu(scale)|LeakyRelu(scale)|Sigmoid(scale))>>\
						concat_noisynormdrop_three >>\
						(Tanh(scale)|Elu(scale)|LeakyRelu(scale)|Sigmoid(scale))>>\
						concat_noisynormdrop_four>>\
						HardSigmoid(1)


	optimizer = algorithms.Adam(
		noisy_para_seq,
		batch_size = None,
		shuffle_data=True,
		loss='binary_crossentropy',
		verbose=True,
		regularizer=algorithms.l2(0.00001)
	)

	optimizer.train(new_examples, labels, epochs=1000)
	optimizer.plot_errors(show=False)
	bytes = io.BytesIO()
	plt.savefig(bytes)
	bytes.seek(0)
	encoded = base64.b64encode(bytes.read())

	return optimizer, vectorizer, [new_examples[0]], encoded
