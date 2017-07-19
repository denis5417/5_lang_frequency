import sys
from collections import Counter
import string


def load_data(filepath):
    try:
        with open(filepath) as file:
            words = file.read().lower().split()
            words = [word.rstrip(string.punctuation) for word in words if len(word.rstrip(string.punctuation)) > 0]
        return words
    except FileNotFoundError:
        print("Такого файла не существует")
        return None


def get_most_frequent_words(words):
    if not words:
        pass
    else:
        print("\n".join(pair[0] for pair in Counter(words).most_common(10)))


if __name__ == '__main__':
    try:
        get_most_frequent_words(load_data(sys.argv[1]))
    except IndexError:
        print("Введите название файла")
