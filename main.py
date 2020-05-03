from mandelbrot import Mandelbrot
from settings import _resolution, _zoom

if __name__ == '__main__':
    _mandelbrot = Mandelbrot(resolution=_resolution, zoom=_zoom)
    _mandelbrot.get_image()
