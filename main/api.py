import requests

def get_popular_mouvies(page = 1):


    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]


    return []

def top_rated(page = 1):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    
    return []


def get_details(id:int):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    
    return {}

def get_videos(id:int):
    url = f"https://api.themoviedb.org/3/movie/{id}/videos"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("results")
        trailers = [film for film in data if film.get("type") == "Trailer"]
        return trailers
    return []

def get_similar_films(id:int, page = 1):
    url = f"https://api.themoviedb.org/3/movie/{id}/similar?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("results")
        return data
    return []

def get_upcoming_films(page = 1):
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page={page}"
    hearders = {
         "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }

    response = requests.get(url, headers=hearders)
    if response.status_code == 200:
        data = response.json().get("results")
        return data
    return []

def search_films(query, page=1):
    url = f"https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page={page}&query={query}"
    hearders = {
         "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTZiMjNmYzY5MmNkMTFiYTVjZWVlZDQzYTNiM2Q0MiIsInN1YiI6IjY0ZjBiZTFlY2FhNTA4MDBhYjcxZThmYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W4atZ6oMiLV6aUGyyKOhuXoWPGkSzbdkcbp_n101zeQ"
    }

    response = requests.get(url,headers=hearders)
    if response.status_code == 200 :
        data = response.json().get("results")
        return data
    return []

