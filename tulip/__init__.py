from tulip.grid import BinaryGrid
from PIL import Image
from itertools import product
import os, sys


def get_terminal_size():
    return map(int, os.popen('stty size', 'r').read().split())

def tulip():
    if len(sys.argv) != 2:
        print("Error: tulip needs one argument", file=sys.stderr)
    else:
        image = Image.open(sys.argv[1])
        height, width = get_terminal_size()

        binary_grid = BinaryGrid(image, width, height)

        for j in range(height):
            for i in range(width):
                if binary_grid[i, j]:
                    print(" ", end="")
                else:
                    print("#", end="")



