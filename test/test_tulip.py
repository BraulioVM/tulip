import sys
sys.path.append("..")

from tulip import tulip

def test_tulip(image_path):
   tulip(image_path)


test_tulip("resources/img.jpg")
