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

    # seleciona a parte mais importante com os coeficientes
    partes = geral.split('=')
    if partes[1] != "0":
        return Exception("A equacao geral deve ser igualada a zero")

    parteImportante = partes[0]

    #Separação dos coeficientes
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

    elif '-' in parteImportante:
        partes = parteImportante.split("-")
        partesTemporarias = list()
        if "" in partes:
            partes.remove("")
            partes[0] = "-"+partes[0]
        for parte in range(len(partes))[1:]:
            partes[parte] = "-"+partes[parte]

    else:
        return Exception("Algo de errado não esta certo!!")

    #manipulação da strig para dar a forma da reduzida
    reduzida = 'y='
    divisor = None

    #ve se a primiera parte tem algum coeficente antes do y
    if partes[0] != 'y':
        divisor = partes[1].split('y')
        divisor.remove('')
        divisor = divisor[0]

    if divisor != None:
        partes.pop(0)
        for a in partes:
            reduzida = reduzida + a
        reduzida + ')' + str(divisor)
    else:
        partes.pop(0)
        for a in partes:
            reduzida = reduzida + '-' + a

    return reduzida


if __name__ == "__main__":
    print(main('y-3x+2=0'))
