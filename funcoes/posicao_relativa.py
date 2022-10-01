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
        relacao = 'Secante'
    elif delta < 0:
        relacao = 'Disjuntas'
    else:
        relacao = 'Tangente'

    # obtendo as raizes da equacao de segundo grau
    # (abscissas dos pontos que interceptam a circunferencia)
    x1 = (-bb + delta**0.5) / (2 * aa)
    x2 = (-bb - delta**0.5) / (2 * aa)

    # obtendo a ordenada dos pontos que interceptam a circunferencia
    y1 = m*x1 + n
    y2 = m*x2 + n

    if x1 == x2:
        return relacao, (x1, y1), (x1, y1)
    else:
        return relacao, (x1, y1), (x2, y2)


if __name__ == '__main__':
    pass
    # main()