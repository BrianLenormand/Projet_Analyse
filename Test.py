# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
import scipy.sparse as sparse
from sklearn.cluster import KMeans
import collections
import time

start = time.clock()
ratings = pd.read_csv("/home/ink/Documents/2016_2017/Analyse de Donnée/Projet_Analyse/ratings.csv", sep = ",",
encoding='latin-1')
ratings = ratings.sort_values('movieId').reset_index()
ratings['movies_matrix'] = 0
df = pd.DataFrame(ratings)
df_movie = df.movieId
df_users = df.userId
df_rating = df.rating

matrix_movies={}
for k, v in enumerate(df_movie.unique()):
    matrix_movies[k] = v
movies_matrix = {v: k for k, v in matrix_movies.iteritems()}


for i in range(len(ratings)):
        ratings["movies_matrix"].ix[i] = movies_matrix[ratings["movieId"].ix[i]]
print ratings.head()
ratings.to_csv("NouveauRatings.csv")

end = time.clock()
print end-start