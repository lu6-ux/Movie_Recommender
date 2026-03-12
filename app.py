import streamlit as st
import pandas as pd
import os
from model import recommend

st.title("🎬 AI Movie Recommendation System")

# Get base folder
BASE_DIR = os.path.dirname(__file__)

@st.cache_data
def load_movies():
    movies = pd.read_csv(os.path.join(BASE_DIR,"movies.csv"))
    movies = movies.rename(columns={'Movie Name':'title','Genre':'genres'})
    return movies
movies = load_movies()
selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        if i < len(names):

            col.write(names[i])
