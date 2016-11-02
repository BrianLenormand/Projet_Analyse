# -*- coding: utf-8 -*-
import pandas as pd
#import graphlab
#train_data = graphlab.SFrame(ratings_base)
#test_data = graphlab.SFrame(ratings_test)

# pass in column names for each CSV and read them using pandas. 
# Column names available in the readme file

#Reading users file:
"""u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('tags.csv', sep='|', names=u_cols,
 encoding='latin-1')"""

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv("/home/ink/Documents/2016_2017/Analyse de Donnée/Projet_Analyse/ratings.csv", sep='\t', names=r_cols,
encoding='latin-1')
print ratings.shape
print ratings.head(50)

#Reading items file:
"""i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('/home/ink/Documents/2016_2017/Analyse de Donnée/Projet_Analyse/', sep='|', names=i_cols,
 encoding='latin-1')"""
