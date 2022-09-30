import math
try:
    from .coeficientes_reduzida import main as extrai_coeficientes_reduzida
    from .geral_para_reduzida import main as transforma_geral_para_reduzida
except ImportError:
    from coeficientes_reduzida import main as extrai_coeficientes_reduzida
    from geral_para_reduzida import main as transforma_geral_para_reduzida


def main(equacao: str) -> float:
    try:
        m, n = extrai_coeficientes_reduzida(equacao)
    except:
        m, n = extrai_coeficientes_reduzida(transforma_geral_para_reduzida(equacao))

    try:
        radians_angle = math.atan(m)
    except ZeroDivisionError:
        radians_angle = 0

    degree_angle = math.degrees(radians_angle) % 360
    if degree_angle < 0:
        degree_angle = 360 + degree_angle
    return round(degree_angle)


if __name__ == '__main__':
    print(main(' y = -5x + 3 '))
