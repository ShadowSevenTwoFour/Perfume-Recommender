#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:23:00 2023

@author: shadow
"""
from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def calculate_most_similar_cluster(query, vectorizer, perfume_data):
    num_clusters = len(set(perfume_data['Cluster']))
    max_similarity = -1
    most_similar_cluster = None

    for cluster in range(num_clusters):
        similarity = calculate_cluster_similarity(query, cluster, vectorizer, perfume_data)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_cluster = cluster

    return most_similar_cluster

def calculate_cluster_similarity(query, cluster, vectorizer, perfume_data):
    query_vector = vectorizer.transform([query])
    cluster_data = perfume_data[perfume_data['Cluster'] == cluster]
    cluster_vectors = vectorizer.transform(cluster_data['PreprocessedNotes'])

    similarities = cosine_similarity(query_vector, cluster_vectors)[0]
    max_similarity = max(similarities)

    return max_similarity

def predict():
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    perfume_data = pd.read_pickle('perfume_data.pkl')

    query = request.json['query']
    most_similar_cluster = calculate_most_similar_cluster(query, vectorizer, perfume_data)
    return jsonify({'Most similar cluster': most_similar_cluster})

if __name__ == '__main__':
    app.run()