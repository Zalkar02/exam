def two(l, d):
    if len(l) == 1:
        return
    d[l[0]+'+'+l[1]] = int(l[0]) + int(l[1])
    return two(l[1:], d)

def two_(l, d):
    if len(l) == 1:
        return
    d[l[0]+'-'+l[1]] = int(l[0]) - int(l[1])
    return two_(l[1:], d)

def task():
    a = '123456789'
    d = {}    
    two(a, d)
    two_(a, d)
    print(d)
    return 123+45-67+8-9

task()