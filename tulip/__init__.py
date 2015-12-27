from tulip.grid import BinaryGrid
from itertools import product
import os, sys


def get_terminal_size():
    return map(int, os.popen('stty size', 'r').read().split())

def tulip():
    if len(sys.argv) != 2:
        print("Error: tulip needs one argument", file=sys.stderr)
    else:
        image_path = sys.argv[1]
        height, width = get_terminal_size()

        binary_grid = BinaryGrid(image_path, width, height)

        for j in range(height):
            for i in range(width):
                if binary_grid[i, j]:
                    print(" ", end="")
                else:
                    print("#", end="")



