import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

movie_list = movies['title'].values

selected_movie = st.selectbox(
    'Select a movie',
    movie_list
)

def recommend(movie):

    similar_movies = similarity[movie].sort_values(ascending=False)[1:6]

    return similar_movies.index.tolist()

if st.button('Recommend'):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)