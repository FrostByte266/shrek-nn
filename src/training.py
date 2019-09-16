from neupy.layers import *
from neupy import algorithms
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
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
	training_examples, test_examples, training_labels, test_labels = train_test_split(new_examples, labels, test_size=0.4)
	input_size = len(new_examples[0])
	scale = int(input_size/10 * (2/3))+1
	fourth = int(scale/4)
	thirds = int(scale/3)

	concat_noisynormdrop_one = Concatenate() >> GaussianNoise(std=1) >> BatchNorm() >> Dropout(proba=.1)
	concat_noisynormdrop_two = Concatenate()>> GaussianNoise(std=1) >> BatchNorm() >> Dropout(proba=.1)
	concat_noisynormdrop_three = Concatenate() >> GaussianNoise(std=1) >> BatchNorm() >> Dropout(proba=.1)

	sub_tri = Elu(fourth) >> Sigmoid(fourth)
	sub_tri_leaky_relu = LeakyRelu(thirds)>>LeakyRelu(thirds)>>LeakyRelu(thirds)

	noisy_para_seq = Input(input_size)>>\
							Linear(scale)>>\
							(Tanh(scale)|Elu(scale)|sub_tri_leaky_relu|sub_tri)>>\
							concat_noisynormdrop_one>>\
							(Tanh(scale)>>Tanh(scale)|Elu(scale)>>Elu(scale)|Sigmoid(fourth)>>Sigmoid(fourth))>>\
							concat_noisynormdrop_two >>\
							(Tanh(scale)|Elu(scale)|LeakyRelu(scale)|Sigmoid(scale))>>\
							concat_noisynormdrop_three>>\
							Sigmoid(1)


	optimizer = algorithms.Adam(
		noisy_para_seq,
		batch_size = None,
		shuffle_data=True,
		loss='binary_crossentropy',
		verbose=True,
		regularizer=algorithms.l2(0.1)
	)

	optimizer.train(training_examples, training_labels, test_examples, test_labels, epochs=2000)
	prediction = [1 if i > .5 else 0 for i in optimizer.predict(test_examples)]
	accuracy = [1 if prediction[i] == test_labels[i] else 0 for i in range(len(prediction))].count(1) / len(
		prediction)
	print(f'{accuracy * 100:.2f}%')
	optimizer.plot_errors(show=False)
	bytes = io.BytesIO()
	plt.savefig(bytes)
	bytes.seek(0)
	encoded = base64.b64encode(bytes.read())

	return optimizer, vectorizer, [new_examples[0]], encoded
