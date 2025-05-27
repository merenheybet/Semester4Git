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
    diag_value = A[j,j]
    elim_value = A[i,j]
    if diag_value == 0:
        sign = 1
    else:
        sign = np.sign(diag_value)
    vector_len = np.sqrt(diag_value**2 + elim_value**2)

    c = sign * diag_value / vector_len
    s = -sign * elim_value / vector_len

    J = np.eye(A.shape[0])
    J[j, j] = c
    J[i, i] = c
    J[j, i] = -s
    J[i, j] = s

    return J


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

    Js = []

    for i in range(n):
        for j in range(i+1, m):
            if R[j,i] == 0:
                continue
            J = givens_rotation(R, j, i)
            R = J @ R
            Js.insert(0, J)

    for J in Js:
        Q = Q @ J

    return (Q.T, R)


def backward_substitute(R, y):
    """Return ``x`` such that ``R @ x = y`` (**)

    Args:
        R (np.ndarray): Upper Triangular Matrix that fulfills the equation (**)
        y (np.ndarray): Vector on the r.h.s. of the equation (**)

    Returns:
        np.ndarray: Vector ``x``, such that (**) holds.
    """
    y_size, x_size = R.shape
    x_array = [0.] * y_size
    for j in range(y_size-1 , -1, -1):
        if j == y_size - 1:
            x_array[j] =  y[j,0] / R[j,j]
            continue
        
        x_j = y[j, 0]
        for i in range(y_size - 1, j - 1, -1):
            x_j -= R[j,i] * x_array[i]
        x_array[j] = x_j / R[j,j]

    return np.array([x_array]).T


def linsolve(A, *bs):
    """Return ``(x_{0}, ..., x_{n-1})``, such that ``A @ xk = bs[k]``
    holds for every ``0 <= k <= n - 1``.

    Args:
        A (np.ndarray): LSE-Matrix
        *bs (List[np.ndarray]): Different r.h.s. in the equations.

    Returns:
        Tuple[np.ndarray, ...]: ``(x_{0}, ..., x_{n - 1})`` as mentioned above.
    """
    Q, R = qr_decompose(A)
    result = []

    for b in bs:
        new_b = Q.T @ b
        result.append(backward_substitute(R, new_b))

    return tuple(result)
