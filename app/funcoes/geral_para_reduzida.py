from app.funcoes.coeficientes_geral import main as coeficientes_geral
from app.funcoes.torna_inteiro import main as torna_inteiro


def main(geral: str) -> str:
    reduzida = "y="

    a, b, c = coeficientes_geral(geral)

    base = torna_inteiro([a, b, c])
    a = int(a * base)
    b = int(b * base)
    c = int(c * base)

    if b < 0:
        b = b * -1
    elif b > 0:
        a = a * -1
        c = c * -1
    else:
        raise Exception("Precisa-se de um coeficiente b")

    coeficientes = {"x": a, None: c}

    temporaria = str()
    for letra, coeficiente in coeficientes.items():
        if coeficiente > 0:
            coeficiente = "+" + str(coeficiente)
        elif coeficiente < 0:
            coeficiente = str(coeficiente)
        else:
            coeficiente = None

        if coeficiente != None:
            if letra == None:
                temporaria += coeficiente
            else:
                if coeficiente == "+1":
                    coeficiente = "+"
                elif coeficiente == "-1":
                    coeficiente = "-"
                temporaria += coeficiente + letra

    if temporaria[0] == "+":
        temporaria = temporaria[1:]

    if b != 1:
        reduzida += "(" + temporaria + ")/" + str(b)
    else:
        reduzida += temporaria

    return reduzida


def testa(relacoes: dict[str: str]) -> bool:
    """
    Só um testadorzinho de cria ;)
    """
    final = dict()
    for k, v in relacoes.items():
        equacao = k
        resultado = v

        if main(equacao) == resultado:
            pass
        else:
            final[equacao] = "deu ruim"
            print(equacao + " deu ruim\n")
            return False
    if final == dict():
        print("Passou tudo")
    return True


if __name__ == "__main__":
    testa({
        "2x+2y+2=0": "y=(-2x-2)/2",
        "2x+y+2=0": "y=-2x-2",

        "x+y=0": "y=-x",
        "y-x=0": "y=x",

        "-y+x=0": "y=x",
        "-2y-x=0": "y=(-x)/2",
        "2y-x=0": "y=(x)/2",

        "(2y-2x-2)/2=0": "y=x+1",
    })
    print(main('1.0x +2.0y +3.0 = 0'))
