def task(l):
    l = list(map(str,l))
    d = {}
    for i in l:
        d[l.index(i)] = int(l[1])
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    a = ''
    for i in d.keys():
        a += l[i]
    return a