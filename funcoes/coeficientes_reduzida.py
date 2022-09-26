def coeficientes_reduzida(equação:str)->"tuple[float, float]":
    """
    Função que dada uma equação de reta reduzida, retorna uma tupla em que, 
    na primeira posição encontra-se o coeficiente angular e na segunda o o coeficiente linear
    """
    coeficienteAngular = float()
    coeficienteLinear = float()

    #Retira espaços:
    juntaTudo = equação.split(" ")
    equação = str()
    for numero in juntaTudo:
        equação += numero
    #Seleciona parte importante da equação
    primeiraParte = str(equação.split("=")[0])
    segundaParte = str(equação.split("=")[1])
    if primeiraParte.lower() != "y":
        raise Exception("equação inserida errado")

    #Para os casos onde temos uma fração que englobe todos os membros da equação:
    if "(" in segundaParte and ")" in segundaParte:
        numerador = segundaParte.split("(")[1].split(")")[0]
        denumerador = segundaParte.split(")")[1]
        #tratamento da virgula no denumerador
        if "," in denumerador:
            denumerador = denumerador.split(",")
            denumerador = denumerador[0]+"."+denumerador[1]
        coeficiente = str()
        partes = list()
        #Divide os coeficientes (linear e angular):
        if "+" in numerador:
            partes = numerador.split("+")
        elif "-" in numerador:
            partes = numerador.split("-")
            if "" in partes:
                partes.remove("")
                partes[0] = "-"+partes[0]
            partes[1] = "-"+partes[1]
        #Pega cada coeficiente:
        for parte in partes:
            #Trata virgula:
            if "," in parte:
                parte = parte.split(",")
                parte = parte[0]+"."+parte[1]
            #Tenta definir como coeficiente linear (se tiver uma letra dará erro e será coeficiente angular):
            try:
                coeficienteLinear = float(eval(parte+denumerador))
            except:
                #Pega cada parte do coeficiente angular
                for numero in parte:
                    #Tenta transformar em numero, a intenção dessa parte é encontrar a letra e retira-la do valor do coeficiente,
                    #então deixamos passar qualquer numero, barra, ponto ou sinal:
                    try:
                        tentaTransformarEmNumero = int(numero)
                        coeficiente+=numero
                    except:
                        if numero == "/" or numero == "." or numero == "-" or numero == "+":
                            coeficiente+=numero
                #Tenta transformar o valor em um float, caso não dê, supõe-se que temos problema na inserção da equação:
                try:
                    coeficienteAngular = float(eval(coeficiente+denumerador))
                except:
                    raise Exception("equação inserida errado")
    #Caso onde não temos uma fração que pega todos os coeficientes:
    else:
        coeficiente = str()
        partes = list()
        #Divide os coeficientes e trata os sinais
        if "+" in segundaParte:
            partes = segundaParte.split("+")
        elif "-" in segundaParte:
            partes = segundaParte.split("-")
            if "" in partes:
                partes.remove("")
                partes[0] = "-"+partes[0]
            partes[1] = "-"+partes[1]
        #Pega cada coeficiente:
        for parte in partes:
             #Trata virgula:
            if "," in parte:
                parte = parte.split(",")
                parte = parte[0]+"."+parte[1]
            try:
                coeficienteLinear = float(eval(parte))
            except:
                for numero in parte:
                    try:
                        coeficiente += str(int(numero))
                    except:
                        if numero == "/" or numero == "." or numero == "-" or numero == "+":
                            coeficiente += numero
                coeficienteAngular = float(eval(coeficiente))

    return coeficienteAngular, coeficienteLinear

if __name__ == "__main__":
    print(coeficientes_reduzida("y = - 3 x - 2 "))
    print(coeficientes_reduzida("y = 3 x - 2 "))
    print(coeficientes_reduzida("y = - 3 x + 2 "))
    print(coeficientes_reduzida("y = 3 x + 2 "))
    print(coeficientes_reduzida("y = 3,2 x + 2.1 "))
    print(coeficientes_reduzida("y = 3.1 x + 2,2 "))
    print(coeficientes_reduzida("y = 3/2 x + 2/2 "))
    print(coeficientes_reduzida("y = - 3.3/3 x - 2.2/2 "))

    print(coeficientes_reduzida("y = ( 3 x - 2) / 2 "))
    print(coeficientes_reduzida("y = ( 3 x - 2) * 2 "))
    print(coeficientes_reduzida("y = ( - 3 x + 2) / 2 "))
    print(coeficientes_reduzida("y = ( - 3 x + 2) * 2 "))


    print(coeficientes_reduzida("y = 2 + 3x"))
    print(coeficientes_reduzida("y = 2 + 3c"))
    print(coeficientes_reduzida("y = 2 + 3z"))