"""
Script para gerar visualização dos resultados do pré-teste e pós-teste com matplotlib e pandas.

Cria dois subplots, um para os resultados do pré-teste, e outro com os resultados do pós-teste.
"""

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def plot_local(pre_questions, equis, pre, post, axes, count, title):
    x_ticks = np.arange(2)
    for p in pre_questions:
        q = equis.loc[equis['pre-test'] == p]['post-test'].values.tolist()

        if len(q) > 0:
            x_ticklabels = [p, '\n'.join(q)]

            axes[count].bar(x_ticks, [pre[p].mean(), post[q].mean(axis=0).mean()])
            axes[count].set_yticks([0, 1])
            axes[count].set_xticks(x_ticks)
            axes[count].set_xticklabels(x_ticklabels)
            axes[count].set_title(f'{title}, {p}')
            count += 1

    return count


def main():
    pre = pd.read_csv(os.path.join('answers', 'raw', 'pre-test_grouped.csv'), index_col=(0, 1))
    post = pd.read_csv(os.path.join('answers', 'raw', 'post-test_grouped.csv'), index_col=(0, 1))
    equis = pd.read_csv(os.path.join('answers', 'raw', 'equivalencies_simplified.csv'))

    turmas = ['eletro', 'info', 'mec']
    pre_questions = pre.columns.unique().sort_values()

    count = 0
    fig, axes = plt.subplots(nrows=5, ncols=4)
    axes = np.ravel(axes.T)
    count = plot_local(pre_questions, equis, pre, post, axes, count, 'todas as turmas')

    for turma in turmas:
        pre_this_class = pre.loc[turma, slice(None)]
        post_this_class = post.loc[turma, slice(None)]

        count = plot_local(pre_questions, equis, pre_this_class, post_this_class, axes, count, f'turma {turma}')

    fig.suptitle('Taxa de acertos entre questões do pré-questionário e suas equivalências no pós-questionário')
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
