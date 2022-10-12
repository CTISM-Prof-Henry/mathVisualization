from app.funcoes import get_number


def main(a: str, b: str, c: str) -> str:
    a = get_number(a)
    b = get_number(b)
    c = get_number(c)

    reduzida = 'y = {0}x {1:+}'.format(get_number(str(a/b)), get_number(str(c/b))).replace('+', '+ ')

    return reduzida


if __name__ == '__main__':
    print(main('1', '2', '3'))
    print(main('-1/2', '2', '3'))
