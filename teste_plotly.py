import plotly.graph_objects as go
import numpy as np

def main():
    x = np.arange(10)
    y = np.arange(10)

    # documentação da função Scatter: 
    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html

    fig = go.Figure(
        data=go.Scatter(
            x=x, 
            y=y,
            name='função linear',
            showlegend=True
        ),

    )
    fig.show()


if __name__ == '__main__':
    main()


