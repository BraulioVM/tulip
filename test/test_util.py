from tulip.util import color_sum, get_average_color, norm, coordinates

from functools import reduce
from PIL import Image


def test_color_sum():
   colors = [(i, 2*i, 3*i) for i in range(10) ]
   result = (9 * 10 / 2)
   total_sum = reduce(color_sum, colors, (0, 0, 0))

   assert (result, 2 * result, 3 * result) == total_sum


def test_basic_get_average_color():
   sample_size = (100, 100)
   sample_color = (200, 100, 150)
   test_image = Image.new('RGB', sample_size, sample_color)
   
   assert get_average_color(test_image) == sample_color
   assert get_average_color(test_image, x=10, y=20) == sample_color

   assert get_average_color(test_image, width=30, height=10) == sample_color



def test_gradient_get_average_color():
   sample_size = (10, 10)
   image = Image.new('RGB', sample_size)

   for i, j in coordinates(sample_size):
      image.putpixel((i, j), (i, 2 * j, 0))

   average_color = (4, 9, 0)

   assert get_average_color(image) == average_color

   assert get_average_color(image, width=2, height=2) == (0, 1, 0)

   assert get_average_color(image, x=8, y=8) == (8, 17, 0)


def test_norm():
   assert norm((0, 0, 0)) == 0
   assert norm((10, 20, 5)) == 100 + 400 + 25
