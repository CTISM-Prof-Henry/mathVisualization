import argparse

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main(file):

    df = pd.read_csv(file)
    coordinates = df['mouse_position'].apply(lambda z: z.replace('(', '').replace(')', '').split(',')).tolist()
    coords = []

    for row in coordinates:
        coords += [(int(row[0]), int(row[1]))]

    coords = np.array(coords)

    fig, ax = plt.subplots()
    ax.plot(coords[:, 0], coords[:, 1])
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gera um mapa de calor a partir dos dados de movimento do mouse coletados.'
    )

    parser.add_argument(
        '--file', action='store', required=True,
        help='Caminho para arquivo a ser tratado.'
    )

    args = parser.parse_args()
    main(file=args.file)
