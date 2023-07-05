#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:19:39 2023

@author: shadow
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def preprocess(notes):
    preprocessed_notes = []
    for element in notes:
        notes_list = []
        element = element.lower()  # Convert to lowercase
        preprocessed_notes.append(element) # Add current element to new Dataframe column
    return preprocessed_notes

def main():
    nltk.download('omw-1.4')
    nltk.download('wordnet')
    nltk.download('wordnet_ic')

    perfume_data = pd.read_excel('class_perfume_data.xlsx')
    perfume_data.dropna(inplace=True)

    perfume_data['PreprocessedNotes'] = preprocess(perfume_data['Notes'])

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(perfume_data['PreprocessedNotes'])

    # Apply K-means clustering
    num_clusters = 10
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(tfidf_matrix)

    perfume_data['Cluster'] = kmeans.labels_

    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
    perfume_data.to_pickle('perfume_data.pkl')

main()
