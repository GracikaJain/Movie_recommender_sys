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
import re

def download_file(url, output_path):
    try:
        urllib.request.urlretrieve(url, output_path)
        st.success(f"Downloaded {os.path.basename(output_path)} successfully.")
    except Exception as e:
        st.error(f"An error occurred while downloading the file: {e}")
        st.stop()

def extract_download_link(readme_path, file_name):
    try:
        with open(readme_path, 'r') as file:
            readme_content = file.read()
        # Regex to find URL ending with the file name
        url_pattern = re.compile(rf'https?://\S+/{file_name}')
        match = url_pattern.search(readme_content)
        if match:
            return match.group(0)
        else:
            st.error(f"No download link found for {file_name} in the README.")
            st.stop()
    except Exception as e:
        st.error(f"An error occurred while reading the README file: {e}")
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
readme_path = os.path.join(current_dir, 'README.md')
movies_path = os.path.join(current_dir, 'movies.pkl')
similarity_path = os.path.join(current_dir, 'similarity.pkl')

# Extract the download link from the README file
download_link = extract_download_link(readme_path, 'similarity.pkl')

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
