import requests
import streamlit as st

try:
    TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
except Exception:
    TMDB_API_KEY = None

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def get_movie_poster(title):
    if not TMDB_API_KEY:
        return None

    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": title
    }

    try:
        response = requests.get(url, params=params).json()

        if response.get("results"):
            poster_path = response["results"][0].get("poster_path")
            if poster_path:
                return IMAGE_BASE + poster_path
    except:
        pass

    return None
