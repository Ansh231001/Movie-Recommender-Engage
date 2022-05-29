import pandas as pd
import pickle
import requests
import difflib

# IMPORTING PKL FILES CREATED USING JUYPTER NOTEBOOK#
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

#CONVERTING TO DATAFRAME
movies = pd.DataFrame(movies_dict)


#FETCHES POSTER FROM TMDB API 
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=64cee1e6331f2960d4607716fddd36f3'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']


#SEARCHES THE DATAFRAME OF MOVIES FOR SIMILAR MOVIES BASED ON SEARCH
def recommend(movie):
    req = difflib.get_close_matches(movie, movies['title']) ##GET CLOSE MATCH EVEN IF THE SEARCH IS NOT PRESENT IN DB
    if(len(req) == 0):
        return [] , []
    movie_index = movies[movies['title'] == req[0]].index[0] #USED KNN
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), #USED TIMSORT
                         reverse=True, key=lambda x: x[1])[1:10] #RETURNING TOP 10 MOVIES

    recommended_movies = []
    posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, posters

from app import views