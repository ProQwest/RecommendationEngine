#Max Kiluk
#4/13/2016

#[[i,j,r]]
#i = user
#j = movie
#r = rating

import numpy as np
import time

#load data, get number of movies, get user list, get mean ratings
data = np.load('train.npy')
numMovies = len(data)
userList = data[:,0]
meanRatings = np.mean(data[:,2])

#meanMovie = np.mean(data[:,1])
#meanUser = np.mean(data[:,0])

#subtract mean ratings from actual ratings
data[:,2] = data[:,2] - meanRatings

#?
for j in range numMovies
    a[j] = np.mean(data[data[:,1] == j,2])
    data[data[:,1] = j,2] -= a[j]

    
