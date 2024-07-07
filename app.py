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
import os
import requests

def download_file_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            st.success(f"Downloaded {os.path.basename(destination)} successfully.")
        else:
            st.error(f"Failed to download file: {response.status_code}")
            st.stop()
    except Exception as e:
        st.error(f"An error occurred while downloading the file: {e}")
        st.stop()

def is_valid_pickle(file_path):
    try:
        with open(file_path, 'rb') as f:
            pickle.load(f)
        return True
    except Exception:
        return False

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[movie_id].title)

    return recommended_movies

# Main Streamlit App
def main():
    st.title('Movie Recommender System')

    # Ensure the files are in the same directory as this script
    current_dir = os.path.dirname(__file__)
    movies_path = os.path.join(current_dir, 'movies.pkl')
    similarity_path = os.path.join(current_dir, 'similarity.pkl')

    # Hardcoded Google Drive file ID for similarity.pkl
    file_id = "1YqdujPMdCO_KF1um10B16_ZtOyC0icJ1"

    # If similarity.pkl is not present, download it
    if not os.path.isfile(similarity_path):
        download_file_from_google_drive(file_id, similarity_path)

    # Validate the downloaded similarity.pkl file
    if not is_valid_pickle(similarity_path):
        st.error(f"Downloaded file is not a valid pickle file: {similarity_path}")
        st.stop()

    # Load movies.pkl and similarity.pkl
    try:
        with open(movies_path, 'rb') as f:
            movies_df = pickle.load(f)
        st.success("Loaded movies.pkl successfully.")
    except FileNotFoundError:
        st.error(f"File not found: {movies_path}. Please ensure the file is in the correct directory.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading movies.pkl: {e}")
        st.stop()

    try:
        with open(similarity_path, 'rb') as f:
            similarity = pickle.load(f)
        st.success("Loaded similarity.pkl successfully.")
    except FileNotFoundError:
        st.error(f"File not found: {similarity_path}. Please ensure the file is in the correct directory.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading similarity.pkl: {e}")
        st.stop()

    # Display movie selection dropdown
    if 'movies_df' in locals() and 'similarity' in locals():
        movies_list = movies_df['title'].values
        selected_movie_name = st.selectbox('Select the movie!', movies_list)

        if st.button('Recommend'):
            rec = recommend(selected_movie_name)
            for i in rec:
                st.write(i)

if __name__ == "__main__":
    main()
