def task(a, b):
    l = []
    for i in a:
        l.append(i)
        l.append(b[a.index(i)])
    return l

