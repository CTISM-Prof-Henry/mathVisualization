"""
Script para gerar visualização dos resultados do pré-teste e pós-teste com matplotlib e pandas.

Cria 4 subplots, com os resultados do pré- e pós-teste para cada turma em cada um dos subplots.
"""

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import patheffects as path_effects


def to_frequencies(df_in):
    df_out = pd.DataFrame(data=0., index=df_in.columns, columns=['errado', 'meio', 'certo'], dtype=float)

    for column in df_in.columns:
        counted = df_in[column].value_counts() / df_in[column].count()
        for label in counted.index:
            df_out.loc[column, label] = round(counted[label], 2)

    df_out.sort_index(inplace=True)
    return df_out


def plot_heatmap(name, df, fig, ax, cmap='YlGn'):

    im = ax.imshow(df.values, cmap=cmap)

    ax.set_yticks(np.arange(len(df.index)), labels=df.index)
    ax.set_xticks(np.arange(len(df.columns)), df.columns)

    # annotation for cells
    for i, a in enumerate(df.index):
        for j, b in enumerate(df.columns):
            text = ax.text(j, i, df.loc[a, b], ha="center", va="center", color="w")

            text.set_path_effects([
                path_effects.Stroke(linewidth=2, foreground='black'),
                path_effects.Normal()
            ])

    ax.set_title(name)
    fig.tight_layout()


def generate_all_plot(pre_test, post_test, description, name, cmap='YlGn'):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(5.5, 10), gridspec_kw={'width_ratios': [2, 1]})
    axes = axes.ravel()
    plot_heatmap('Pré-teste', pre_test, fig, axes[0], cmap)
    plot_heatmap('Pós-teste', post_test, fig, axes[1], cmap)

    fig.suptitle(description)
    plt.tight_layout()
    plt.savefig(os.path.join('plots', name), format='pdf')


def main():
    pre_test = to_frequencies(pd.read_csv(os.path.join('answers', 'raw', 'pre-test.csv'), index_col=(0, 1)))
    post_test = to_frequencies(pd.read_csv(os.path.join('answers', 'raw', 'post-test.csv'), index_col=(0, 1)))

    generate_all_plot(
        pre_test, post_test, name='heatmap_general.pdf',
        description='Taxa de acertos para cada questão dos testes, todos os alunos'
    )

    turmas = ['eletro', 'info', 'mec']
    for turma in turmas:
        pre_this_class = pd.read_csv(os.path.join('answers', 'raw', 'pre-test.csv'), index_col=(0, 1))
        post_this_class = pd.read_csv(os.path.join('answers', 'raw', 'post-test.csv'), index_col=(0, 1))

        pre_this_class = pre_this_class.loc[turma, slice(None)]
        post_this_class = post_this_class.loc[turma, slice(None)]

        pre_this_class = to_frequencies(pre_this_class)
        post_this_class = to_frequencies(post_this_class)

        generate_all_plot(
            round(pre_this_class - pre_test, 2), round(post_this_class - post_test, 2),
            name='heatmap_%s.pdf' % turma,
            description='Taxa de acertos para cada questão dos testes, turma %s.\n'
                        'Diferença em relação a média de todos os alunos' % turma,
            cmap='Blues'
        )

    plt.show()


if __name__ == '__main__':
    main()
