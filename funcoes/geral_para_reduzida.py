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

    parteImportante = str(geral.split('=')[0])

    if '+' in parteImportante:
        partes = parteImportante.split("+")

    #### VAI TER QUE ARRUMAR PRA QUANDO TIVER ALGUM -

    for parte in partes:
        try:
            c = float(parte)
        except:
            if "x" in parte:
                if parte == "x":
                    a = 1
                else:
                    coeficiente = parte.split("x")
                    for parten in coeficiente:
                        if len(parten) > 0:
                            a = float(parten)
            elif "y" in parte:
                if parte == "y":
                    b = 1
                else:
                    coeficiente = parte.split("y")
                    for parten in coeficiente:
                        if len(parten) > 0:
                            b = float(parten)
            else:
                raise Exception("equacao inserida errado")

    # TODO precisa retornar uma string, e não uma tupla!!!
    return a, b, c


if __name__ == "__main__":
    main('x+8y+6=0')
