#!/usr/bin/env python3

import numpy as np
import numpy.linalg


def interpolate_linearly(a, b):
    """Return an object of type numpy.poly1d with degree 1 that passes
    through a and b, i.e. interpolates linearly between a and b.

    Args:
        a (np.ndarray):
            A NumPy-Array of shape (2,) that represents the first point. The
            first coordinate is the x-coordinate, while the second one is the
            y-coordinate of the point.
        b (np.ndarray):
            A NumPy-Array of shape (2,) that represents the second point. The
            first coordinate is the x-coordinate, while the second one is the
            y-coordinate of the point.

    Returns:
        np.poly1d:
            A NumPy-Polynomial that interpolates linearly between a and b.
    """
    pass  # TODO


def newton_matrix(X):
    """Setup the matrix of the LSE which is used to determine the coefficients
    of the Newton-basis.  X are the x-coordinates of the nodes which are
    used for interpolation.

    Args:
        X (np.ndarray):
            A NumPy-Array of shape (n,) that represents the x-coordinates of
            the to be interpolated nodes.

    Returns:
        np.ndarray:
            A NumPy-Array of shape (n, n) that represents the Newton-
            Coefficient-Matrix in the LSE that is used to determine the
            coefficients of the Newton-basis.
    """
    pass  # TODO


def newton_polynomial(C, X):
    """Take coefficients and interpolation point x-coordinates of the Newton-
    polynomial and determine the corresponding interpolation polynomial.

    Args:
        C (np.ndarray):
            A NumPy-Array of shape (n,) that represents the coefficients of
            the Newton-basis.
        X (np.ndarray):
            A NumPy-Array of shape (n,) that represents the x-coordinates of
            the to be interpolated nodes.

    Returns:
        np.poly1d:
            The Newton interpolation polynomial of the nodes.
    """
    assert len(C) == len(X)
    pass  # TODO


def interpolating_polynomial(X, Y):
    """Determine the interpolating polynomial for the given NumPy arrays of x
    and y coordinates.

    Args:
        X (np.ndarray):
            A NumPy-Array of shape (n,) that represents the x-coordinates of
            the to be interpolated nodes.
        Y (np.ndarray):
            A NumPy-Array of shape (n,) that represents the y-coordinates of
            the to be interpolated nodes.

    Returns:
        np.poly1d:
            The Newton interpolation polynomial of the nodes.
    """
    assert len(X) == len(Y)
    pass  # TODO


def main():
    pass


if __name__ == "__main__":
    main()
