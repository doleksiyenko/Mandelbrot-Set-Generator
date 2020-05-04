from mandelbrot import get_image
from settings import bounds
import time
from settings import _zoom, frames
import os
import shutil
import imageio
from natsort import natsorted


def initial_center_image(center_x, center_y) -> None:
    bounds[0, 0] = -1.5 + center_x
    bounds[0, 1] = 1.5 + center_x
    bounds[1, 0] = 1 + center_y
    bounds[1, 1] = -1 + center_y

    print(bounds)


def scale_bounds(scale) -> None:
    x_scale = scale * (bounds[0, 0] - bounds[0, 1]) / 2
    y_scale = scale * (bounds[1, 0] - bounds[1, 1]) / 2

    bounds[0, 0] -= x_scale
    bounds[0, 1] += x_scale
    bounds[1, 0] -= y_scale
    bounds[1, 1] += y_scale


def print_center() -> str:
    return ("x: {}, y: {}".format((bounds[0][1] + bounds[0][0]) / 2,
                                (bounds[1][1] + bounds[1][0]) / 2))


if __name__ == '__main__':
    # first, set the first bounds such that their center is the zoom point
    initial_center_image(_zoom[0], _zoom[1])
    # secondly, generate the images into a folder
    path = os.getcwd()
    try:
        # create a new folder for saving the images
        os.mkdir("animation_images")
    except OSError:
        print("The creation of the image folder was unsuccessful.")
    else:
        os.chdir("animation_images")
        print("Rendering...")
        time_a = time.time()
        # generate all the images
        for frame in range(1, frames + 1):
            time_d = time.time()
            get_image('frame_{}'.format(frame), bounds)
            time_c = time.time()
            scale_bounds(0.01)
            print("Complete: frame {} / {}. "
                  "Time : {} seconds".format(
                    frame,
                    frames,
                    time_c - time_d))
            # calculate the rendering time
        time_b = time.time()
        t = time_b - time_a
        print("Rendering took: {} seconds / {} minutes.".format(t,
                                                                round((t / 60),
                                                                      2)))

        # next, generate the video file using the images in the folder created
        images_directory = os.getcwd()

        print('Generating GIF...')
        with imageio.get_writer(path + '/movie.gif', mode='I') \
                as writer:
            for filename in natsorted(os.listdir(os.getcwd())):
                image = imageio.imread(filename)
                writer.append_data(image)

        # delete the folder full of the generated images
        os.chdir(path)
        try:
            shutil.rmtree(images_directory)
        except OSError as err:
            print("Could not delete the images folder. Reason: {}".format(err))

        print('Complete.')
