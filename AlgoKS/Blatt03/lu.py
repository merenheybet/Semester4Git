#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def swap_rows(A, row1, row2):
    """Swap the rows ``row1`` and ``row2`` of ``A``.

    Args:
        A (np.ndarray): Matrix in which the rows are to be swapped.
        row1 (int):     Index of first row.
        row2 (int):     Index of second row.

    Returns:
        np.ndarray: The augmented matrix with swapped rows.
    """
    pass  # TODO


def subtract_scaled(A, dst, src, scale):
    """Subtract ``scale`` times the row ``src`` from the row ``dst`` of ``A``.

    Args:
        A (np.ndarray): Matrix in which the rows are to be subtracted.
        dst (int):      Index of the minuend.
        src (int):      Index of the subtrahend.
        scale (float):  Factor of the subtrahend.

    Returns:
        np.ndarray: The augmented matrix with subtracted rows.
    """
    pass  # TODO


def pivot_index(A, column):
    """Compute the row index of the maximum element of ``A`` in this ``column``,
    excluding all elements above the diagonal of ``A``.

    Args:
        A (np.ndarray): Matrix in which the pivot index is to be calculated in.
        column (int):   column to look in.

    Returns:
        int: The pivot index, satisfying the condition above.
    """
    pass  # TODO


def lu_decompose(A):
    """Return ``(P, L, U)``, such that ``A = P @ L @ U``.

    Args:
        A (np.ndarray): Matrix of which a PLU-decomposition must be calculated.

    Returns:
        Tuple[np.ndarray,np.ndarray,np.ndarray]:
            PLU-decomposition in order ``(P, L, U)``.
    """
    m, n = A.shape
    assert m == n

    P = np.eye(n)
    L = np.zeros((n, n))
    U = A.copy()

    # TODO

    return (P, L, U)


def forward_substitute(L, b):
    """Return ``y`` such that ``L @ y = b`` (*)

    Args:
        L (np.ndarray): Lower Triangular Matrix that fulfills the equation (*)
        b (np.ndarray): Vector on the r.h.s. of the equation (*)

    Returns:
        np.ndarray: Vector ``y``, such that (*) holds.
    """
    pass  # TODO


def backward_substitute(R, y):
    """Return ``x`` such that ``R @ x = y`` (**)

    Args:
        R (np.ndarray): Upper Triangular Matrix that fulfills the equation (**)
        y (np.ndarray): Vector on the r.h.s. of the equation (**)

    Returns:
        np.ndarray: Vector ``x``, such that (**) holds.
    """
    pass  # TODO


def linsolve(A, *bs):
    """Return ``(x_{0}, ..., x_{n-1})``, such that ``A @ xk = bs[k]``
    holds for every ``0 <= k <= n - 1``.

    Args:
        A (np.ndarray): LSE-Matrix
        *bs (List[np.ndarray]): Different r.h.s. in the equations.

    Returns:
        Tuple[np.ndarray, ...]: ``(x_{0}, ..., x_{n - 1})`` as mentioned above.
    """
    pass  # TODO
