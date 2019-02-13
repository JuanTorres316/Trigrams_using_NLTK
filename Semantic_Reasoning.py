#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:25:48 2018

@author: Juan
"""

import nltk
from nltk.corpus import stopwords
import pandas
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

english_Stopwords = stopwords.words('english')
data = pandas.read_csv('/Users/Juan/Desktop/complaint_tool/CSV_File_Manipulation/Consumer_Complaints_2.csv')

narrative = data['Consumer complaint narrative']

dataset = [line.lower() for line in narrative]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

lsa = TruncatedSVD(n_components = 4 , n_iter = 1000)

lsa.fit(X)

concept_words = {}
terms = vectorizer.get_feature_names()

for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms, key = lambda x:x[1], reverse = True)
    sortedTerms = sortedTerms[:10]
    concept_words["Concept " + str(i)] = sortedTerms
     
for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)
                
