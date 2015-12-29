from tulip.grid import BinaryGrid
from PIL import Image
from itertools import product
import os
import sys
import click


def get_terminal_size():
    return map(int, os.popen('stty size', 'r').read().split())

def get_terminal_width():
    _, width = get_terminal_size()
    return width

def get_terminal_height():
    height, _ = get_terminal_size()
    return height

@click.command()
@click.option('--width', default=None, help='Width (in characters) of the image', type=int)
@click.option('--height', default=None, help='Height (in characters) of the image to represent', type=int)
@click.argument('image_path', type=click.Path(exists=True))
def tulip(width, height, image_path):
    width = width or get_terminal_width()
    height = height or get_terminal_height()

    binary_grid = BinaryGrid.from_file(image_path, width, height)

    for j in range(height):
        for i in range(width):
            if binary_grid[i, j]:
                print(" ", end="")
            else:
                print("#", end="")

        print('') # \n

