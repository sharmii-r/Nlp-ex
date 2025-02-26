#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# In[2]:


text = """
Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. 
The goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. 
Applications of NLP include machine translation, sentiment analysis, chatbots, and speech recognition. 
NLP combines computational linguistics with statistical, machine learning, and deep learning models.
"""


# In[3]:


from nltk.tokenize import word_tokenize, sent_tokenize

# Word Tokenization
words = word_tokenize(text)
print("Word Tokens:", words)

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokens:", sentences)


# In[4]:


from nltk import pos_tag

pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)


# In[5]:


from nltk import ne_chunk

named_entities = ne_chunk(pos_tags)
print("Named Entities:", named_entities)


# In[6]:


from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)


# In[7]:


from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("Stemmed Words:", stemmed_words)


# In[8]:


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print("Lemmatized Words:", lemmatized_words)


# In[14]:


from nltk import CFG
from nltk.parse import ChartParser

# Define a grammar that allows ambiguity
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    NP -> Det N | Det Adj N | 'NLP' | 'computers' | 'humans' | 'artificial' 'intelligence' | Adj N
    PP -> P NP
    Det -> 'the' | 'a'
    Adj -> 'natural' | 'useful' | 'artificial'
    N -> 'field' | 'language' | 'goal' | 'interaction' | 'applications' | 'intelligence'
    V -> 'is' | 'focuses' | 'enable' | 'include'
    P -> 'between' | 'of'
""")

# Create a parser
parser = ChartParser(grammar)

# Parse the sentence
sentence = "NLP is a field of artificial intelligence"
tokens = sentence.split()

# Check for possible parse trees
try:
    trees = list(parser.parse(tokens))
    if trees:
        print(f"Number of parse trees: {len(trees)}")
        for i, tree in enumerate(trees, 1):
            print(f"Parse Tree {i}:")
            print(tree)
            tree.pretty_print()
    else:
        print("No valid parse tree found.")
except ValueError as e:
    print("Error:", e)


# In[ ]:




