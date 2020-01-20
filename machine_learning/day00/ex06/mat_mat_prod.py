import numpy as np


def dot(x, y):
    """Computes the dot product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have the same dimensions.
    Args:
     x: has to be an numpy.ndarray, a vector.
     y: has to be an numpy.ndarray, a vector.
    Returns:
     The dot product of the two vectors as a float.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
    """
    if type(x) is not np.ndarray or x.ndim != 1 or x.size == 0:
        return None
    if type(y) is not np.ndarray or y.ndim != 1 or x.size != y.size:
        return None
    xydot = 0.0
    for i in range(x.size):
        xydot += x[i] * y[i]
    return xydot


def mat_mat_prod(x, y):
    """Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * p.
    Returns:
     The product of the matrices as a matrix of dimension m * p.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
"""
    if type(x) is not np.ndarray or x.ndim != 2 or x.size == 0:
        return None
    if type(y) is not np.ndarray or y.ndim != 2 or y.size == 0:
        return None
    xi, xj = x.shape
    yi, yj = y.shape
    if xj != yi:
        return None
    prod = np.empty((xi, yj), dtype=np.int64)
    for i in range(xi):
        for j in range(yj):
            prod[i][j] = dot(x[i], y.T[j])
    return prod


W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])
Z = np.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])
print(mat_mat_prod(W, Z))
print()
print(mat_mat_prod(Z, W))
