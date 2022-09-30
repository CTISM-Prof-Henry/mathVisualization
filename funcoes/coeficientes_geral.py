def main(geral: str) -> tuple[float, float, float]:
    coeficientes = list()
    coeficienteA = 0
    coeficienteB = 0
    coeficienteC = 0

    partes = geral.split("=")
    if "0" not in partes:
        raise Exception("Equação precisa ser igualada a zero")

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
                coeficientes.append(coeficiente)
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
                coeficientes.append(coeficiente)
    else:
        raise Exception("Problema")

    for coeficiente in coeficientes:
        try:
            coeficienteC = float(coeficiente)
        except:
            if "x" in coeficiente:
                divide = str(coeficiente).split("x")
                divide.remove("")
                coeficienteA = float(divide[0])      
            if "y" in coeficiente:
                divide = str(coeficiente).split("y")
                divide.remove("")
                coeficienteB = float(divide[0])                  

    return coeficienteA, coeficienteB, coeficienteC


if __name__ == "__main__":
    print('primeiro teste:', main("-3x-8y-7=0"))
    print('segundo teste:', main('-3x - 8y - 7 = 0'))
