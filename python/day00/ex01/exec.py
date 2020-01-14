import sys

j = len(sys.argv) - 1
if j == 0:
    sys.exit()
result = ""
while j > 0:
    for i in reversed(sys.argv[j]):
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    j -= 1
    if j > 0:
        result += " "
print(result)

# i = len(sys.argv) - 1
# if i > 0:
#     while i > 0:
#         print(str.swapcase(sys.argv[i])[::-1], end='')
#         i -= 1
#         if i > 0:
#             print(" ", end='')
#     print()
