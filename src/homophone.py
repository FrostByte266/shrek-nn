import fuzzy
import csv
import numpy as np

def generate_dmeta_pair(row):
    dmeta = fuzzy.DMetaphone()
    return dmeta(row[0]), dmeta(row[1])

def get_all_pairs(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            yield generate_dmeta_pair(row)

def check_equal(meta_tuple):
    intersection = [word for word in meta_tuple[0] if word in meta_tuple[1]]
    return True if intersection else False
