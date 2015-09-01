# coding=utf-8
"""Markov chain which reads text and then generates text."""
import pickle
from collections import defaultdict
from random import choice
import os
import pyPdf
import string


def read_pdf(infile, outfile):
    """Read PDF and save text as .txt."""
    pdf = pyPdf.PdfFileReader(open(infile, 'rb'))
    with open(outfile, 'w') as wr:
        for page in pdf.pages:
            wr.write(page.extractText())
    print("Wrote text version of the PDF to %s" % outfile)


def create_markov_chain_from_text(infile, outfile):
    """Read file in and create Markov chain, then pickle the resulting dict."""
    chain = defaultdict(list)
    exclude = set(string.punctuation)
    exclude.discard('-')
    with open(infile, 'r') as reader:
        for line in reader.readlines():
            line = ''.join([ch for ch in line if ch not in exclude])
            words = [w.lower() for w in line.strip().split(' ') if w != '']
            for i in range(0, len(words) - 2):
                key = (words[i], words[i + 1])
                chain[key].append(words[i + 2])
    pickle.dump(chain, open(outfile, 'wb'))
    print("Dumped chain to %s" % outfile)


def generate_text_from_chain(infile, iterations):
    """Generate text based on a saved Markov chain."""
    chain = pickle.load(open(infile, 'rb'))
    # Start the Markov chain
    start = choice(chain.keys())
    text = list(start)
    for _ in range(iterations):
        words = chain.get(start, None)
        if words:
            new_word = choice(words)
            text.append(new_word)
            start = (text[-2], text[-1])
        else:
            break
    display_generated_text(text)


def display_generated_text(text):
    """Print generated text."""
    height, width = map(int, os.popen('stty size', 'r').read().split())
    print("\n" + "-" * width)
    for word in text:
        print(word),
    print("...\n" + "-" * width)


if __name__ == '__main__':
    pdffile = "DouglasAdams_TheHitchhikerTrilogy_5Books1ShortStory.pdf"
    textfile = "flatland.txt"
    pickledfile = "flatland.p"
    iterations = 200
    #read_pdf(pdffile, textfile)
    create_markov_chain_from_text(textfile, pickledfile)
    generate_text_from_chain(pickledfile, iterations)
