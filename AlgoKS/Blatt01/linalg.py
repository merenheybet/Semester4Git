import numpy as np


def reflection2d(omega):
    """Construct a 2D reflection matrix from the line angle `omega`.

    Args:
        omega (float): Rotation-Angle

    Returns:
        np.ndarray: The resulting rotation matrix of dimension (2, 2).
    """
    return np.array([[np.cos(2 * omega), np.sin(2 * omega)], 
              [np.sin(2 * omega), -1 * np.cos(2 * omega)]])


def eye(n, m):
    """Construct an identity matrix, i.e. a matrix with ones on its diagonal
    and zeros everywhere else, of arbitrary shape.

    Args:
        n (int): Number of Rows
        m (int): Number of Columns

    Returns:
        np.ndarray: The resulting "identity matrix" of dimension (n, m).
    """
    return np.eye(n, m)


def compose(matrices):
    """Compose the given `matrices` to one single matrix.

    Args:
        matrices (list[np.ndarray]): Input matrices.

    Returns:
        np.ndarray: Composed Matrix.
    """
    assert matrices, "Expected at least one matrix"

    prev_matrix = None
    for matrix in matrices:
        if prev_matrix is None:
            prev_matrix = matrix
            continue
        else:
            prev_matrix = prev_matrix @ matrix
            continue
    
    return prev_matrix


def antidiag(values):
    """Construct an antidiagonal matrix.

    Args:
        values (list[float]): The values on the antidiagonal.

    Returns:
        np.ndarray: The resulting anti-diagonal matrix.
    """
    assert len(values) >= 1

    diag_values = np.array(values)
    diagonal_matrix = np.diag(diag_values)
    anti_diag = np.flipud(diagonal_matrix)
    return anti_diag


def kronecker_product(A, B):
    """Calculate the Kronecker-Matrix-Product of ``A`` and ``B``.

    Returns:
        np.ndarray: The resulting matrix.
    """
    array_list = []

    for line in A:
        row_result = []
        for number in line:
            temp_result = number * B
            row_result.append(temp_result)
        array_list.append(np.hstack(row_result))


    return np.vstack(array_list)



def walsh(n):
    """Construct the n-th Walsh Matrix.

    Returns:
        np.ndarray: The resulting matrix of dimension (2**n, 2**n).
    """
    if n==0: 
        return np.array([[1]])
    
    prev = walsh(n-1)
    upper_list = [prev, prev]
    lower_list = [prev, -1 * prev]
    upper = np.hstack(upper_list)
    lower = np.hstack(lower_list)
    total_list = [upper, lower]
    
    return np.vstack(total_list)
