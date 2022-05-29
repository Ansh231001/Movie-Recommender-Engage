import pandas as pd
import pickle
from .engine import fetch_poster #IMPORTING FECTH POSTER FROM ENGINE.PY
import difflib


# IMPORTING PKL FILES CREATED USING JUYPTER NOTEBOOK SIMILAR TO ENGINE.PY#
movies_dict = pickle.load(open('Interests.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('interestSimilarity.pkl', 'rb'))

#SIMILAR TO RECOMMEND FUNCTION IN ENGINE.PY BUT STORES DATA ACCORING TO GENRES,TYPES ETC SEARCHED BY THE USER 
def interests(movie):
    req = difflib.get_close_matches(movie, movies['title']) #USED KNN, FOR BETTER RESULTS GET_CLOSE_MATCHES IS USED
    if(len(req) == 0):
        return [] , []
    movie_index = movies[movies['title'] == req[0]].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), #USED TIM SORT 
                         reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, posters
