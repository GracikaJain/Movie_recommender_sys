'''import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies
st.title('Movie Recommender System')

movies_df = pickle.load(open('movies.pkl','rb'))
movies_list= movies_df['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name= st.selectbox(
'Select the movie!',
    movies_list)
if st.button('Recommend'):
    rec = recommend(selected_movie_name)
    for i in rec:
        st.write(i)

import streamlit as st
import pickle
import pandas as pd
import os

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[movie_id].title)

    return recommended_movies

st.title('Movie Recommender System')

# Ensure the files are in the same directory as this script
current_dir = os.path.dirname(__file__)
movies_path = os.path.join(current_dir, 'movies.pkl')
similarity_path = os.path.join(current_dir, 'similarity.pkl')

try:
    movies_df = pickle.load(open(movies_path, 'rb'))
    similarity = pickle.load(open(similarity_path, 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}. Please ensure the file is in the correct directory.")
    st.stop()

movies_list = movies_df['title'].values

selected_movie_name = st.selectbox('Select the movie!', movies_list)

if st.button('Recommend'):
    rec = recommend(selected_movie_name)
    for i in rec:
        st.write(i)
'''

import streamlit as st
import pickle
import pandas as pd
import os
import urllib.request

def download_file(url, output_path):
    try:
        urllib.request.urlretrieve(url, output_path)
        st.success(f"Downloaded {os.path.basename(output_path)} successfully.")
    except Exception as e:
        st.error(f"An error occurred while downloading the file: {e}")
        st.stop()

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[movie_id].title)

    return recommended_movies

st.title('Movie Recommender System')

# Ensure the files are in the same directory as this script
current_dir = os.path.dirname(__file__)
movies_path = os.path.join(current_dir, 'movies.pkl')
similarity_path = os.path.join(current_dir, 'similarity.pkl')

# Direct download link for similarity.pkl
download_link = 'https://drive.google.com/uc?export=download&id=1YqdujPMdCO_KF1um10B16_ZtOyC0icJ1'

# If similarity.pkl is not present, download it
if not os.path.isfile(similarity_path):
    download_file(download_link, similarity_path)

try:
    movies_df = pickle.load(open(movies_path, 'rb'))
    similarity = pickle.load(open(similarity_path, 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}. Please ensure the file is in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

movies_list = movies_df['title'].values

selected_movie_name = st.selectbox('Select the movie!', movies_list)

if st.button('Recommend'):
    rec = recommend(selected_movie_name)
    for i in rec:
        st.write(i)

