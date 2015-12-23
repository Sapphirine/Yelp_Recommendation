__author__ = 'Simons'
import math
from textblob import TextBlob as tb

def tf(word, doc):
    return 0.5+0.5*doc.words.count(word) / len(doc.words)

def n_containing(word, doclist):
    return sum(1 for doc in dcolist if word in doc)

def idf(word, doclist):
    return math.log(len(doclist) / (1 + n_containing(word, doclist)))

def tfidf(word, doc, doclist):
    return tf(word, doc) * idf(word, doclist)