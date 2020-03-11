def task(l):
    l = list(map(str,l))
    d = {}
    for i in l:
        d[l.index(i)] = int(i[0])
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    a = ''
    print(d)
    for i in d.__reversed__():
        a += l[i]
    return a

print(task([122, 47, 3, 9]))