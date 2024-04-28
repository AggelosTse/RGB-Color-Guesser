from math import sqrt


def colordistance(
    sliderred, slidergreen, sliderblue, randomred, randomgreen, randomblue
):
    """takes 3 RGB values from a random color, and 3 from slider's color,
    calculates their distance"""
    distance = sqrt(
        (sliderred - randomred) ** 2
        + (slidergreen - randomgreen) ** 2
        + (sliderblue - randomblue) ** 2
    )
    return (distance / 442.7) * 100
