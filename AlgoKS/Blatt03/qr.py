#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def givens_rotation(A, i, j):
    """Return the rotation matrix ``J``, such that ``(J @ A)[i,j] = 0.0``

    Args:
        A (np.ndarray): Matrix in which an entry should be eliminated.
        i (int):        Row Index of the newly created zero.
        j (int):        Column Index of the newly created zero.

    Returns:
        np.ndarray: Rotation Matrix ``J`` as above.
    """
    pass  # TODO


def qr_decompose(A):
    """Return ``(Q, R)``, such that ``A = Q @ R``

    Args:
        A (np.ndarray): Matrix of which a QR-decomposition must be calculated.

    Returns:
        Tuple[np.ndarray,np.ndarray]: QR-decomposition in order ``(Q, R)``.
    """
    m, n = A.shape
    assert(m >= n)
    
    Q = np.eye(m)
    R = A.copy()

    # TODO


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
