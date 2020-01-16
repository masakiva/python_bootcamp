import sys
import re


def errorexit():
    print("ERROR")
    sys.exit()


argc = len(sys.argv)
if argc != 3:
    errorexit()
try:
    n = int(sys.argv[2])
except ValueError:
    errorexit()
ret = [w for w in re.findall("[a-zA-Z]+", sys.argv[1]) if len(w) > n]
print(ret)


# regex = "[a-zA-Z]{" + str(n + 1) + ",}"
# print(re.findall(regex, sys.argv[1]))
