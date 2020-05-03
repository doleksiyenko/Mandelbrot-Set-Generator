from settings import bounds
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
        # the coordinates on which to zoom in on
        self.zoom_x = zoom[0]
        self.zoom_y = zoom[1]

    @jit
    def generate_fractal(self, max_iterations) -> np.array:
        """
        The mandelbrot set is symmetrical, therefore, only the top portion of
        the set must be generated.

        Colour range from 0-255 gray-scale image.
        Apply a sigmoid transformation, meaning smaller no. of iterations makes
        pixel whiter
        """
        image = np.zeros((self.height, self.width))
        colour = 0

        # for every pixel in the image
        for py in range(self.height):
            print("Completed: {}/{} rows".format(py, self.height - 1))
            for px in range(self.width):
                # c is the coordinate related with the center of the pixel
                # (px, py)
                c = complex(bounds[0][0] + (0.5 + px) * (
                            (bounds[0][1] - bounds[0][0]) / self.width),
                            (bounds[1][1] - (0.5 + py) * (
                                bounds[1][1] - bounds[1][0]) / self.height
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

                        colour = 255 - (iteration * np.log2(
                            np.log2(z.real**2 + z.imag**2)))
                        break

                    if iteration == max_iterations - 1:
                        # then this pixel is bounded
                        colour = 255

                image[py, px] = colour

        return image

    def _set_bounds(self) -> None:
        pass

    def get_image(self, name: str) -> None:
        """
        Generate the image of the mandelbrot, with a scale and center
        coordinates
        """
        image = Image.fromarray(self.generate_fractal(max_iterations=255))
        image = image.convert('L')
        image.save('{}.png'.format(name))

