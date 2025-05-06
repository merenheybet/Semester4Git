import numpy as np


def reflection2d(omega):
    """Construct a 2D reflection matrix from the line angle `omega`.

    Args:
        omega (float): Rotation-Angle

    Returns:
        np.ndarray: The resulting rotation matrix of dimension (2, 2).
    """
    pass  # TODO


def eye(n, m):
    """Construct an identity matrix, i.e. a matrix with ones on its diagonal
    and zeros everywhere else, of arbitrary shape.

    Args:
        n (int): Number of Rows
        m (int): Number of Columns

    Returns:
        np.ndarray: The resulting "identity matrix" of dimension (n, m).
    """
    pass  # TODO


def compose(matrices):
    """Compose the given `matrices` to one single matrix.

    Args:
        matrices (list[np.ndarray]): Input matrices.

    Returns:
        np.ndarray: Composed Matrix.
    """
    assert matrices, "Expected at least one matrix"
    pass  # TODO


def antidiag(values):
    """Construct an antidiagonal matrix.

    Args:
        values (list[float]): The values on the antidiagonal.

    Returns:
        np.ndarray: The resulting anti-diagonal matrix.
    """
    assert len(values) >= 1
    pass  # TODO


def kronecker_product(A, B):
    """Calculate the Kronecker-Matrix-Product of ``A`` and ``B``.

    Returns:
        np.ndarray: The resulting matrix.
    """
    pass  # TODO


def walsh(n):
    """Construct the n-th Walsh Matrix.

    Returns:
        np.ndarray: The resulting matrix of dimension (2**n, 2**n).
    """
    pass  # TODO
