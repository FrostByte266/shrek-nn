import csv
import re
import sys
from random import shuffle, seed

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score

sys.path.append('/src/')

from data_fetching import fetch_puns_list

def make_train_csv():
    with open('/data/sentences.txt', 'r') as f:
        lines = f.readlines()
    reg = re.compile(r'\n')
    blank = ''
    data = [f'"{re.sub(reg, blank, line)}", 0' for line in lines]
    with open('data/sentences.csv', 'w+') as f:
        f.write("\n".join(data))

def load_sentences():
    with open('/data/sentences.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return([[str(row[0]), int(row[1])] for row in reader])

def make_training_set(pages = 1, rand_seed=None):
    sentences = load_sentences()
    puns = fetch_puns_list(pages)
    if rand_seed is not None:
        seed(rand_seed)
    training_set = sentences + puns
    shuffle(training_set)
    return np.array(training_set, object)

# def vectorize(training_set):
#     vectorizer = TfidfVectorizer(stop_words='english')
#     np_training = np.array(training_set)
#     without_labels = np_training[:, :-1]
#     list_set = [item[0] for item in without_labels.tolist()]
#     X = vectorizer.fit_transform(list_set)
#     return X.toarray()

def vectorize(training_set):
    # print(training_set)
    vectorizer = TfidfVectorizer(stop_words='english')
    without_labels = training_set[:, :-1]
    list_set = np.array([item[0] for item in without_labels])
    X = vectorizer.fit_transform(list_set)
    out = []
    for key, value in enumerate(X.toarray()):
        # print(f'Key: {key}, Value: {value}, Label: {training_set[key][1]}\n\n')
        out.append([value, training_set[key][1]])
    return np.array(out, object), vectorizer

# if __name__ == '__main__':
#     vectorize(make_training_set())
