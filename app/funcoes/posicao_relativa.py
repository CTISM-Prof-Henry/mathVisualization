# TODO: implementar codigo com as funcoes que capturam os
# TODO coeficientes das equacoes da reta e da circunferencia

def main(a: int | float, b: int | float, r: int | float, m: int | float, n: int | float) -> tuple:
    """
    Calcula a relação entre uma reta e uma circunferência ('Secantes', 'Tangentes' ou 'Disjuntas'), e em que ponto elas
    se interceptam (se for o caso).

    :param a: centro da circunferência no eixo x.
    :param b: centro da circunferência no eixo y.
    :param r: raio da circunferência.
    :param m: coeficiente angular da reta.
    :param n: coeficiente linear da reta.
    :return: uma tupla onde o primeiro item é a relação entre a reta e a circunferência, e o segundo item uma outra
             tupla de duas posições, com as coordenadas em que a reta e a circunferência se interceptam.
    """
    # pegando os coeficientes da formula de Bhaskara
    aa = m**2+1
    bb = -2*a + 2*m*(n-b)
    cc = a**2 + (n-b)**2 - (r**2)

    # obtendo o delta
    delta = bb**2 - 4*aa*cc

    # determinando a relação entre a reta e a circunferência
    if delta > 0:
        relacao = 'Secantes'
    elif delta < 0:
        relacao = 'Disjuntas'
    else:
        relacao = 'Tangentes'

    if relacao != 'Disjuntas':
        # obtendo as raízes da equação de segundo grau
        # (abscissas dos pontos que interceptam a circunferência)
        x1 = round((-bb + delta**0.5) / (2 * aa), 2)
        x2 = round((-bb - delta**0.5) / (2 * aa), 2)

        # obtendo a ordenada dos pontos que interceptam a circunferência
        y1 = round(m*x1 + n, 2)
        y2 = round(m*x2 + n, 2)

        if x1 == x2:
            return relacao, (x1, y1), (x1, y1)
        return relacao, (x1, y1), (x2, y2)
    return relacao, (None, None), (None, None)


if __name__ == '__main__':
    print(main(100, 100, 3, 3, 1))
    print(main(2, 2, -3, 1, -1))
    print(main(6, -8, 0, 2, -1))
    print(main(2, -6, -27, 8, -3))
