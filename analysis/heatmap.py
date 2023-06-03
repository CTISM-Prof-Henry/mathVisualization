"""
Gera um mapa de calor a partir dos dados de movimento do mouse coletados.
"""

import argparse
import os

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix


def main(path):
    all_coords = []
    max_x = -np.inf
    max_y = -np.inf
    for file in os.listdir(path):
        df = pd.read_csv(os.path.join(path, file))
        coordinates = df['mouse_position'].apply(lambda z: z.replace('(', '').replace(')', '').split(',')).tolist()
        coords = []

        for row in coordinates:
            coords += [(int(row[0]), int(row[1]))]

        coords = np.array(coords)

        max_x = max(max_x, coords[:, 0].max() + 1)
        max_y = max(max_y, coords[:, 1].max() + 1)

        all_coords += [coords]

    matrix = csr_matrix((max_x, max_y), dtype=float)  # matriz de zeros
    for coords in all_coords:
        for x, y in coords:
            matrix[x, y] += 1

    matrix = matrix.toarray()
    matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())

    fig, ax = plt.subplots()
    ax.hist2d(matrix[:, 0], matrix[:, 1], bins=(50, 50), cmap=plt.cm.viridis)

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gera um mapa de calor a partir dos dados de movimento do mouse coletados.'
    )

    parser.add_argument(
        '--path', action='store', required=True,
        help='Caminho para arquivo a ser tratado.'
    )

    args = parser.parse_args()
    main(path=args.path)
