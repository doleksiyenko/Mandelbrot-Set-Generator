from mandelbrot import Mandelbrot
from settings import _resolution, _zoom
import time

if __name__ == '__main__':
    _mandelbrot = Mandelbrot(resolution=_resolution, zoom=_zoom)
    print("Rendering...")
    time_a = time.time()

    _mandelbrot.get_image('set_1500_aspect')

    time_b = time.time()
    t = time_b - time_a
    print("Rendering took: {} seconds / {} minutes.".format(t, (t / 60)))
