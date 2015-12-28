from tulip.util import get_average_color, coordinates
from tulip.grid import Grid
from PIL import Image

def test_basic_grid():
    size = 100, 100
    image = Image.new('RGB', size)

    for i, j in coordinates(size):
        image.putpixel((i, j), (i, j * 2, i + j))

    grid = Grid(image, width=4, height=4)
    
    assert grid[0, 0] == get_average_color(image, width=25, height=25)
