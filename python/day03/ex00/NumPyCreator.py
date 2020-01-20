import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst, dtype='float32')

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr, dtype='float64')

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.empty(shape)

    def identity(self, n):
        return np.identity(n)

npc = NumPyCreator()
n1 = npc.from_list([[1,2,3],[6,3,4]])
n2 = npc.from_tuple(("a", "b", "c"))
n3 = npc.from_iterable(range(5))
shape = (3,5)
n4 = npc.from_shape(shape)
n5 = npc.random(shape)
n6 = npc.identity(4)
for n in [n1,n2,n3,n4,n5,n6]:
    print("array:\n", n)
    print("ndim:", n.ndim)
    print("shape:", n.shape)
    print("size:", n.size)
    print("dtype:", n.dtype)
    print("itemsize:", n.itemsize)
    print()
