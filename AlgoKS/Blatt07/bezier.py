#!/usr/bin/env python3

import numpy as np


def de_casteljau_step(P, t):
    """For a given control polygon P of length N, return a control polygon of
    length N-1 by performing a single de Casteljau step with the given
    floating point number t.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.
        t (float):
            Step size for the De Casteljau Algorithm. Must be between 0 and 1.

    Returns:
        np.ndarray:
            A NumPy-Array of shape (N - 1, 2) representing the new control
            polygon after one De Casteljau step.
    """
    assert len(P) > 1, 0 <= t <= 1
    pass  # TODO


def de_casteljau(P, t):
    """Evaluate the Bezier curve specified by the control polygon P at a single
    point corresponding to the given t in [0,1]. Returns a one-dimensional
    NumPy array contining the x and y coordinate of the Point,
    respectively.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than **OR EQUAL** to 1!
        t (float):
            Step size for the De Casteljau Algorithm. Must be between 0 and 1!

    Returns:
        np.ndarray:
            A NumPy-Array of shape (2,) representing the point on the curve.
            It needs to be one-dimensional and have exactly **two** entries,
            the first one being the x-, and the second one the y-coordinate.
    """
    assert len(P) != 0, 0 <= t <= 1
    pass  # TODO


def bezier1(P, m):
    """Return a polygon with m points that approximates the Bezier curve
    specified by the control polygon P.

    The approximation is done by the ``de_casteljau``-function above and
    a uniform sampling of the interval [0, 1].

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.
        m (int):
            Number of points in the polygon that are used to approximate
            the Bezier curve.

    Returns:
        np.ndarray:
            A NumPy-Array of shape (m, 2) representing the polygon approximating
            the Bezier curve.
    """
    assert len(P) > 1, m > 1
    pass  # TODO


def add_control_point(P):
    """For the given Bezier curve control polygon P of length n, return a new
    control polygon with n+1 points that describes the same curve.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.

    Returns:
        np.ndarray:
            A NumPy-Array of shape (N + 1, 2) representing the control polygon
            of the same Bezier curve that P descrbes.
    """
    assert len(P) > 1
    pass  # TODO


def split_curve(P):
    """Split a Bezier curve, specified by a control polynomial P. Return a
    tuple (L, R), where L and R are control polygons with the same
    length as P, that describe the left and the right half of the original
    curve, respectively.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.

    Returns:
        Tuple[np.ndarray, np.ndarray]:
            A Tuple of two NumPy-Arrays of shape (N, 2) representing the
            control polygons of the two halves of the original Bezier curve.
    """
    assert len(P) > 1
    pass  # TODO


def bezier2(P, depth):
    """Return a polygon that approximates the Bezier curve specified by the
    control polygon P by depth recursive subdivisions.

    Args:
        P (np.ndarray):
            A NumPy-Array of shape (N, 2) representing the control polygon
            of the Bezier curve. N should be greater than 1.
        depth (int):
            Number of steps for the recursive subdivisions. depth should
            not be negative.

    Returns:
        np.ndarray:
            A NumPy-Array of shape (2^depth * (N - 1) + 1, 2) representing
            a polygon approximating the Bezier curve.
    """
    assert len(P) > 1, depth >= 0
    pass  # TODO


def main():
    pass


if __name__ == "__main__":
    main()
