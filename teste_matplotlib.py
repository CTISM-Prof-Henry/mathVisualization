from matplotlib import pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots()

    x = np.arange(10)
    y = np.arange(10)

    ax.plot(x, y, label='Função linear')

    ax.set_title('Função linear de {0} à {1}'.format(x[0], x[-1]))

    plt.legend(loc='upper right')

    plt.show()


if __name__ == '__main__':
    main()