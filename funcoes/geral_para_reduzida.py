import math
def main(geral: str) -> str:
    # tratamento
    ca = float()
    cb = float()

    partes = list()
    geral = geral.lower()
    geral_tranformada = geral.split(" ")
    geral = str()

    for numero in geral_tranformada:
        geral += numero

    partes = geral.split('=')
    if partes[1] != "0":
        return Exception("A equacao geral deve ser igualada a zero")
    parteImportante = partes[0]

    if parteImportante[0] == "+":
        parteImportante = parteImportante[1:]

    if '+' in parteImportante:
        partes = parteImportante.split("+")
        partesTemporarias = list()
        if "" in partes:
            partes.remove("")
        for parte in range(len(partes)):
            if "-" in partes[parte]:
                partesMenos = partes[parte].split("-")
                if "" in partesMenos:
                    partesMenos.remove("")
                    partesMenos[0] = "-" + partesMenos[0]
                partesMenos[-1] = "-" + partesMenos[-1]
                if "--" in partesMenos[0]:
                    partesMenos[0] = partesMenos[0][1:]
                partesTemporarias+=partesMenos
            else:
                partesTemporarias.append(partes[parte])
        partes = partesTemporarias
        for coeficiente in partes:
            if coeficiente != "":
                print(coeficiente)

    elif '-' in parteImportante:
        partes = parteImportante.split("-")
        partesTemporarias = list()
        if "" in partes:
            partes.remove("")
            partes[0] = "-"+partes[0]
        for parte in range(len(partes))[1:]:
            partes[parte] = "-"+partes[parte]
        for coeficiente in partes:
            if coeficiente != "":
                print(coeficiente)


    else:
        return Exception("Problema")

    reduzida = 'y='
    divisor = None
    if partes[1] != 'y':
        divisor = partes[1].split('y')
        divisor.remove('')
        divisor = divisor[0]

    if divisor != 0:
        reduzida = reduzida + '('
        partes.pop(1)
        for a in partes:
            reduzida = reduzida + '-' + a
        reduzida + ')' + str(divisor)
    else:
        partes.pop(1)
        for a in partes:
            reduzida = reduzida + '-' + a

    return reduzida


if __name__ == "__main__":
    print(main('2x-8y-6=0'))
