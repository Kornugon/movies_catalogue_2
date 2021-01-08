import requests
import random

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZTQxNDVhYWZmYTQ4MDQ5ODRkYTRlNDU2ODY1Y2IxNyIsInN1YiI6IjVmZjdiMWI4OTFmMGVhMDAzZjkyOTc2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y8xBRnexLAYN_tyO7lnXMHExTcoAs2LcJXj4XKcxIj8"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def generate_movies():
    """
    Randomise Popular Movies
    """
    data = []
    movies = get_popular_movies()["results"]

    for _ in range(len(movies)):
        show = random.choice(movies)
        if show not in data:
            data.append(show)
    return data


def get_movies(how_many):
    data = generate_movies()
    return data[:how_many]


"""
def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
"""


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


