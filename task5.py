def two(l, d):
    l = list(l)
    while len(l) != 1:
        d.append(l[0]+l[1])
        l.pop(0)

def three(l, d):
    l = list(l)
    while len(l) != 2:
        d.append(l[0]+l[1]+l[2])
        l.pop(0)

def task():
    a = '123456789'
    l = []
    for i in a:
        l.append(i)
    two(a, l)
    three(a, l)
    return l

def matrix():
    l = task()
    one = [i for i in l if i[0] == '1'] 
    two = [i for i in l if i[0] == '2'] 
    three = [i for i in l if i[0] == '3']
    four = [i for i in l if i[0] == '4'] 
    five = [i for i in l if i[0] == '5'] 
    six = [i for i in l if i[0] == '6'] 
    seven = [i for i in l if i[0] == '7'] 
    eight = [i for i in l if i[0] == '8'] 
    nine = [i for i in l if i[0] == '9']
    l = [one, two, three, four,
    five, six, seven, eight, nine]
    return l

def if_(decision, num, i, r):
    decision2 = decision
    num2= num
    if r == 1:
        if decision2[-1] == '+':
            num2 += int(i)
            decision2 += i+'-'
        else:
            num2 -= int(i)
            decision2 += i+'+'
    elif r == 2:
        m = decision2.count('-')
        p = decision2.count('+')
        if p % 2 != 0:
            num2 += int(i)
            decision2 += i+'+'
        elif m % 2 != 0:
            num2 -= int(i)
            decision2 += i+'-' 
        else: 
            if decision2[-1] == '+':
                num2 += int(i)
                decision2 += i+'-'
            else:
                num2 -= int(i)
                decision2 += i+'+'
    elif r == 3:
        m = decision2.count('-')
        p = decision2.count('+')
        if '+' in decision2[:4]:
            if p % 2 != 0:
                num2 += int(i)
                decision2 += i+'+'
            elif decision2[-1] == '+':
                num2 += int(i)
                decision2 += i+'-'
            else:
                num2 -= int(i)
                decision2 += i+'+'
        else:
            if m % 2 != 0:
                num2 -= int(i)
                decision2 += i+'-'
            elif decision2[-1] == '-':
                num2 -= int(i)
                decision2 += i+'+'
            else:
                num2 += int(i)
                decision2 += i+'-'
    return decision2, num2

def nine(decision, num, m, d, r):
    decision2 = decision
    num2 = num
    if decision[-2] != '9':
        decision2, num2 = if_(decision, num, '9', r)
    d[decision2[:-1]] = num2

def eight(decision, num, m, d, r):
    for i in m[7]:
        decision2 = decision
        num2 = num
        if decision[-2] == '7':
            decision2, num2 = if_(decision, num, i, r)
        nine(decision2, num2, m, d, r)
            
def seven(decision, num, m, d, r):
    for i in m[6]:
        decision2 = decision
        num2 = num
        if decision[-2] == '6':
            decision2, num2 = if_(decision, num, i, r)
        eight(decision2, num2, m, d, r)

def six(decision, num, m, d, r):
    for i in m[5]:
        decision2 = decision
        num2 = num
        if decision[-2] == '5':
            decision2, num2 = if_(decision, num, i, r)
        seven(decision2, num2, m, d, r)

def five(decision, num, m, d, r):
    for i in m[4]:
        decision2 = decision
        num2 = num
        if decision[-2] == '4':
            decision2, num2 = if_(decision, num, i, r)
        six(decision2, num2, m, d, r)

def four(decision, num, m, d, r):
    for i in m[3]:
        decision2 = decision
        num2 = num
        if decision[-2] == '3':
            decision2, num2 = if_(decision, num, i, r)
        five(decision2, num2, m, d, r)

def three_(decision, num, m, d, r):
    for i in m[2]:
        decision2 = decision
        num2 = num
        if decision[-2] == '2':
            decision2, num2 = if_(decision, num, i, r)
        four(decision2, num2, m, d, r)

def two_(decision, num, m, d, r):
    for i in m[1]:
        decision2 = decision
        num2 = num
        if decision[-2] == '1':
            decision2, num2 = if_(decision2, num2, i, r)
        three_(decision2, num2, m, d, r)
                    
def plus_minus(m, d, r):
    for i in m[0]:
        decision = ''
        num = 0
        num += int(i)
        decision += i+'+'
        two_(decision, num, m, d, r)
            
def minus_plus(m, d, r):
    for i in m[0]:
        decision = ''
        num = 0
        num += int(i)
        decision += i+'-'
        two_(decision, num, m, d, r)

def done():
    m = matrix()
    d = {}
    plus_minus(m, d, 1)
    minus_plus(m, d, 1)
    plus_minus(m, d, 2)
    minus_plus(m, d, 2)
    # plus_minus(m, d, 3)
    # minus_plus(m, d, 3)
    print(len(d))
    d = {k:v for k,v in d.items() if v == 100}
    print(d)


if __name__ == "__main__":
    done()