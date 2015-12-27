from PIL import Image
from itertools import product
from functools import reduce
from tulip.util import norm, get_average_color

class Grid(object):
    def __init__(self, image_path, width, height):
        self.image = Image.open(image_path).convert('RGB')
        real_width, real_height = self.image.size
        
        self.width = width
        self.height = height

        self.bucket_width = real_width // width + 1 
        self.bucket_height = real_height // height + 1

        self.image = self.image.resize((width * self.bucket_width, height * self.bucket_height))

        self.buckets = {}

    def __getitem__(self, coordinates):
        i, j = coordinates
        width, height = self.width, self.height
        
        if i > width or j > height:
            raise(IndexError())

        if (i, j) in self.buckets: # memoize
            return self.buckets[i, j]

        real_i = i * self.bucket_width
        real_j = j * self.bucket_height

        result = get_average_color(self.image, real_i, real_j, self.bucket_width, self.bucket_height)
        self.buckets[i, j] = result

        return result
                 
class BinaryGrid(Grid):
    def __init__(self, image_path, width, height):
       super(BinaryGrid, self).__init__(image_path, width, height)

       self.threshold = self.get_average_norm()

    def __getitem__(self, coordinates):
        color = super(BinaryGrid, self).__getitem__(coordinates)

        return norm(color) > self.threshold


    def get_average_norm(self):
        average_color = get_average_color(self.image)
        return norm(average_color)
       
