import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZTQxNDVhYWZmYTQ4MDQ5ODRkYTRlNDU2ODY1Y2IxNyIsInN1YiI6IjVmZjdiMWI4OTFmMGVhMDAzZjkyOTc2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y8xBRnexLAYN_tyO7lnXMHExTcoAs2LcJXj4XKcxIj8"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def generate_random_movies(list_type):
    """
    Randomise Popular Movies
    """
    data = []
    movies = get_movies_list(list_type)["results"]

    for _ in range(len(movies)):
        show = random.choice(movies)
        if show not in data:
            data.append(show)
    return data


def get_movies(how_many, list_type):
    """
    Generate random movies from popular type.
    For others types there is no randomise.
    """
    if list_type == "popular":
        data = generate_random_movies(list_type)
    else:
        data = get_movies_list(list_type)["results"]
    return data[:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


