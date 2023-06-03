"""
Script para gerar visualização dos resultados do pré-teste e pós-teste com matplotlib e pandas.

Cria dois subplots, um para os resultados do pré-teste, e outro com os resultados do pós-teste.
"""

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import patheffects as path_effects

from compute_tests_statistics import to_frequencies, plot_heatmap


def process():
    pass


def main():
    fig0, axes0 = plt.subplots(nrows=1, ncols=4)
    fig1, axes1 = plt.subplots(nrows=1, ncols=4)

    axes0 = axes0.ravel()
    axes1 = axes1.ravel()

    pre_test = to_frequencies(pd.read_csv(os.path.join('answers', 'raw', 'pre-test.csv'), index_col=(0, 1)))
    post_test = to_frequencies(pd.read_csv(os.path.join('answers', 'raw', 'post-test.csv'), index_col=(0, 1)))

    plot_heatmap('Pré-teste (geral)', pre_test, fig0, axes0[0], 'YlGn')
    plot_heatmap('Pós-teste (geral)', post_test, fig1, axes1[0], 'YlGn')

    turmas = ['eletro', 'info', 'mec']
    for ax0, ax1, turma in zip(axes0[1:], axes1[1:], turmas):
        pre_this_class = pd.read_csv(os.path.join('answers', 'raw', 'pre-test.csv'), index_col=(0, 1))
        post_this_class = pd.read_csv(os.path.join('answers', 'raw', 'post-test.csv'), index_col=(0, 1))

        pre_this_class = pre_this_class.loc[turma, slice(None)]
        post_this_class = post_this_class.loc[turma, slice(None)]

        pre_this_class = round(to_frequencies(pre_this_class) - pre_test, 2)
        post_this_class = round(to_frequencies(post_this_class) - post_test, 2)

        plot_heatmap(f'Pré-teste ({turma})', pre_this_class, fig0, ax0, 'Blues')
        plot_heatmap(f'Pós-teste ({turma})', post_this_class, fig1, ax1, 'Blues')

    fig0.suptitle('Taxa de acertos geral e diferença de cada turma para a média geral')
    fig1.suptitle('Taxa de acertos geral e diferença de cada turma para a média geral')
    plt.tight_layout()
    # plt.savefig(os.path.join('plots', 'heatmap_pre_v2.pdf'), format='pdf')
    plt.show()


if __name__ == '__main__':
    main()
