from numba import jit
from PIL import Image
import numpy as np
import time


@jit(nopython=True, fastmath=True)
def generate_fractal(max_iterations, bounds) -> np.array:
    """
    The mandelbrot set is symmetrical, therefore, only the top portion of
    the set must be generated.

    Colour range from 0-255 gray-scale image.
    Apply a sigmoid transformation, meaning smaller no. of iterations makes
    pixel whiter
    """
    image_array = np.zeros((1000, 1500))
    colour = 0

    # for every pixel in the image
    for py in range(1000):
        # print("Completed: {}/{} rows".format(py, 2000 - 1))
        for px in range(1500):
            # c is the coordinate related with the center of the pixel
            # (px, py)
            c = complex(bounds[0][0] + (0.5 + px) * (
                        (bounds[0][1] - bounds[0][0]) / 1500),
                        (bounds[1][1] - (0.5 + py) * (
                            bounds[1][1] - bounds[1][0]) / 1000
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

            image_array[py, px] = colour

    return image_array


def get_image(name: str, bound) -> None:
    """
    Generate the image of the mandelbrot, with a scale and center
    coordinates
    """
    frame_ = Image.fromarray(generate_fractal(max_iterations=350,
                                              bounds=bound))
    frame_ = frame_.convert('L')
    frame_.save('{}.png'.format(name))
