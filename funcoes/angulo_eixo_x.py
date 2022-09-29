import math
from coeficientes_reduzida import main as extrai_coeficientes_reduzida
from geral_para_reduzida import main as transforma_geral_para_reduzida


def main(equacao: str) -> float:
    try:
        m, n = extrai_coeficientes_reduzida(equacao)
    except:
        try:
            m, n = extrai_coeficientes_reduzida(transforma_geral_para_reduzida(equacao))
        except:
            m, n = 0, 0  # caso default

    print(m, n)

    try:
        radians_angle = 1./math.tan(m)
    except ZeroDivisionError:
        radians_angle = 0

    degree_angle = math.degrees(radians_angle)
    return degree_angle


if __name__ == '__main__':
    print(main(' y = 3x + 1 '))
