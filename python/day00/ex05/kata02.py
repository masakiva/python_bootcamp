def printtime(t):
    print("{0[3]:02d}/{0[4]:02d}/{0[2]:04d} {0[0]:02d}:{0[1]:02d}".format(t))


t = (3, 30, 2019, 9, 25)
printtime(t)
