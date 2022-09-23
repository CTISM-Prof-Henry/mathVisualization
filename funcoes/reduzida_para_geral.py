#isso é so um teste

def reduzida_para_geral(red: str) -> str:
    #tratamento
    red = red.lower()
    red_tranformada = red.split(" ")
    red = str()
    for numero in red_tranformada:
        red += numero

    return red

def separa_elementos():
    reduzida_para_geral()

def main():


if __name__ == "__main__":
    main()