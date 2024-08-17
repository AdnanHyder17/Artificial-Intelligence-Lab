# Use Spacy to perform the following tasks.
# 1. Create a syntactic dependency visualizer for a given sentence.
# 2. Break a given sentence into tokens each representing a single word.

import spacy
from spacy import displacy

# Load the English language model in Spacy
nlp = spacy.load('en_core_web_sm')

# Task 1: Create a syntactic dependency visualizer for a given sentence
def visualize_dependency(sentence):
    doc = nlp(sentence)
    displacy.render(doc, style='dep', jupyter=True)

# Task 2: Break a given sentence into tokens representing single words
def tokenize_sentence(sentence):
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    return tokens

# Sample usage
sentence = "The cat is sitting on the mat."

# Task 1: Visualize syntactic dependency of the sentence
visualize_dependency(sentence)

# Task 2: Tokenize the sentence into individual words
tokens = tokenize_sentence(sentence)
print(tokens)
