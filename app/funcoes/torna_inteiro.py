def main(numeros:list, base = 1)->int:
    for numero in numeros:
        if int(numero*base) == numero*base:
            pass
        else:
            base+=1
            base = main(numeros=numeros, base=base)
    return base