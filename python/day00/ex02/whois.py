import sys

argc = len(sys.argv)
if argc == 1:
    sys.exit()
if argc > 2:
    print("ERROR")
    sys.exit()
try:
    n = int(sys.argv[1])
except ValueError:
    print("ERROR")
    sys.exit()
if n == 0:
    print("I'm Zero.")
elif n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
