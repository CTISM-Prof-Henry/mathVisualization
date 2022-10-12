from app.funcoes import get_number


def main(a: str, b: str, c: str) -> str:
    a = get_number(a)
    b = get_number(b)
    c = get_number(c)

    geral = '{0}x {1:+}y {2:+} = 0'.format(a, b, c).replace('+', '+ ')

    return geral


if __name__ == '__main__':
    print(main('1', '2', '3'))
    print(main('-1/2', '2', '3'))
