from math import sqrt

def colordistance(sliderred,slidergreen,sliderblue,randomred,randomgreen,randomblue):
    distance = sqrt((sliderred - randomred)**2 + (slidergreen - randomgreen)**2 + (sliderblue - randomblue)**2)
    return (distance / 442.7) * 100 