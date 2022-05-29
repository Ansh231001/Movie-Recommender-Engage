import pandas as pd
import requests

#API URL WITH THE API KEY
URL = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=64cee1e6331f2960d4607716fddd36f3'

#FETCHES THE POPULAR MOVIES FROM THE API(EXTRA FEATURE)
def popularity():
    movies = []
    posters = []
    response = requests.get(URL)
    data= response.json()
    results = data['results']
    for x in range(20):
        movies.append(results[x]['title'])
        posters.append('https://image.tmdb.org/t/p/w500' + results[x]['poster_path'])
    
    return movies , posters 
