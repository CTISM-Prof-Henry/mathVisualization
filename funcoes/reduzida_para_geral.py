def reduzida_para_geral(red: str) -> str:
    # tratamento
    a = float()
    b = float()
    c = float()
    partes = list()
    red = red.lower()
    red_tranformada = red.split(" ")
    red = str()
    for numero in red_tranformada:
        red += numero
    partes = red.split('=')[:2]
    partes2 = partes[::-1]
    partes2.insert(1, '-')
    partes3 = str(partes2)
    partes4 = partes3+'=0'
    partes5= partes4.replace("'", '')
    partes6= partes5.replace('[', '')
    partes7 = partes6.replace(']', '')
    partes8 = partes7.replace(',', '')
    return partes8.replace(' ','')


def main():
    reduzida= 'y = 3x+7'
    print(reduzida_para_geral(reduzida))
if __name__ == "__main__":
    main()