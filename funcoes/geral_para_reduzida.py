
def geral_para_reduzida(geral: str) -> str:
    #tratamento
    geral = geral.lower()
    geral_tranformada = geral.split(" ")
    geral = str()
    for numero in geral_tranformada:
        geral += numero

    parteImportante = str(geral.split('=')[0])

    try:
        if 'y' in parteImportante:
            antessede_y = (parteImportante.split("y")[0])
            print(antessede_y)

        else:
            print('não tem y')

    except:
        raise Exception("Errado, não tem y")

    return ...


def main():
    geral = '2y- 3x-3=0'
    print(geral_para_reduzida('-3x+5y+3=0'))
    print(geral_para_reduzida(geral))

    
if __name__ == "__main__":
    main()