def main(geral: str) -> tuple[float, float, float]:
    coeficientes = list()
    parteImportante = str()
    divisor = "/1"
    coeficienteA = 0
    coeficienteB = 0
    coeficienteC = 0

    if " " in geral:
        tiraEspaço = geral.split(" ")
        geral = str()
        for a in tiraEspaço:
            geral+=a

    partes = geral.split("=")
    if not "0" in partes:
        raise Exception("Equação precisa ser igualada a zero")

    for a in partes:
        if a != "0":
            parteImportante = a
    if "+" in parteImportante[0]:
        parteImportante = parteImportante[1:]

    if "(" in parteImportante and ")" in parteImportante:
        divisor = parteImportante.split(")")[1]
        parteImportante = parteImportante.split(")")[0]
        parteImportante = parteImportante.split("(")[1]
    
    if "-" in parteImportante:
        coeficientes = parteImportante.split("-")
        if "" in coeficientes:
            coeficientes.remove("")
            coeficientes[0] = "-"+coeficientes[0]
        for a in range(len(coeficientes)):
            if a == 0:
                continue
            else:
                coeficientes[a] = "-"+coeficientes[a]
    else:
        coeficientes = parteImportante.split("+")
        try:
            b.remove("")
        except:
            pass

    momentaneo = list()
    for a in coeficientes:
        if "+" in a:
            b = a.split("+")
            try:
                b.remove("")
            except:
                pass
            for c in b:
                momentaneo.append(c)
            coeficientes.remove(a)
    coeficientes += momentaneo
    
    for coeficiente in coeficientes:
        try:
            coeficienteC = float(eval(coeficiente+divisor))
        except:
            if "x" in coeficiente:
                a = coeficiente.split("x")
                try:
                    a.remove("")
                    if a[0] == "":
                        a[0] = '+1'
                    elif a[0] == "-":
                        a[0] = '-1'
                except:
                    pass
                coeficienteA = float(eval(a[0]+divisor))
            elif "y" in coeficiente:
                b = coeficiente.split("y")
                try:
                    b.remove("")
                    if b[0] == "":
                        b[0] = '+1'
                    elif b[0] == "-":
                        b[0] = '-1'
                except:
                    pass
                coeficienteB = float(eval(b[0]+divisor))
            else:
                return Exception("Deve utilizar x e y na equação geral")

    return coeficienteA, coeficienteB, coeficienteC

def testa(relacoes: dict[str : tuple[float,float,float]]) -> bool:
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
        " 3x + 2y + 5 = 0": (3, 2, 5),
        " -3x + 2y + 5 = 0": (-3, 2, 5),
        " +3x - 2y + 5 = 0": (3, -2, 5),
        " +3x + 2y - 5 = 0": (3, 2, -5),
        " +3x - 2y - 5 = 0": (3, -2, -5),
        " -3x + 2y - 5 = 0": (-3, 2, -5),
        " -3x - 2y + 5 = 0": (-3, -2, 5),
        " -3x - 2y - 5 = 0": (-3, -2, -5),

        " -3x - 2y= 0": (-3, -2, 0),
        " -3x - 2= 0": (-3, 0, -2),
        " -3y - 2= 0": (0, -3, -2),
        " +3y= 0": (0, 3, 0),
        " 3x= 0": (3, 0, 0),

        " 3/2x= 0": (1.5, 0, 0),
        " (3x)/2= 0": (1.5, 0, 0),

        " (-3x - 2y - 5) / 2 = 0": (-1.5, -1, -2.5),
        " (-3x - 2y - 5) * 2 = 0": (-6, -4, -10),
    }))
