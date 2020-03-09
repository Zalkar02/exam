def fib():
    l = [1, 1]
    while len(l) <= 100:
        l.append(l[-2]+l[-1])
    return l
