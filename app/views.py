from app import app
from flask import render_template, request

# importing features(engine) from Engine folder
from app.Engine.engine import recommend
from app.Engine.popularity_engine import URL, popularity
from app.Engine.interests import interests
from app.Engine.filters import genres, genreFilter
## **-------** ##


from .pseudoDB import setFil, setInt, setRec , setFilters , setRecommendations , setInterests


##LIST FOR POPULAR MOVIES 
##GLOBAL TO ALWAYS SHOW
results = popularity()


@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    interest = []
    Filter = []
    if request.method == "POST":

        ##POST REQUEST FOR SERACH
        req = request.form.get("search-bar")
        
        ##POST REQUEST FOR FILTERS
        req2 = request.form.getlist("myCheckbox") #TO LOG PRINT(request.form.getlist("myCheckbox"))

        ##IF NO SERACH IS PROVIDED
        if len(req) == 0 and len(req2) == 0:
            return render_template('public/index.html', movies=results[0], p2=results[1], p3=[], interests=[], btngrp=genres, filtered=[], p4=[])

        ##IF FILTER IS PROVIDED
        elif len(req) == 0 and len(req2) != 0:
            Filter = genreFilter(req2)
            setFilters(Filter)
            if(setFil == [[] , []]):
                return render_template('public/index.html', collections=setRec[0] if setRec else [], p1=setRec[1] if setRec else [], movies=results[0], p2=results[1], interests=setInt[0] if setInt else [], p3=setInt[1] if setInt else [], btngrp=genres,  filtered=["No data found"], p4=setFil[1])
            return render_template('public/index.html', collections=setRec[0] if setRec else [], p1=setRec[1] if setRec else [], movies=results[0], p2=results[1], interests=setInt[0] if setInt else [], p3=setInt[1] if setInt else [], btngrp=genres,  filtered=setFil[0], p4=setFil[1])

        ##IF SERACH IS PROVIDED
        elif len(req) != 0 and len(req2) == 0:
            recommendations = (recommend(req))
            setRecommendations(recommendations)
            interest = (interests(req))
            setInterests(interest)
            if(setRec == [[] , []] or setInt == [[] , []]):
                return render_template('public/index.html', collections=["No data Found"], p1=setRec[1], movies=results[0], p2=results[1], interests=setInt[0], p3=setInt[1], btngrp=genres,  filtered=setFil[0] if setFil else [], p4=setFil[1] if setFil else [])

            return render_template('public/index.html', collections=setRec[0], p1=setRec[1], movies=results[0], p2=results[1], interests=setInt[0], p3=setInt[1], btngrp=genres,  filtered=setFil[0] if setFil else [], p4=setFil[1] if setFil else [])
    
    return render_template('public/index.html', movies=results[0], p2=results[1], p3=[], interests=[], btngrp=genres, filtered=[], p4=[])


#FOR REFERENCING: VARIABLES ARE USED TO SEND DATA TO TEMPLATE

# collections=setRec[0]         ...movies for serach results
# p1=setRec[1],                 ...posters for serach results

# movies=results[0],            ...movies for popular section
# p2=results[1],                ...posters for popular section

# interests=setInt[0],          ...movies for interests
# p3=setInt[1],                 ...posters for interests

# filtered=setFil[0],           ...movies from filters
# p4=setFil[1]                  ...posters for filters

# btngrp=genres,                ...genre buttons

