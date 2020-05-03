from matplotlib import pyplot as plt
from numba import jit
from PIL import Image
import numpy as np


class Mandelbrot:
    """
    A class for the generation of mandelbrot sets.

    """
    def __init__(self, resolution: np.array, zoom: np.array):
        # the resolution of the image
        self.height = resolution[1]
        self.width = resolution[0]
        print(self.height)
        # the coordinates on which to zoom in on
        self.zoom_x = zoom[0]
        self.zoom_y = zoom[1]

        self.x_bound = np.array([-2, 1])
        self.y_bound = np.array([-1, 1])

    @jit
    def generate_fractal(self, max_iterations) -> np.array:
        """
        The mandelbrot set is symmetrical, therefore, only the top portion of
        the set must be generated.
        """
        image = np.zeros((self.height, self.width))
        colour = 0

        # for every pixel in the image
        for py in range(self.height):
            print(py)
            for px in range(self.width):
                # c is the coordinate related with the center of the pixel
                # (px, py)
                c = complex(self.x_bound[0] + (0.5 + px) * (
                            (self.x_bound[1] - self.x_bound[0]) / self.width),
                            (self.y_bound[1] - (0.5 + py) * (
                                self.y_bound[1] - self.y_bound[0]) / self.height
                             ))
                z = complex(0, 0)

                # test if the coordinate is bounded
                for iteration in range(max_iterations):
                    z_n = z * z + c
                    z = z_n

                    if z.real**2 + z.imag**2 > 4:
                        # then this pixel has escaped the bound, and colour the
                        # pixel depending on how many iterations it took to
                        # escape
                        colour = 0
                        break

                    if iteration == max_iterations - 1:
                        # then this pixel is bounded
                        colour = 255
                image[py, px] = colour
        return image

    def _set_bounds(self) -> None:
        pass

    def get_image(self) -> None:
        """
        Generate the image of the mandelbrot, with a scale and center
        coordinates
        """
        image = Image.fromarray(self.generate_fractal(max_iterations=300))
        image = image.convert("L")
        image.save('test.png')
