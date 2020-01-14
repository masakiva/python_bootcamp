import random

x = 1

x = 12 + x

print(x)

z = "print"
y = 'this'

# print(z + " " + y)

x = str(x)

def mafonction(arg):
    print(arg, type(arg))

mafonction(x)

a = 1

while a < 7:
    a += 1
    print(a)

for i in range(4):
    ran = random.random()
    print("U:", ran)
