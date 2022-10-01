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
                a.remove("")
                coeficienteA = float(eval(a[0]+divisor))
            elif "y" in coeficiente:
                b = coeficiente.split("y")
                b.remove("")
                coeficienteB = float(eval(b[0]+divisor))
            else:
                return Exception("Deve utilizar x e y na equação geral")

    return coeficienteA, coeficienteB, coeficienteC


if __name__ == "__main__":
    print('segundo teste:', main('(-3x - 8y - 7)/2 = 0'))
