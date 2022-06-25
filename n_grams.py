from cleaning import cleaning
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import copy
from sklearn.feature_extraction.text import TfidfVectorizer
import re

X_train, Y_train = cleaning()
tok =[]
dataset = X_train.copy()

### getting the  top 50 frequent words in our dataset ###

for i in range(len(dataset)):
   dataset[i] = re.sub('[\W_]+', ' ', dataset[i])
   
for i in dataset:
    tokens = word_tokenize(i)
    for j in tokens:
        
       tok.append(j)
most_common_words= [word for word, word_count in Counter(tok).most_common(50)]

### getting different n-grams ###

def vectorize_unigram(dataset):
    tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1,1), stop_words = most_common_words)
    tfidf.fit(dataset)
    
    features = tfidf.transform(dataset)
    return features
def vectorize_bigram(dataset):
    tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(2,2), stop_words = most_common_words)
    tfidf.fit(dataset)
    features = tfidf.transform(dataset)
    return features
def vectorize_trigram(dataset):
    tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(3,3), stop_words = most_common_words)
    tfidf.fit(dataset)
    features = tfidf.transform(dataset)
    return features
def vectorize_12gram(dataset):
    tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1,2), stop_words = most_common_words)
    tfidf.fit(dataset)
    
    features = tfidf.transform(dataset)
    return features
def vectorize_13gram(dataset):
    tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1,3), stop_words = most_common_words)
    tfidf.fit(dataset)
    features = tfidf.transform(dataset)
    return features

def get_grams():
    return vectorize_unigram(X_train), vectorize_bigram(X_train), vectorize_trigram(X_train), vectorize_12gram(X_train),vectorize_13gram(X_train) 
