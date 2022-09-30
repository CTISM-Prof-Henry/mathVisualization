def main(geral: str) -> str:
    # TODO tratamento da string recebida (isso funciona)
    partes = list()
    geral = geral.lower()
    geral_tranformada = geral.split(" ")
    geral = str()

    # Remove os espaços
    for numero in geral_tranformada:
        geral += numero

    # seleciona a parte mais importante com os coeficientes
    partes = geral.split('=')
    if partes[1] != "0":
        return Exception("A equacao geral deve ser igualada a zero")
    parteImportante = partes[0]

    # TODO Separação dos coeficientes (isso funciona)
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
        return Exception("Equação inserida errado, verifique! ")

    # TODO parte problemática: arrumar a equação com os coef. que separamos

    reduzida = 'y='
    # coeficiente que pode estar junto com o Y
    divisor = None

    # verifica se a primeira parte tem numero antes do y
    # Obs: "partes" é uma lista com os coeficientes
    if partes[0] != 'y':
        divisor = partes[1].split('y')
        divisor = divisor[0]

    # se tiver um divisor, joga para o outro lado
    if divisor != None:
        reduzida = reduzida + '('
        partes.pop(0)
        for a in partes:
            reduzida = reduzida + a
            reduzida + ')' + str(divisor)

    # se não tiver, junta as partes e muda o sinal
    else:
        partes.pop(0)
        for a in partes:
            reduzida = reduzida + '-' + a

    return reduzida


if __name__ == "__main__":
    # com uma equação assim, funciona
    print(main('y+2x+2=0'))

# Desculpa sor!