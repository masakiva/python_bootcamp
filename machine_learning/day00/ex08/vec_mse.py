import numpy as np


def vec_mse(y, y_hat):
    """Computes the mean squared error of two non-empty numpy.ndarray,
without any for loop. The two arrays must have the same dimensions.
    Args:
     y: has to be an numpy.ndarray, a vector.
     y_hat: has to be an numpy.ndarray, a vector.
    Returns:
     The mean squared error of the two vectors as a float.
     None if y or y_hat are empty numpy.ndarray.
     None if y and y_hat does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
    """
    if type(y) is not np.ndarray or y.ndim != 1 or y.size == 0:
        return None
    if type(y_hat) is not np.ndarray or y_hat.ndim != 1 or y.size != y_hat.size:
        return None
    diff = y_hat - y
    xmean = diff.dot(diff)
    #xmean = sum(diff ** 2)
    return xmean / y.size

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(vec_mse(X, Y))
print(vec_mse(X, X))
