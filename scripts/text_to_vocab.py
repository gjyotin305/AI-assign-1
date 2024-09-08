import nltk
from nltk.tokenize import word_tokenize
from constant import text
import string

nltk.download('punkt_tab')

def text_to_vocab(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    vocabularly = set(words)
    return vocabularly


def save_vocab(vocab, filename):
    # Write the vocabularly to a text file, one word per line
    with open(filename, "w") as f:
        for word in sorted(vocab):
            f.write(f"{word}\n")


vocab = text_to_vocab(text)


save_vocab(vocab, "../data/vocab.txt")