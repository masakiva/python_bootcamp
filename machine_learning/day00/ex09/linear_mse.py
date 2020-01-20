import numpy as np


def linear_mse(x, y, theta):
    """Computes the mean squared error of three non-empty numpy.ndarray,
using a for-loop. The three arrays must have compatible dimensions.
    Args:
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     x: has to be an numpy.ndarray, a matrix of dimesion m * n.
     theta: has to be an numpy.ndarray, a vector of dimension n * 1.
    Returns:
     The mean squared error as a float.
     None if y, x, or theta are empty numpy.ndarray.
     None if y, x or theta does not share compatibles dimensions.
    Raises:
     This function should not raise any Exception.
    """
    if type(x) is not np.ndarray or x.ndim != 2 or x.size == 0:
        return None
    if type(y) is not np.ndarray or y.ndim != 1:
        return None
    if type(theta) is not np.ndarray or theta.ndim != 1:
        return None
    xi, xj = x.shape
    if xi != y.size or xj != theta.size:
        return None
    xmean = 0.0
    for i in range(y.size):
        xmean += (theta.dot(x[i]) - y[i]) ** 2
    return xmean / y.size

X = np.array([
[ -6, -7, -9],
    [ 13, -2, 14],
    [ -7, 14, -1],
    [ -8, -4, 6],
    [ -5, -9, 6],
    [ 1, -5, 11],
    [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print(linear_mse(X, Y, Z))
W = np.array([0,0,0])
print(linear_mse(X, Y, W))

