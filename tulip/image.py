from tulip.grid import Grid, BinaryGrid
from tulip.braille import get_braille_character
from PIL import Image

class TextImage(object):
    UnderlyingGrid = Grid
    def __init__(self, image, width, height):
        self.grid = self.UnderlyingGrid(image, width, height)

    @classmethod
    def from_file(Klass, image_path, width, height):
        image = Image.open(image_path)

        return Klass(image, width, height)
        

    def get_pixel(self, coordinates):
        return self.grid[coordinates]

    def show(self):
        width = self.grid.width
        height = self.grid.height
        
        for j in range(height):
            for i in range(width):
                print(self.get_pixel((i, j)), end='')
            
            print('') # \n


class BinaryImage(TextImage):
    UnderlyingGrid = BinaryGrid

    def get_pixel(self, coordinates):
        i, j = coordinates
        if self.grid[i, j]:
            return " "
        else:
            return "#"
            
class BrailleImage(TextImage):
    UnderlyingGrid = BinaryGrid
    
    def __init__(self, image, width, height):
        super(BrailleImage, self).__init__(image, width * 2, height * 4)

    def get_pixel(self, coordinates):
        print(coordinates)
        i, j = coordinates
        
        back_i = 2*i
        back_j = 4*j

        braille_grid = []

        for j in range(back_j, back_j + 4):
            braille_grid.append(
                (self.grid[back_i, j], self.grid[back_i + 1, j])
            )
        
        return get_braille_character(braille_grid)
