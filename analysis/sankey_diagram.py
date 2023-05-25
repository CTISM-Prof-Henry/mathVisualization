import numpy as np
import pandas as pd
from pySankey import sankey
import os
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import to_hex


def main():
    pd.options.display.max_rows = 8
    df = pd.read_csv(os.path.join('answers', 'raw', 'equivalencies.csv'))

    labels_pre = np.sort(df['pre-test'].unique())
    labels_post = np.sort(df['post-test'].unique())

    colors_pre = {k: to_hex(cm.viridis(i)) for k, i in zip(labels_pre, np.linspace(0, 1, len(labels_pre)))}
    colors_post = {k: to_hex(cm.viridis(i)) for k, i in zip(labels_post, np.linspace(0, 1, len(labels_post)))}

    colors_pre.update(colors_post)
    colors_dict = colors_pre

    sankey.sankey(
        df['pre-test'], df['post-test'], aspect=20, colorDict=colors_dict,
        fontsize=12
    )

    plt.tight_layout()
    plt.savefig(os.path.join('plots', 'sankey_questions.pdf'), format='pdf')

    plt.show()


if __name__ == '__main__':
    main()