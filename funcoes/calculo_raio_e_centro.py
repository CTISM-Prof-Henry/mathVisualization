def main(eq: str) -> tuple[float, float, float]:
    eq = eq.split('=')
    r = float(eq[1])**0.5
    eq = eq[0]

    eq = eq.split('(')

    for i in range(len(eq)):
        eq[i] = eq[i].split(')')

    if len(eq) == 3:
        eq.pop(0)
        a = eq[0][0].strip('x')
        if a == '':
            a = 0
        else:
            a = -float(a)

        b = eq[1][0].strip('y')
        if b == '':
            b = 0
        else:
            b = -float(b)

    elif len(eq) == 2:
        if 'x' in eq[0][0]:
            a = 0
            b = eq[1][0].strip('y')
            if b == '':
                b = 0
            else:
                b = -float(b)
        else:
            eq.pop(0)
            a = eq[0][0].strip('x')
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
    print(main('(x - a)**2 + (y - b)**2'))
