# TODO: implementar codigo com as funcoes que capturam os
# coeficientes das equacoes da reta e da circunferencia

def posicao_relativa(a, b, r, m, n) -> tuple[str, tuple[float, float], tuple[float, float]]:
    aa = m**2+1
    bb = -2*a + 2*m*(n-b)
    cc = a**2 + (n-b)**2 - (r**2)

    delta = bb**2 - 4*aa*cc

    if delta > 0:
        relacao = 'secante'
    elif delta < 0:
        relacao = 'externa'
        return relacao
    else:
        relacao = 'tangente'

    x1 = (-bb + delta**0.5) / (2 * aa)
    x2 = (-bb - delta**0.5) / (2 * aa)

    y1 = m*x1 + n
    y2 = m*x2 + n

    if x1 == x2:
        return relacao, (x1, y1)
    else:
        return relacao, (x1, y1), (x2, y2)

