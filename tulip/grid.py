from PIL import Image
from tulip.util import norm, get_average_color

class Grid(object):
    def __init__(self, image, width, height):
        self.width = width  # width * height = number of buckets
        self.height = height

        image = image.convert('RGB')
        image_width, image_height = image.size
        
        self.bucket_width = image_width // width
        self.bucket_height = image_height // height

        # make the buckets fit
        self.image = image.resize((width * self.bucket_width, height * self.bucket_height))

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
    def __init__(self, image, width, height):
       super(BinaryGrid, self).__init__(image, width, height)

       self.threshold = self.get_average_color_norm()

    def __getitem__(self, coordinates):
        color = super(BinaryGrid, self).__getitem__(coordinates)

        return norm(color) > self.threshold


    def get_average_color_norm(self):
        average_color = get_average_color(self.image)
        return norm(average_color)
       


