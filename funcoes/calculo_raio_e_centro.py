def main(eq: str) -> tuple[float, float, float]:
    eq = eq.split('=')
    try:
        r = float(eq[1])**0.5
    except:
        try:
            r = eval(eq[1])**0.5
        except:
            r = eq[1].split('^')
            r = float(r[0])
    eq = eq[0]

    eq = eq.split('(')

    for i in range(len(eq)):
        eq[i] = eq[i].split(')')

    if len(eq) == 3:
        eq.pop(0)
        a = eq[0][0].strip('x')
        a = a.replace(' ', '')
        if a == '':
            a = 0
        else:
            a = -float(a)

        b = eq[1][0].strip('y')
        b = b.replace(' ', '')
        if b == '':
            b = 0
        else:
            b = -float(b)

    elif len(eq) == 2:
        if 'x' in eq[0][0]:
            a = 0
            b = eq[1][0].strip('y')
            b = b.replace(' ', '')
            if b == '':
                b = 0
            else:
                b = -float(b)
        else:
            eq.pop(0)
            a = eq[0][0].strip('x')
            a = a.replace(' ', '')
            if a == '':
                a = 0
            else:
                a = -float(a)
            b = 0

    else:
        a = 0
        b = 0

    return a, b, r


if __name__ == '__main__':
    print(main('(x - 3)**2 + (y - 1)**2 = 4'))
    print(main('(x - 5)**2 + (y - 12)**2 = 5**2'))
    print(main('(x - 8)**2 + (y - 9)**2 = 0')) #averiguar
    print(main('(x - 2)**2 + (y - 2)**2 = 2**2'))
    print(main('(x - 2)**2 + (y - 3)**2 = 1'))



