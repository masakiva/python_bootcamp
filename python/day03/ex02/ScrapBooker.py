import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

class ScrapBooker:
    def crop(self, array, dimensions, position=(0,0)):
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            sys.exit("ERROR: the dimensions must not exceed original image size")
        starty = position[0]
        startx = position[1]
        endy = starty + dimensions[0]
        endx = startx + dimensions[1]
        return array[starty:endy, startx:endx, :]

    def thin(self, array, n, axis):
        return np.delete(array, np.s_[n - 1::n], axis)

    def juxtapose(self, array, n, axis):
        return np.tile(array, n)
    
    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)


class ImageProcessor:
    def load(self, path):
        img = mpimg.imread(path)
        print("Loading image of dimensions %d x %d" % img.shape[:-1])
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
manip = ScrapBooker()
imp.display(manip.juxtapose(arr, 2, 1))

# https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# https://www.google.com/search?client=firefox-b-d&q=matrix+product
# https://docs.scipy.org/doc/numpy/user/quickstart.html#indexing-slicing-and-iterating
