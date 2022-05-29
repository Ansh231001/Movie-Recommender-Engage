# PSEUDODB SHOWS DATABASE IMPLEMENTATION. HERE SETFILTERS, SETRECOMMENDATIONS, SETINTRESTS STORE USER INFORMATION
# TO CATER CONTENT. REST READ FROM THE README FILE#

import pandas as pd
import numpy as np

setFil = [[], []]
setRec = [[], []]
setInt = [[], []]

def setFilters(Filter):
    setFil[0].clear()
    setFil[1].clear()
    setFil[0].extend(Filter[0] if Filter else [])
    setFil[1].extend(Filter[1] if Filter else [])

def setRecommendations(recommendations):
    setRec[0].clear()
    setRec[1].clear()
    setRec[0].extend(recommendations[0])
    setRec[1].extend(recommendations[1])

#THIS STORES THE INTERESTS OF USER BASED ON THE SEARCH. HENCE, IF THE APP
#IS RUNNING FOR CONTINOUS CYCLES THIS STORES THE DATA
def setInterests(interest):
    setInt[0].extend(interest[0])
    setInt[1].extend(interest[1])
