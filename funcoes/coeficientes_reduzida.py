def coeficientes_reduzida(equação:str):
    coeficienteAngular = float()
    coeficienteLinear = float()
    juntaTudo = equação.split(" ")
    equação = str()
    for numero in juntaTudo:
        equação += numero
    print(equação)
    primeiraParte = str(equação.split("=")[0])
    segundaParte = str(equação.split("=")[1])
    print(primeiraParte)
    if primeiraParte.lower() == "y":
        if "(" in segundaParte:
            numerador = segundaParte.split("(")[1].split(")")[0]
            denumerador = segundaParte.split(")")[1]
            if "/" in denumerador:
                coeficiente = float()
                for numero in numerador:
                    try:
                        coeficiente = float(eval(numero+denumerador))
                    except:
                        if numero != "+":
                            coeficienteAngular = coeficiente
                coeficienteLinear = coeficiente
        else:
            coeficiente = str()
            partes = segundaParte.split("+")
            for parte in partes:
                try:
                    coeficienteLinear = eval(parte)
                except:
                    for numero in parte:
                        try:
                            coeficiente += str(int(numero))
                        except:
                            if numero == "/" or numero == ".":
                                coeficiente += numero
                    coeficienteAngular = eval(coeficiente) 

        return coeficienteAngular, coeficienteLinear
    else:
        return "problema"

if __name__ == "__main__":
    print(coeficientes_reduzida("y=3x+1"))
    print(coeficientes_reduzida(" y = 3 x + 1"))
    print(coeficientes_reduzida("y=3/2x+1"))
    print(coeficientes_reduzida("y = 3 / 2 x + 1 "))
    print(coeficientes_reduzida("y=(3x+1)/2"))
    print(coeficientes_reduzida("y = ( 3 x + 1 ) / 2"))
    print(coeficientes_reduzida("2y=3x+1"))
    print(coeficientes_reduzida("y = ( 3 x + 1 ) * 2")) ## ainda não implementado
