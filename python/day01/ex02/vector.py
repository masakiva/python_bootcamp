import sys


class Vector:
    def __init__(self, arg1, arg2=None):
        if type(arg1) is list:
            if arg2 is not None:
                sys.exit("A list of values must be the only argument")
            for f in arg1:
                if type(f) is not float:
                    sys.exit("The values must be represented by floats")
            self.values = arg1
            self.size = len(arg1)
        elif type(arg1) is int:
            if arg2 is None:
                self.values = []
                self.size = arg1
                for i in range(arg1):
                    self.values.append(float(i))
            elif type(arg2) is int:
                self.values = []
                self.size = 0
                for i in range(arg1, arg2, 1 if arg2 >= arg1 else -1):
                    self.values.append(float(i))
                    self.size += 1
            else:
                sys.exit("The second argument must be an int representing the end of the range")
        else:
            sys.exit("You can pass either a list of float values, a size or a range of vector in argument(s).")

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] + other
            return new
        elif type(other) is Vector and self.size == other.size:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] + other.values[i]
            return new
        else:
            sys.exit("The variable to add must be either an int, a float or a Vector of same size")

    def __radd__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = other + self.values[i]
            return new
        else:
            sys.exit("The variable to add must be either an int, a float or a Vector of same size")

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] - other
            return new
        elif type(other) is Vector and self.size == other.size:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] - other.values[i]
            return new
        else:
            sys.exit("The variable to substract must be either an int, a float or a Vector of same size")

    def __rsub__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = other - self.values[i]
            return new
        else:
            sys.exit("The variable to be substracted must be either an int or a float")

    def __truediv__(self, other):
        if (type(other) is int or type(other) is float) and other != 0:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] / other
            return new
        else:
            sys.exit("The variable to divide must be a non-null int or float")

    def __rtruediv__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = other / self.values[i]
            return new
        else:
            sys.exit("The variable to be divided must be either an int or a float")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = self.values[i] * other
            return new
        elif type(other) is Vector and self.size == other.size:
            new = 0
            for i in range(self.size):
                new += self.values[i] * other.values[i]
            return new
        else:
            sys.exit("The variable to multiply must be either an int, a float or a Vector of same size")

    def __rmul__(self, other):
        if type(other) is int or type(other) is float:
            new = Vector(self.size)
            for i in range(self.size):
                new.values[i] = other * self.values[i]
            return new
        else:
            sys.exit("The variable to multiply must be either an int, a float or a Vector of same size")

    def __str__(self):
        txt = ', '.join(str(f) for f in self.values)
        return txt

    def __repr__(self):
        return "vector of size " + str(self.size) + ": " + str(self.values)
