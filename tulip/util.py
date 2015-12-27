from itertools import product
from functools import reduce

def color_sum(color1, color2):
    return (color1[0] + color2[0],
        color1[1] + color2[1],
        color1[2] + color2[2]
    )

def divide(color, n):
    return (color[0] // n, color[1] // n, color[2] // n)

def get_average_color(image, x=0, y=0, width=None, height=None):
    
    width = width if width is not None else image.size[0] - x
    height = height if height is not None else image.size[1] - y

    coordinates = product(range(x, x + width), range(y, y + height))
    colors = ( image.getpixel(coordinate) for coordinate in coordinates )

    total_sum = reduce(color_sum, colors, (0, 0, 0))

    return divide(total_sum, width * height) 


def norm(color):
    return sum(c ** 2 for c in color)

def coordinates(size):
    i, j = size
    return product(range(i), range(j))
