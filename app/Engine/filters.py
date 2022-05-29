import pandas as pd
import numpy as np
import requests

#GENRE ARRAY FROM TMDB API
genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
          'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']

#GENRE ID FROM TMDB API. MAPPED TO SAME INDEX FROM GENRE. EG: ACTION HAS ID 28
genre_ID = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749 , 878 , 10770, 53 , 10752 , 37]


#FECTHES MOVIES BASED ON THE FILTERS
def genreFilter(requestedList):
    URL = "https://api.themoviedb.org/3/discover/movie?api_key=64cee1e6331f2960d4607716fddd36f3&language=en-US&sort_by=popularity.desc&with_genres="
    movies = []
    posters = []
    for idx in requestedList:
        URL = URL  + str(genre_ID[int(idx)]) +  ',' #TO LOG THE FILTERS USE THE PRINT(GENRE_ID[INT(IDX)])
    
    
    response = requests.get(URL)
    data= response.json()
    results = data['results']

    for x in range(len(results)):
        movies.append(results[x]['title'])
        posters.append('https://image.tmdb.org/t/p/w500' + results[x]['poster_path'])
        
    return movies,posters





