#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# Now import the utilities from task 1.  Make sure the file imgutils.py is
# in the same folder as this file.
import imgutils


def compute_means(clusters):
    """Compute mean values for each cluster in the given list of clusters.

    Args:
        clusters (List[List[Tuple[int, int, int, int, int]]]):
            A list of clusters, i.e. a list of pixel-lists.

    Returns:
        List[Tuple[int, int, int]]:
            A list that has the same length as the list of clusters and
            contains to each cluster the average color value of it.

            This means, that ``len(retVal) == len(clusters)`` must hold after
            calling this function!
    """
    pass  # TODO


def compute_clusters(pixels, means):
    """Computes clusters for a given pixellist and means.

    Given a mean value ``m``, the cluster ``C_m`` with respect to ``m``
    consists of all points in ``pixels`` that are the closest to ``m``, whilst
    not being closer to any other mean value in ``means``:

    ```C_m = { (r,g,b,x,y) ∈ pixels | 2norm((r,g,b) - m)^2 ⩽
    2norm((r,g,b) - n)^2 for every n ∈ means with m ≠ n }```

    If a pixel has the same distance to multiple means, you **must** choose
    the mean with the lower index.

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.
        means (List[Tuple[int, int, int]]):
            A list of mean values of type ``(R, G, B)``.

    Returns:
        List[List[Tuple[int, int, int, int, int]]]:
            A list of clusters for every mean value in ``means``. A cluster
            consists of the points in pixels that are closest to the respective
            mean value of the cluster.

            **IMPORTANT**: It must hold, that your return value is of the same
            length as ``means``!
    """
    pass  # TODO


def averaged_pixels(clusters, means):
    """Calculates a pixel-list with averaged values.

    Args:
        clusters (List[List[Tuple[int, int, int, int, int]]]):
            List of clusters for every mean value in ``means``, i.e. a list
            of pixel-lists.
        means (List[Tuple[int, int, int]]):
            A list of mean values of type ``(R, G, B)``. Each mean value
            corresponds to a cluster at the same index in ``clusters``.

    Returns:
        List[Tuple[int, int, int, int, int]]:
            A list of all pixels from all clusters where the pixel colors have
            been replaced with the respective color of the mean value.
    """
    assert(len(clusters) == len(means))
    pass  # TODO


def kmeans(image, k):
    """Executes the k-means clustering algorithm for the given image.

    Args:
        image (int-array):
            A NumPy-Array of type ``uint8`` and shape (M, N, 3).
        k (int):
            Number of clusters the color space is divided into.

    Returns:
        int-array:
            A NumPy-Array of type ``uint8`` and shape (M, N, 3) representing
            the image created by the k-means clustering algorithm.
    """
    pixels = imgutils.image2pixels(image)
    pixels = pixel_kmeans(pixels, k)
    return imgutils.pixels2image(pixels)


def pixel_kmeans(pixels, k):
    """Executes the k-means clustering algorithm for the given image represented
    by a list of pixel colors and their positions.

    Finishes after the mean calculation does not result in new mean values.

    Args:
        pixels (List[Tuple[int, int, int, int, int]]):
            A List containing the ``(R, G, B)``-values of pixels at the
            position ``(X, Y)``.
        k (int):
            Number of clusters.

    Returns:
        List[Tuple[int, int, int, int, int]]:
            A List in the same format as the input list ``pixels`` was, filled
            with the averaged color values for each cluster.
    """
    # Ensure that k is never bigger than the number of pixels.
    k = min(k, len(pixels))
    # Choose some initial clusters.  A better strategy would improve the
    # algorithm quite a bit, but this simple technique is usually fine, too.
    clusters = [[pixels[i]] for i in range(0, len(pixels), len(pixels) // k)][:k]
    means = compute_means(clusters)
    while True:
        assert(len(means) == k)
        assert(len(clusters) == k)
        clusters = compute_clusters(pixels, means)
        new_means = compute_means(clusters)
        if means == new_means:
            return averaged_pixels(clusters, means)
        means = new_means


def main():
    #   Main-Funktion:
    #   Eigenen Test-Code bitte hier einfügen
    pass


if __name__ == "__main__":
    main()
