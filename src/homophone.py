from fuzzy import nysiis
from fuzzywuzzy import fuzz
import csv
import numpy as np

def get_all_pairs(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            yield nysiis(row[0]), nysiis(row[1])

def check_equal(pair):
    return pair[0] == pair[1]

if __name__ == '__main__':
    with open('../data/homophones.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(f'Word pair: {" & ".join(str(x) for x in row)}')
            for word in row:
                print(f'Pronunciation: {nysiis(word)}')
            print("Match" if nysiis(row[0]) == nysiis(row[1]) else "No match")
            print(fuzz.ratio(*row))
