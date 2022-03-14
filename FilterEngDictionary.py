import os
import json

BASEDIR = os.path.dirname(os.path.abspath(__file__))


def format_dictionary():
    with open('dictionary.json', 'r') as f:
        filtered_words = [str(word) for word in json.load(f).keys()
                          if len(str(word)) == 5 and '-' not in str(word)]
        filtered_words.sort()
        filtered_words.pop(0)
        with open('filtered_eng_dict.txt', 'w') as d:
            for word in filtered_words:
                d.write(word+'\n')

