# TODO: implementar codigo com as funcoes que capturam os
# TODO coeficientes das equacoes da reta e da circunferencia

def main(a, b, r, m, n) -> tuple[str, tuple[float, float], tuple[float, float]]:
    # pegando os coeficientes da formula de bhaskara
    aa = m**2+1
    bb = -2*a + 2*m*(n-b)
    cc = a**2 + (n-b)**2 - (r**2)

    # obtendo o delta
    delta = bb**2 - 4*aa*cc

    # determinando a relacao entre a reta e a circunferencia
    if delta > 0:
        relacao = 'Secantes'
    elif delta < 0:
        relacao = 'Disjuntas'
    else:
        relacao = 'Tangentes'

    # obtendo as raizes da equacao de segundo grau
    # (abscissas dos pontos que interceptam a circunferencia)
    x1 = round((-bb + delta**0.5) / (2 * aa), 2)
    x2 = round((-bb - delta**0.5) / (2 * aa), 2)

    # obtendo a ordenada dos pontos que interceptam a circunferencia
    y1 = round(m*x1 + n, 2)
    y2 = round(m*x2 + n, 2)

    if x1 == x2:
        return relacao, (x1, y1), (x1, y1)
    else:
        return relacao, (x1, y1), (x2, y2)


if __name__ == '__main__':
    print(main(2, 2, -3, 1, -1))
    print(main(6, -8, 0, 2, -1))
    print(main(2, -6, -27, 8, -3))
