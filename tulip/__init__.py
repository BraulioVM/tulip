from tulip.grid import BrailleGrid, BinaryGrid
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
@click.option(
    '--width', 
    default=None, 
    help='Width (in characters) of the image shell representation (defaults to the current shell width)', 
    type=int
)
@click.option(
    '--width-percentage', 
    '-wp', 
    default=100, 
    help='Percentage of the shell width that will be used to display the image (will be ignored if --width is specified)',
    type=float
)
@click.option(
    '--height', 
    default=None,
    help='Height (in characters) of the image shell representation (defaults to the current shell height)',
    type=int
)
@click.option(
    '--height-percentage',
    '-hp',
    default=100,
    help='Percentage of the shell height that will be used to display the image (will be ignored if --height is specified)',
    type=float
)
@click.option(
    '--just-ascii',
    default=False,
    help='Display image using just ascii characters',
    is_flag=True
)
@click.argument('image_path', type=click.Path(exists=True))
def tulip(width, width_percentage, height, height_percentage, just_ascii, image_path):
    width = width or int(get_terminal_width() * float(width_percentage) / 100)
    height = height or int(get_terminal_height() * float(height_percentage) / 100)

    if just_ascii:
        display_ascii_image(image_path, width, height)
    
    else:
        display_braille_image(image_path, width, height)


def display_ascii_image(image_path, width, height):
    binary_grid = BinaryGrid.from_file(image_path, width, height)

    for j in range(height):
        for i in range(width):
            if binary_grid[i, j]:
                print(' ', end='')
            else:
                print('#', end='')
        print('') # \n

def display_braille_image(image_path, width, height):
    grid = BrailleGrid.from_file(image_path, width, height)
    
    for j in range(height):
        for i in range(width):
            print(grid[i, j], end='')
        
        print('') # \n
