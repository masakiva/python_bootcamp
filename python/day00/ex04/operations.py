import sys


def ops(n1, n2):
    print("Sum:        ", n1 + n2)
    print("Difference: ", n1 - n2)
    print("Product:    ", n1 * n2)
    print("Quotient:   ", end=" ")
    try:
        print(n1 / n2)
    except ZeroDivisionError:
        print("ERROR (div by zero)")
    print("Remainder:  ", end=" ")
    try:
        print(n1 % n2)
    except ZeroDivisionError:
        print("ERROR (modulo by zero)")


def error():
    print("Usage: python operations.py")
    print("Example:\n\tpython operations.py 10 3")
    sys.exit()


argc = len(sys.argv)
if argc > 3:
    print("InputError: too many arguments\n")
elif argc == 2:
    print("InputError: too few arguments\n")
if argc != 3:
    error()
try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except ValueError:
    print("InputError: only numbers\n")
    error()
ops(n1, n2)
