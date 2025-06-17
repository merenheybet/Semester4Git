#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def load_image(path):
    """Load the specified image as uint8 Numpy array.

    Args:
        path (str or file-like):
            The image file to read: a filename, or a file-like object opened in
            read-binary mode. (Copied from plt.imread's documentation)

    Returns:
        np.ndarray: A NumPy-Array of type ``uint8`` that contains the specified
            image. The returned array has shape (M, N, 3) for RGB images, and
            (M, N) for grayscale images.
    """
    return np.int64(plt.imread(path) * 255)


def image2pixels(image):
    """Create a list of ``(R, G, B, X, Y)`` tuples from a given 3d image array.

    This function is the inverse to the function ``pixels2image``, i.e.
    ```pixels2image(image2pixels(image)) = image.```

    Args:
        image (NumPy-array of integer type):
            A NumPy-Array of integer type and shape (M, N, 3).

    Returns:
        List[Tuple[int, int, int, int, int]]:
            A List containing all ``(R, G, B)``-values of the ``image`` together
            with the coordinates ``(X, Y)`` of the respective pixel.
    """
    rows, cols, colors = image.shape

    ret_list = []
    for y in range(rows):
        for x in range(cols):
            red = image[y,x,0]
            green = image[y,x,1]
            blue = image[y,x,2]
            ret_list.append((red, green, blue, x, y))
    
    return ret_list


def pixels2image(pixels):
    """Create a 3d image array from a list of (R, G, B, X, Y) pixels.

    This function is the inverse to the function ``image2pixels``, i.e.
    ```image2pixels(pixels2image(pixels))) = pixels.```

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.

    Returns:
        np.uint8-array:
            A NumPy-Array of type ``uint8`` and shape (M, N, 3) representing
            the image given by ``pixels``.
    """
    x_size = max(pixel[3] for pixel in pixels) + 1
    y_size = max(pixel[4] for pixel in pixels) + 1

    image = np.zeros((y_size, x_size, 3), dtype="uint8")

    for pixel in pixels:
        x_pos = pixel[3]
        y_pos = pixel[4]

        image[y_pos, x_pos,0], image[y_pos, x_pos,1], image[y_pos, x_pos,2] = pixel[0], pixel[1], pixel[2]

    return image


def bounding_box(pixels):
    """Return a tuple ``((Rmin, Rmax), (Gmin, Gmax), (Bmin, Bmax))`` with the
    respective minimum and maximum values of each color.

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.

    Returns:
        Tuple[Tuple[np.uint8, np.uint8], ...]:
            A tuple containing the respective minimum and maximum values of
            each color in the image represented by ``pixels``.
    """

    # The most inefficient solution
    ## Don't forget to optimise before Abgabe
    # red_max = max(pixel[0] for pixel in pixels)
    # red_min = min(pixel[0] for pixel in pixels)

    # green_max = max(pixel[1] for pixel in pixels)
    # green_min = min(pixel[1] for pixel in pixels)

    # blue_max = max(pixel[2] for pixel in pixels)
    # blue_min = min(pixel[2] for pixel in pixels)

    # return ((red_min, red_max), (green_min, green_max), (blue_min, blue_max))
    red_max = 0
    red_min = float('inf')

    blue_max = 0
    blue_min = float('inf')

    green_max = 0
    green_min = float('inf')

    for pixel in pixels:
        if pixel[0] > red_max:
            red_max = pixel[0]
        if pixel[0] < red_min:
            red_min = pixel[0]
        if pixel[1] > green_max:
            green_max = pixel[1]
        if pixel[1] < green_min:
            green_min = pixel[1]
        if pixel[2] > blue_max:
            blue_max = pixel[2]
        if pixel[2] < blue_min:
            blue_min = pixel[2]
            
    return ((red_min, red_max), (green_min, green_max), (blue_min, blue_max))

def color_average(pixels):
    """Return list of tuples (Ravg, Gavg, Bavg) with averaged color values.

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.

    Returns:
        Tuple[int, int, int]:
            A tuple containing the average value of red, green, and blue
            color values in the image represented by ``pixels``.
    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    length = len(pixels)

    for pixel in pixels:
        red_sum += pixel[0]
        green_sum += pixel[1]
        blue_sum += pixel[2]

    return (round(red_sum / length), round(green_sum / length), round(blue_sum / length))


def main():
    #   Main-Funktion:
    #   Eigenen Test-Code bitte hier einfügen
    pass


if __name__ == "__main__":
    main()
