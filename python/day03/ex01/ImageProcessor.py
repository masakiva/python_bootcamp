import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
imp.display(arr)
