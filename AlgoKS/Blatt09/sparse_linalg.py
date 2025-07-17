#!/usr/bin/env python3

import numpy as np


class CrsMatrix:
    def __init__(self, val, col_idx, row_ptr):
        self.val = val
        self.col_idx = col_idx
        self.row_ptr = row_ptr

    def __str__(self) -> str:
        return (
            f"CrsMatrix(val={self.val}, col_idx={self.col_idx}, row_ptr={self.row_ptr})"
        )

    def __repr__(self) -> str:
        return f"CrsMatrix(val={repr(self.val)}, col_idx={repr(self.col_idx)}, row_ptr={repr(self.row_ptr)})"


def crs_assemble(n, row_callback):
    """Assemble the CRS representation of an n x n matrix,
    with entries of each row given by `row_callback`.

    Args:
        n (int): Number of rows and columns of the matrix
        row_callback (int -> [(int, int)]): A function for computing the entries of each row.
            Given argument `j`, it returns a list of tuples `(val, col_idx)`, indicating that in
            column `col_idx` the matrix should have entry `val`.

    Returns:
        CrsMatrix: A named 3-tuple with entries `(val, col_idx, row_ptr)`, with types
            - `val`: NumPy-array with `float` entries
            - `col_idx`: NumPy-array with `int` entries
            - `row_ptr`: NumPy-array with `int` entries
    """
    total_vals = []
    total_col_idxs = []
    row_ptr = [0]
    row_ctr = 0

    for i in range(n):
        vals = []
        col_idxs = []
        combined_values = row_callback(i)
        for value in combined_values:
            vals.append(value[0])
            col_idxs.append(value[1])
        total_vals += vals
        total_col_idxs += col_idxs
        row_ctr += len(vals)
        row_ptr.append(row_ctr)
        
    
    return CrsMatrix(np.array(total_vals, dtype=float), np.array(total_col_idxs), np.array(row_ptr))


def crs_mvm(A, x):
    """Multiply the n x n matrix A, stored in CRS format, with the vector x of size n, to obtain y = A @ x.

    Args:
        A (CrsMatrix): Tuple `(val, col_idx, row_ptr)` of the n x n matrix
        x (np.ndarray): Vector of size n

    Returns:
        np.ndarray: The result vector y.
    """
    result_vector = np.zeros(x.shape)
    val_ctr = 0
    for i in range (0, len(A.row_ptr) - 1):
        num_elements_row = A.row_ptr[i+1] - A.row_ptr[i]
        for y in range(num_elements_row):
            a_ij = A.val[val_ctr + y]
            j = A.col_idx[val_ctr + y]
            res = a_ij * x[j]
            result_vector[i] += res
        val_ctr += num_elements_row

    return result_vector



def jacobi_step(A: CrsMatrix, b: np.ndarray, x: np.ndarray):
    """Perform one step of the Jacobi method.

    Args:
        A (CrsMatrix): The system matrix, stored in CRS format
        b (np.ndarray): The right hand-side vector of the system
        x (np.ndarray): The current approximate solution

    Returns:
        The new approximate solution after the Jacobi step
    """
    new_x = np.zeros(x.shape)

    for i in range(len(x)):
        row_start = A.row_ptr[i]
        row_end = A.row_ptr[i+1]
        total = 0
        diag = 0

        for index in range(row_start, row_end):
            j = A.col_idx[index]
            a_ij = A.val[index]
            if i == j:
                diag = a_ij
            else:
                total += a_ij * x[j]

        new_x[i] = (b[i] - total) / diag

    return new_x

def sor_step(A: CrsMatrix, b: np.ndarray, x: np.ndarray, w: float):
    """Perform one step of the successive over-relaxation Gauss-Seidel method.

    Args:
        A (CrsMatrix): The system matrix, stored in CRS format
        b (np.ndarray): The right hand-side vector of the system
        x (np.ndarray): The current approximate solution
        w (float): The relaxation parameter, with 0.5 < w < 2.

    Returns:
        The new approximate solution after the SOR step
    """
    for i in range(len(x)):
        row_start = A.row_ptr[i]
        row_end = A.row_ptr[i+1]
        total = 0
        diag = 0

        for index in range(row_start, row_end):
            j = A.col_idx[index]
            a_ij = A.val[index]
            if i == j:
                diag = a_ij
            else:
                total += a_ij * x[j]

        x_temp = (b[i] - total) / diag
        x[i] = (1 - w) * x[i] + x_temp * w
    return x

def cg(A, b, x0, epsilon=1e-6, max_iter=100):
    """Run the conjugate gradient algorithm on the system Ax = b, with starting vector x0, until the
    norm of the residual falls below epsilon.

    Args:
        A (CrsMatrix): The system matrix, stored in CRS format
        b (np.ndarray): Right-hand side of the system
        x0 (np.ndarray): The starting vector of the iteration

    Returns:
        (np.ndarray, int): The approximate solution reached after `nmax` steps, or earlier if
            a residual norm of <= epsilon was reached; and the number of steps the algorithm took.

    """
    def cg_step(A, b, x, r, d, epsilon, max_iter):
        if max_iter < 0:
            return (x, 100)
        if np.linalg.norm(r) < epsilon:
            return (x, 100 - max_iter)
        alpha = (r.T @ r) / (d.T @ crs_mvm(A, d))
        next_x = x + (alpha * d)
        next_r = r - (alpha * crs_mvm(A, d))
        beta = (next_r.T @ next_r) / (r.T @ r)
        next_d = next_r + (beta * d)
        return cg_step(A, b, next_x, next_r, next_d, epsilon, max_iter - 1)

    r = b - crs_mvm(A, x0)
    if np.linalg.norm(r) < epsilon:
        return (x0, 0)
    d = r
    return cg_step(A, b, x0, r, d, epsilon, max_iter)
    

def main():
    pass  # Eigenen Test-Code hier einfügen


if __name__ == "__main__":
    main()
