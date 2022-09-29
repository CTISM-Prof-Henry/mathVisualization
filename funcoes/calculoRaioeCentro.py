eq = '(x-a)**2 + (y - b)**2 = r**2'

eq = eq.split("=")
#eq = ['(x - a)**2 + (y - b)**2', 'r**2']
r = float(eq[1])**0.5
eq = eq[0]

#eq = '(x - a)**2 + (y - b)**2'
eq = eq.split("(")

#eq = ['x - a)**2 +', 'y - b)**2'
for parte in eq:
    parte.split(')')
    #eq = ['x- a', '**2+', 'y-b', '**2']
    eq.pop(3)
    eq.pop(1)
    eq = ['x - a', 'y - b']
    a = eq[0].strip('x')
    if a == '':
        a = 0
    else:
        a= -float(a)
    b= eq[1].strip('y')

    if b == '':
        b = 0
    else:
        b = -float(b)