
def geral_para_reduzida(geral: str) -> str:
    #tratamento
    geral = geral.lower()
    geral_tranformada = geral.split(" ")
    geral = str()
    for numero in geral_tranformada:
        geral += numero

    parteImportante = str(geral.split('=')[0])

    if 'y' in parteImportante:
        print('equação correta')
    else:
        print('equação errada')


def main():
    geral = '2X - 3y-3=0'
    print(geral_para_reduzida('-3 X+3=0'))
    print(geral_para_reduzida(geral))


if __name__ == "__main__":
    main()