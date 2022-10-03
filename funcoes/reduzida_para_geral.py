from coeficientes_reduzida import main as coeficientes_reduzida
from torna_inteiro import main as torna_inteiro

def main(red: str) -> str:
    geral = str()
    m, n = coeficientes_reduzida(red)
    coeficienteB = torna_inteiro([m, n])
    coeficienteA = int(m*coeficienteB)
    coeficienteC = int(n*coeficienteB)

    if coeficienteA <= 0:
        coeficienteA*=-1
        coeficienteC*=-1
    else:
        coeficienteB*=-1

    coeficientes = {"x":coeficienteA, "y":coeficienteB, None:coeficienteC}

    for letra, coeficiente in coeficientes.items():
        if coeficiente > 0:
                coeficiente = "+"+str(coeficiente)
        elif coeficiente < 0:
            coeficiente = str(coeficiente)
        else:
            coeficiente = None
        if coeficiente!=None:
            if letra==None:
                geral+=coeficiente
            else:
                if coeficiente == "+1":
                    coeficiente = "+"
                elif coeficiente == "-1":
                    coeficiente = "-"
                geral += coeficiente+letra
    geral+="=0"
    if geral[0] == "+":
        geral = geral[1:]

    return geral

def testa(relacoes: dict[str : str]) -> bool:
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
            print(equacao+" deu ruim\n")
            return False
    if final == dict():
        print("Passou tudo")
    return True

if __name__ == "__main__":
    print(testa({
        "y=3x+1" : "3x-y+1=0",
        "y=3x-1" : "3x-y-1=0",
        "y=-3x-1" : "3x+y+1=0",

        "y=-3x" : "3x+y=0",
        "y=+3x" : "3x-y=0",
        "y=x" : "x-y=0",
        "y=-x" : "x+y=0",

        "y=-1" : "y+1=0",
        "y=1" : "y-1=0",
        "y=0" : "y=0",

        "y=(2x+2)/2" : "x-y+1=0",
        "y=(3x+2)/2" : "3x-2y+2=0",
    }))
