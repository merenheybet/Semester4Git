#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# Now import the utilities from task 1.  Make sure the file imgutils.py is
# in the same folder as this file.
import imgutils


def cut_dimension(bbox):
    """Determine the longest side of the bounding box, i.e. 
    return 0, 1 or 2. In case of a draw, prefer the lower dimensions.

    Args:
        bbox (Tuple[Tuple[int, int], ...]): 
            A bounding box in the format of the function ``bounding_box()`` of
            the module ``imgutils``. This tuple has three entries, each of
            which consists of a tuple of two entries and corresponds to red,
            green, and blue, respectively. The 2-tuples then stand for the
            respective minimum and maximum values of each color.

    Returns:
        int:
            The index of the longest side of the bounding box. Herein, the
            number 0 stands for red, 1 stands for green, and 2 stands for blue.
            In case of a draw, the smaller value has to be returned.
    """
    pass  # TODO


def recursive_median_cut(pixels, N, bbox=False):
    """Implements the main part of the median cut algorithm **recursively**.

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.
        N (int):
            The number of recursive steps to be taken.
        bbox (Tuple[Tuple[int, int], ...], *optional*):
            A bounding box surrounding the pixels. Expects the format of
            the function ``bounding_box`` in the module ``imgutils``.

            **WARNING**: The paramter ``bbox`` does not need to be set!

    Returns:
        List[Tuple[int, int, int, int, int]]:
            A list in the format of the ``pixels`` parameter, yet is filled
            by the values of the median cut algorithm, i.e. some sort of
            average pixel values.
    """
    pass  # TODO


def median_cut(image, ncuts=8):
    """Perform the median cut algorithm on a given image.

    Args:
        image (np.uint8-array):
            A NumPy-Array of integer element type and shape (M, N, 3).
        ncuts (int, *optional*):
            The number of recursive steps the algorithm should perform.

    Returns:
        np.uint8-array:
            A NumPy-Array of type ``uint8`` and shape (M, N, 3) representing
            the image created by the median cut algorithm.
    """
    pass  # TODO


def main():
    #   Main-Funktion:
    #   Eigenen Test-Code bitte hier einfügen
    pass


if __name__ == "__main__":
    main()
