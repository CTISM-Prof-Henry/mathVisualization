def main(equacao: str) -> tuple[float, float]:
    """
    Função que dada uma equacao de reta reduzida, retorna uma tupla em que, 
    na primeira posição encontra-se o coeficiente angular e na segunda o coeficiente linear
    """
    coeficienteAngular = float()
    coeficienteLinear = float()

    # Retira espaços:
    juntaTudo = equacao.split(" ")
    equacao = str()
    for numero in juntaTudo:
        equacao += numero

    # Seleciona parte importante da equacao
    primeiraParte = str(equacao.split("=")[0])
    segundaParte = str(equacao.split("=")[1])
    if primeiraParte.lower() != "y":
        raise Exception("equacao inserida errado")

    # Trata o primeiro +:
    if "+" == segundaParte[0]:
        processo = segundaParte
        segundaParte = str()
        for numero in range(len(processo)):
            if numero != 0:
                segundaParte += processo[numero]

    # Para os casos onde temos uma fração que englobe todos os membros da equacao:
    if "(" in segundaParte and ")" in segundaParte:
        numerador = segundaParte.split("(")[1].split(")")[0]
        denumerador = segundaParte.split(")")[1]
        # Trata os outros +:
        if "+" == numerador[0]:
            processo = numerador
            numerador = str()
            for numero in range(len(processo)):
                if numero != 0:
                    numerador += processo[numero]
        if "+" == denumerador[0]:
            processo = numerador
            denumerador = str()
            for numero in range(len(processo)):
                if numero != 0:
                    denumerador += processo[numero]

        # tratamento da virgula no denumerador
        if "," in denumerador:
            denumerador = denumerador.split(",")
            denumerador = denumerador[0] + "." + denumerador[1]
        coeficiente = str()
        partes = list()

        # Divide os coeficientes (linear e angular):
        if "+" in numerador:
            partes = numerador.split("+")
        elif "-" in numerador:
            partes = numerador.split("-")
            if "" in partes:
                partes.remove("")
                partes[0] = "-" + partes[0]
            partes[1] = "-" + partes[1]
        else:
            partes.append(numerador)

        # Pega cada coeficiente:
        for parte in partes:
            # Trata virgula:
            if "," in parte:
                parte = parte.split(",")
                parte = parte[0] + "." + parte[1]
            try:
                coeficienteLinear = float(eval(parte + denumerador))
            except:
                for numero in parte:
                    try:
                        tentaTransformarEmNumero = int(numero)
                        coeficiente += numero
                    except:
                        if numero == "/" or numero == "." or numero == "-" or numero == "+":
                            coeficiente += numero
                if len(parte) == 1:
                    coeficienteAngular = float(eval('1.0' + denumerador))
                elif len(parte) == 0:
                    coeficienteAngular = 0
                else:
                    coeficienteAngular = float(eval(coeficiente + denumerador))

    # Caso onde não temos uma fração que pega todos os coeficientes:
    else:
        coeficiente = str()
        partes = list()

        # Divide os coeficientes e trata os sinais
        if "+" in segundaParte:
            partes = segundaParte.split("+")
        elif "-" in segundaParte:
            partes = segundaParte.split("-")
            if "" in partes:
                partes.remove("")
                partes[0] = "-" + partes[0]
            partes[1] = "-" + partes[1]
        else:
            partes.append(segundaParte)

        # Pega cada coeficiente:
        for parte in partes:
            # Trata virgula:
            if "," in parte:
                parte = parte.split(",")
                parte = parte[0] + "." + parte[1]
            try:
                coeficienteLinear = float(eval(parte))
            except:
                for numero in parte:
                    try:
                        coeficiente += str(int(numero))
                    except:
                        if numero == "/" or numero == "." or numero == "-" or numero == "+":
                            if coeficiente == '' and numero != "+" and numero != '-':
                                coeficiente += "1.0"
                            coeficiente += numero
                if len(parte) == 1:
                    coeficienteAngular = 1.0
                elif len(parte) == 0:
                    coeficienteAngular = 0.0
                else:
                    coeficienteAngular = float(eval(coeficiente))

    return coeficienteAngular, coeficienteLinear


def testa(relacoes: 'dict[str : tuple[float,float]]') -> bool:
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
            return False
    if final == dict():
        print("Passou tudo")
    return True


if __name__ == "__main__":
    print(testa({
        " y = 3 x + 2": (3, 2),
        " y = 3 x -2 ": (3, -2),
        " y = - 3 x - 2 ": (-3, -2),
        " y = - 3 x + 2 ": (-3, 2),

        " y = (3 x -2)/2 ": (1.5, -1),
        " y = (+3 x +2)/2 ": (1.5, 1),
        " y = (-3 x -2)/2 ": (-1.5, -1),
        " y = (-3 x + 2)/2 ": (-1.5, 1),

        " y = x+2 ": (1, 2),
        " y = (x+2)/2 ": (0.5, 1),

        " y = x ": (1, 0),
        " y = x/2 ": (0.5, 0),
        " y = (x)/2 ": (0.5, 0),

        " y = (4)/2 ": (0, 2),
        " y = 4/2 ": (0, 2),
    }))
