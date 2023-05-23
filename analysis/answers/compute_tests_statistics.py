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


def generate_general_counts(path):
    df_in = pd.read_csv(path, index_col=(0, 1))

    df_out = pd.DataFrame(data=0., index=df_in.columns, columns=['certo', 'meio', 'errado'], dtype=float)

    for column in df_in.columns:
        counted = df_in[column].value_counts() / df_in[column].count()
        for label in counted.index:
            df_out.loc[column, label] = counted[label]

    df_out.sort_index(inplace=True)
    return df_out


def plot_heatmap(name, df, fig, ax):

    im = ax.imshow(df.values, cmap='YlGn')

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


def add_arrows(fig, axes):
    transFigure = fig.transFigure.inverted()

    points = [
        ((1.25, 0), (0.40, 0)),
        ((1.25, 0), (0.40, 1)),
        ((1.25, 0), (0.40, 2))
    ]

    for point in points:
        p1_trans = transFigure.transform(axes[0].transData.transform(point[0]))
        p2_trans = transFigure.transform(axes[1].transData.transform(point[1]))

        fig.patches.append(
            patches.FancyArrowPatch(
                p1_trans,  # posA
                p2_trans,  # posB
                shrinkA=0,  # so tail is exactly on posA (default shrink is 2)
                shrinkB=0,  # so head is exactly on posB (default shrink is 2)
                transform=fig.transFigure,
                color='black',
                arrowstyle='-|>',  # "normal" arrow
                # connectionstyle=ConnectionStyle("Arc3", rad=0.2),
                connectionstyle=ConnectionStyle(
                    "arc3"
                ),
                # joinstyle='round',
                mutation_scale=30,  # controls arrow head size
                linewidth=3,
            )
        )
    return fig


def main():
    # overall_colors = [to_hex(colormaps.YlGn(x)) for x in np.linspace(0, 1, 10)]
    # colors = [overall_colors[2], overall_colors[4], overall_colors[6]]

    pre_test = generate_general_counts(os.path.join('raw', 'pre-test.csv'))
    post_test = generate_general_counts(os.path.join('raw', 'post-test.csv'))

    fig, axes = plt.subplots(nrows=1, ncols=2)  # , gridspec_kw={'width_ratios': [2, 1]})
    axes = axes.ravel()
    plot_heatmap('Pré-teste', pre_test, fig, axes[0])
    plot_heatmap('Pós-teste', post_test, fig, axes[1])

    fig = add_arrows(fig, axes)

    fig.suptitle('Taxa de acertos para cada questão dos testes, todos os alunos')
    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()


if __name__ == '__main__':
    main()
