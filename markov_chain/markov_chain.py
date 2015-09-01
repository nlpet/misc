"""Markov chain which reads text and then generates text."""
import pickle
from collections import defaultdict
from random import choice


def read_pdf(infile, outfile):
    """Read PDF and save text as .txt."""
    wr = open(outfile, 'w')
    import pyPdf
    pdf = pyPdf.PdfFileReader(open(infile, 'rb'))
    for page in pdf.pages:
        wr.write(page.extractText())


def create_markov_chain_from_text(infile, outfile):
    """Read file in and create Markov chain, then pickle the resulting dict."""
    chain = defaultdict(list)
    with open(infile, 'r') as reader:
        for line in reader.readlines():
            words = [w for w in line.strip().split(' ') if w != '']
            for i in range(1, len(words) - 2):
                key = (words[i], words[i + 1])
                chain[key].append(words[i + 2])
    pickle.dump(chain, open(outfile, 'wb'))
    print("Dumped chain to %s" % outfile)


def generate_text_from_chain(infile):
    """Generate text based on a saved Markov chain."""
    chain = pickle.load(open(infile, 'rb'))
    iterations = 10
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
    print(text)


if __name__ == '__main__':
    #create_markov_chain_from_text('Hitchhikers_Guide.txt', 'HGTTG.p')
    generate_text_from_chain("HGTTG.p")
