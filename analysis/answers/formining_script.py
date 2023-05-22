import pandas as pd
import numpy as np
import os


def main():
    pre_test = pd.read_csv(os.path.join('raw', 'pre-test.csv'), index_col=1)
    post_test = pd.read_csv(os.path.join('raw', 'post-test.csv'), index_col=1).drop(columns='turma')
    pre_survey = pd.read_csv(os.path.join('processed', 'pre-survey-processed.csv'), index_col=1).drop(columns='turma')
    post_survey = pd.read_csv(os.path.join('processed', 'post-survey-processed.csv'), index_col=1).drop(columns='turma')

    df = pre_test.join(post_test, how='inner').join(pre_survey, how='inner').join(post_survey, how='inner')

    col_name = 'Eu utilizaria esta ferramenta nos meus estudos de Geometria Analítica:'

    df.loc[:, col_name] = df[col_name].replace(
        to_replace='concordo totalmente', value='usaria'
    ).replace(
        to_replace='concordo', value='usaria'
    ).replace(
        to_replace='neutro', value='não usaria'
    ).replace(
        to_replace='discordo', value='não usaria'
    ).replace(
        to_replace='discordo totalmente', value='não usaria'
    )

    df.to_csv(os.path.join('processed', 'for-mining.csv'), index=False, quotechar='"', encoding='utf-8')


if __name__ == '__main__':
    main()
