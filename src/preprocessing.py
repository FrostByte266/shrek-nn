import csv
import re
from random import shuffle, seed

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score

from data_fetching import fetch_puns_list

def add_padding(data):
    n_sampels = len(data)
    max_seq_length = max(map(len, data))

    data_matrix = np.zeros((n_sampels, max_seq_length))
    for i, sample in enumerate(data):
        data_matrix[i, -len(sample):] = sample

    return data_matrix

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


def vectorize(training_set):
    vectorizer = TfidfVectorizer(stop_words='english')
    without_labels = training_set[:, :-1]
    list_set = np.array([item[0] for item in without_labels])
    X = vectorizer.fit_transform(list_set)
    out = []
    for key, value in enumerate(X.toarray()):
        out.append([value, training_set[key][1]])
    return np.array(out, object), vectorizer
