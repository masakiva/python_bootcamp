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
n += 1
regex = "[a-zA-Z]{" + str(n) + ",}"
words = []
for word in re.findall(regex, sys.argv[1]):
    words.append(word)
print(words)
