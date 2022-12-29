import numpy as np
from PIL import Image


class Canvas:
    """
    Canvas:
            width
            height
            color
            make(imagepath)
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the [0,0,0] to input color
        self.data[:] = self.color

    def make(self, imagepath):
        # Converts the current array to an image
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
