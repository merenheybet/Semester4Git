#!/usr/bin/env python3

import numpy as np

from sparse_linalg import crs_assemble, cg


def assemble_poisson_matrix(N):
    """Assemble the system matrix A in CRS format for the discrete
    Poisson problem on an N x N square grid.

    Args:
        N (int): Number of grid points in each direction

    Returns:
        CrsMatrix: The system matrix in CRS format
    """
    pass  # TODO


def assemble_rhs(N, f, phi):
    """Assemble the right-hand side vector for the Poisson problem.

    Args:
        N (int): Number of grid points in each direction
        f ((float, float) -> float): Function of the source field;
            callable as f(x,y) with 0 <= x,y <= 1.
        phi ((float, float) -> float): Function specifying the Dirichlet
            boundary condition; callable as phi(x,y) with 0 <= x,y <= 1

    Returns:
        np.ndarray: Right-hand side vector as one-dimensional numpy array.
    """
    pass  # TODO


def solve_poisson(N, f, phi):
    """Solve the discretized Poisson problem on an N x N square grid
    with Dirichlet boundary condition phi and source field f.

    Args:
        N (int): Number of grid points in each direction
        f ((float, float) -> float): Function of the source field;
            callable as f(x,y) with 0 <= x,y <= 1.
        phi ((float, float) -> float): Function specifying the Dirichlet
            boundary condition; callable as phi(x,y) with 0 <= x,y <= 1

    Returns:
        np.ndarray: Two-dimensional array of shape (n, n) containing
            the values of the discrete solution u, with u_ij stored at index [j, i].
    """
    pass  # TODO


def main():
    pass  # Eigenen Test-Code hier einfügen


if __name__ == "__main__":
    main()
