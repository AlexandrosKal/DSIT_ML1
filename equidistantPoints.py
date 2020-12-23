import numpy as np
import math


'''
Getting N equidistant points
degree corresponds to the polynomial
'''
def getPoints(N,start,end,degree):

    maxDistance = end - start

    #since our N points are equidistant
    pointDistance = maxDistance / N

    points = np.arange(start,end,pointDistance)

    Fx = np.ones((N,degree))
    for i in range(degree):
        for j in range(N):
            Fx[j,i] = math.pow(points[j],i)

    return (points, Fx)