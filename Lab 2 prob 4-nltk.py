# Perform the following tasks with NLTK.
# 1. Write a Python NLTK program to split the text sentence/paragraph into a list of words. Sample Below.
# 2. Write a Python NLTK program to create a list of words from a given string.
# 3. Write a Python NLTK program to tokenize words, sentence wise.

# NLTK Tasks
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Downloading punkt tokenizer if not already downloaded
nltk.download('punkt')

# Sample text
text = "Joe waited for train. The train got late. Jow took a cab. Had to attend conference late"

# Task 1: Split the text sentence/paragraph into a list of words
words_list = nltk.word_tokenize(text)
print("TASK 1 - LIST OF WORDS:", words_list)

# Task 2: Create a list of words from a given string
string = "Python is an amazing programming language!"
words_list_from_string = nltk.word_tokenize(string)
print("TASK 2 - LIST OF WORDS FROM STRING:", words_list_from_string)

# Task 3: Tokenize words, sentence wise
sentences_list = nltk.sent_tokenize(text)
words_sentence_wise = [nltk.word_tokenize(sentence) for sentence in sentences_list]
print("TASK 3 - TOKENIZED WORDS, SENTENCE WISE:", words_sentence_wise)
