import os

import pandas as pd
from matplotlib import pyplot as plt


def main():
    pre_test = pd.read_csv(os.path.join('raw', 'pre-test.csv'), index_col=(0, 1))
    post_test = pd.read_csv(os.path.join('raw', 'post-test.csv'), index_col=(0, 1))
    df_in = pre_test.join(post_test, how='inner')

    df_out = pd.DataFrame(data=0., index=df_in.columns, columns=['certo', 'errado', 'meio'], dtype=float)

    general_counts = dict()

    for column in df_in.columns:
        counted = df_in[column].value_counts() / df_in[column].count()
        for label in counted.index:
            df_out.loc[column, label] = counted[label]

    df_out.sort_index(inplace=True)
    print(df_out)


if __name__ == '__main__':
    main()
