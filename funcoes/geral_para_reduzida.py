import math
def main(geral: str) -> str:
    # tratamento
    a = float()
    b = float()
    c = float()

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


if __name__ == "__main__":
    main('x-8y-6=0')
