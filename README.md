# Mandelbrot Set Generator

This is a Python implementation of a mandelbrot set generator.
The file "mandelbrot.py" generates an image of the mandelbrot set given bounds of the real axis and imaginary axis. The process is sped up through the use of numba's JIT.

The file "main.py" generates a GIF given a point location found in "settings.py" (the variable _zoom). The number of frames rendered can be changed in "settings.py" as well.
"main.py" will create a new folder in the script's directory location, and then once all the images are generated, the imageio library generates the GIF.

The resolution of the image can also be adjusted in settings.


![Mandelbrot 3000x2000](https://github.com/doleksiyenko/Mandelbrot-Set-Generator/blob/master/images/set_3000.png)
