from .angulo_eixo_x import main as angulo_eixo_x_func
from .calculo_raio_e_centro import main as calculo_raio_e_centro_func
from .coeficientes_geral import main as coeficiente_geral_func
from .coeficientes_reduzida import main as coeficientes_reduzida_func
from .geral_para_reduzida import main as geral_para_reduzida_func
from .posicao_relativa import main as posicao_relativa_func
from .reduzida_para_geral import main as reduzida_para_geral_func


def get_number(number: str) -> int | float:
    """
    Converte a string de um número em um número inteiro ou flutuante.
    """
    try:
        _ = float(number)
    except ValueError:
        number = eval(number)

    try:
        _ = int(number)
    except ValueError:
        return float(number)

    return int(number) if float(number) == int(number) else float(number)
