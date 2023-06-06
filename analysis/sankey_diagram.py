import numpy as np
import pandas as pd
from pySankey import sankey
import os
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import to_hex


def main():
    pd.options.display.max_rows = 8
    df = pd.read_csv(os.path.join('answers', 'raw', 'equivalencies_simplified.csv'))

    labels_pre = [f"Questão {x.split('.')[-1]}" for x in np.sort(df['pre-test'].unique()).tolist()]  # type: list
    labels_post = [f"Questão {x.split('.')[-1]}" for x in np.sort(df['post-test'].unique()).tolist()]  # type: list

    colors_pre = {k: to_hex(cm.viridis(i)) for k, i in zip(labels_pre, np.linspace(0, 1, len(labels_pre)))}
    colors_post = {k: to_hex(cm.viridis(i)) for k, i in zip(labels_post, np.linspace(0, 1, len(labels_post)))}

    colors_pre.update(colors_post)
    colors_dict = colors_pre

    sankey.sankey(
        df['pre-test'].apply(lambda x: f"Questão {x.split('.')[-1]}"),
        df['post-test'].apply(lambda x: f"Questão {x.split('.')[-1]}"),
        aspect=20,
        # leftLabels=labels_post,
        # rightLabels=labels_pre,
        colorDict=colors_dict,
        fontsize=12
    )

    plt.tight_layout()
    plt.savefig(os.path.join('plots', 'sankey_questions.pdf'), format='pdf')

    plt.show()


if __name__ == '__main__':
    main()
