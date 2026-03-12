import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

BASE_DIR = os.path.dirname(__file__)

# Load dataset
movies = pd.read_csv(os.path.join(BASE_DIR,"movies.csv"))

movies = movies.rename(columns={'Movie Name':'title','Genre':'genres'})

for col in ['overview','keywords']:
    if col not in movies.columns:
        movies[col] = ''

movies['tags'] = movies['overview'] + " " + movies['genres'] + " " + movies['keywords']

# Create TF-IDF vectors
vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
vectors = vectorizer.fit_transform(movies['tags'])

def recommend(movie):
    
    try:
        idx = movies[movies['title'] == movie].index[0]
    except:
        return ["Movie not found"]*5

    movie_vector = vectors[idx]
    similarity = cosine_similarity(movie_vector, vectors).flatten()

    recommended_idx = similarity.argsort()[-6:-1][::-1]


    return [movies.iloc[i].title for i in recommended_idx]
