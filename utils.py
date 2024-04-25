from math import sqrt

def colordistance(sliderred,slidergreen,sliderblue,randomred,randomgreen,randomblue):
    distance_percentage = sqrt((sliderred - randomred)**2 + (slidergreen - randomgreen)**2 + (sliderblue - randomblue)**2)
    return distance_percentage