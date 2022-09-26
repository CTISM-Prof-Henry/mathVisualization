#isso é so um teste

def geral_para_reduzida(geral: str) -> str:
    #tratamento
    geral = geral.lower()
    geral_tranformada = geral.split(" ")
    geral = str()
    for numero in geral_tranformada:
        geral += numero

    return geral


def main():
    geral = 'Y - 3X+3= 0'
    print(geral_para_reduzida('y - 3 X+3=0'))
    print(geral_para_reduzida(geral))
if __name__ == "__main__":
    main()