from tulip.util import get_average_color, coordinates
from tulip.grid import Grid
from PIL import Image
import os

def test_basic_grid():
    size = 100, 100
    image = Image.new('RGB', size)

    for i, j in coordinates(size):
        image.putpixel((i, j), (i, j * 2, i + j))

    grid = Grid(image, width=4, height=4)
    
    assert grid[0, 0] == get_average_color(image, width=25, height=25)
    assert grid[1, 0] == get_average_color(image, x=25, y=0, width=25, height=25)

    assert grid[0, 1] == get_average_color(image, x=0, y=25, width=25, height=25)

    assert grid[3, 3] == get_average_color(image, x=75, y=75, width=25, height=25)




def test_from_file():
    size = 100, 100
    filename = 'test.png'
    image = Image.new('RGB', size)
    
    for i, j in coordinates(size):
        image.putpixel((i, j), (i, j + 3, i + j))

    try:
        image.save(filename)
        grid = Grid.from_file(filename, width=2, height=2)
        assert grid[0, 0] == get_average_color(image, width=50, height=50)

        assert grid[1, 1] == get_average_color(image, x=50, y=50)
        
    finally:
        os.remove(filename)
        
