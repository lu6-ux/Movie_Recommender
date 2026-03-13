import streamlit as st
import pandas as pd
import os
from model import recommend

st.set_page_config(page_title="AI Movie Recommender", layout="wide")

st.title("🎬 AI Movie Recommendation System")

BASE_DIR = os.path.dirname(__file__)

@st.cache_data
def load_movies():
    movies = pd.read_csv(os.path.join(BASE_DIR,"dataset/movies.csv"))
    movies = movies.rename(columns={'Movie Name':'title','Genre':'genres'})
    return movies

movies = load_movies()

selected_movie = st.selectbox("🍿 Select a Movie", movies['title'].values)

# YouTube search links
def full_movie_link(movie):
    query = movie.replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}+full+movie"

def trailer_link(movie):
    query = movie.replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}+trailer"

if st.button("🎯 Recommend Movies"):

    names = recommend(selected_movie)

    st.subheader("🔥 Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    for i, col in enumerate([col1, col2, col3, col4, col5]):
        if i < len(names):

            movie = names[i]

            with col:
                st.markdown(f"### {movie}")

                # Full movie button
                st.markdown(
                    f"[🎬 Watch Full Movie]({full_movie_link(movie)})"
                )

                # Trailer button
                st.markdown(
                    f"[▶ Watch Trailer]({trailer_link(movie)})"
                )
