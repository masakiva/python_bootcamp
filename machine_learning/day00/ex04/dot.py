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

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(dot(Y, Y))
