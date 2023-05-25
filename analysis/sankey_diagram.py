"""
Script para gerar visualização dos resultados do pré-teste e pós-teste com matplotlib e pandas.
"""

import os

import numpy as np
import pandas as pd
from matplotlib import lines
from matplotlib import patches
from matplotlib import pyplot as plt
from matplotlib import patheffects as path_effects
from matplotlib.patches import ConnectionStyle


def add_arrows(fig, axes, equivalencies):
    transFigure = fig.transFigure.inverted()

    xA = 1.25
    xB = 0.40

    translate_a = {k: i for i, k in enumerate(np.sort(equivalencies['pre-test'].unique()))}
    translate_b = {k: i for i, k in enumerate(np.sort(equivalencies['post-test'].unique()))}

    points = []

    for i, line in equivalencies.iterrows():
        points.append((
            (xA, translate_a[line.iloc[0]]), (xB, translate_b[line.iloc[1]])
        ))

    for point in points:
        p1_trans = transFigure.transform(axes[0].transData.transform(point[0]))
        p2_trans = transFigure.transform(axes[1].transData.transform(point[1]))

        # TODO angles: https://members.cbio.mines-paristech.fr/~nvaroquaux/tmp/matplotlib/users/annotations.html

        fig.patches.append(
            patches.FancyArrowPatch(
                p1_trans,  # posA
                p2_trans,  # posB
                shrinkA=0,  # so tail is exactly on posA (default shrink is 2)
                shrinkB=0,  # so head is exactly on posB (default shrink is 2)
                transform=fig.transFigure,
                color='black',
                arrowstyle='fancy',  # "normal" arrow
                # connectionstyle='arc',
                mutation_scale=30,  # controls arrow head size
                linewidth=3,
                alpha=0.5,
            )
        )
    return fig


def main():
    equivalencies = pd.read_csv(os.path.join('raw', 'equivalencies.csv'))

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(5.5, 10), gridspec_kw={'width_ratios': [2, 1]})
    axes = axes.ravel()

    fig = add_arrows(fig, axes, equivalencies)

    fig.suptitle('Taxa de acertos para cada questão dos testes, todos os alunos')
    plt.tight_layout()
    plt.savefig(os.path.join('plots', 'sankey_questions.pdf'), format='pdf')
    plt.show()


if __name__ == '__main__':
    main()
