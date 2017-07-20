import sys
from collections import Counter
import string


def load_data(filepath):
    try:
        with open(filepath) as file:
            text = file.read()
        return get_words_from_text(text)
    except FileNotFoundError:
        print("Такого файла не существует")
        return None


def get_words_from_text(text):
    words = text.lower().split()
    words = [word.rstrip(string.punctuation) for word in words if len(word.rstrip(string.punctuation))]
    return words


def get_most_frequent_words(words):
    if not words:
        return None
    else:
        output_words_quantity = 10
        print("\n".join(pair[0] for pair in Counter(words).most_common(output_words_quantity)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_most_frequent_words(load_data(sys.argv[1]))
    else:
        print("Введите название файла")
