import sys
from collections import Counter
import string
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        print("Такого файла не существует")
        return None
    with open(filepath) as file:
        text = file.read()
    return get_words_from_text(text)


def get_words_from_text(text):
    words = text.lower().split()
    rstrip_words = lambda word: word.rstrip(string.punctuation)
    words = [rstrip_words(word) for word in words if rstrip_words(word)]
    return words


def get_most_frequent_words(words):
    output_words_quantity = 10
    print("\n".join(pair[0] for pair in Counter(words).most_common(output_words_quantity)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_most_frequent_words(load_data(sys.argv[1]))
    else:
        print("Введите название файла")
