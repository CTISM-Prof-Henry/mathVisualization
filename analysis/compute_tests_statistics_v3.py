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

def plot_local(pre_questions, equis, pre, post, nrows, ncols, title):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    axes = np.ravel(axes)

    for i, p in enumerate(pre_questions):
        q = equis.loc[equis['pre-test'] == p]['post-test'].values.tolist()

        axes[i].bar(np.arange(2), [pre[p].mean(), post[q].mean(axis=0).mean()])
        axes[i].set_title(f'{p}')
        fig.suptitle(title)
        fig.tight_layout()


def main():
    pre = pd.read_csv(os.path.join('answers', 'raw', 'pre-test_grouped.csv'), index_col=(0, 1))
    post = pd.read_csv(os.path.join('answers', 'raw', 'post-test_grouped.csv'), index_col=(0, 1))
    equis = pd.read_csv(os.path.join('answers', 'raw', 'equivalencies_simplified.csv'))

    turmas = ['eletro', 'info', 'mec']
    pre_questions = pre.columns.unique()

    nrows = len(pre_questions) // 2
    ncols = len(pre_questions) // nrows

    plot_local(pre_questions, equis, pre, post, nrows, ncols, 'todas as turmas')
    plt.show()

    for turma in turmas:
        pre_this_class = pre.loc[turma, slice(None)]
        post_this_class = post.loc[turma, slice(None)]

        plot_local(pre_questions, equis, pre_this_class, post_this_class, nrows, ncols, f'turma {turma}')

    plt.show()


if __name__ == '__main__':
    main()
