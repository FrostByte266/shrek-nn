import csv
import re
from random import shuffle, seed

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

from src.data_fetching import fetch_puns_list

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
    return training_set
