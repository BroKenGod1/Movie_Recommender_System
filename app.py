import streamlit as st
import requests
import pandas as pd
import pickle
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetching posters
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Which movie do you want to recommend?',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

