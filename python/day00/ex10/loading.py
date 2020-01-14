import time


def ft_progress(listy):
    inittime = time.time()
    for i in listy:


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += elem + 1
    sleep(0.01)
print()
print(ret)
