from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np


def define_layout():
    app = Dash(__name__)

    app.layout = html.Div([

        html.Title('Math Visualization'),
        html.Link(href='https://fonts.googleapis.com/css?family=Rubik Dirt', rel='stylesheet'),
        html.Header([
            html.Div(
                className="app-main",
                children=[
                    html.Div(className="app-main--title")
                ]
            ),
         html.Div([
            html.P(["Math Visualization"], className="titulo"),
            html.Section(),
         ], className="container"),
         ]),
         html.Br(),
        html.Br(),
        html.Label("Digite uma equação de reta: ", htmlFor="input_equacao_reta"),
        html.Br(),
        html.Br(),
        dcc.Input(
            id="input_equacao_reta",
            placeholder='',
            type='text',
            value=''
        ),
        html.Br(),
        html.Br(),
        dcc.RadioItems(
            id="seletor_intersecao_reta_circunferencia",
            options=["Secante", "Tangente","Disjuntas"],
            value="Secante",
        ),
        html.Br(),
        dcc.Loading(dcc.Graph(id="grafico"), type="cube"),
    ], className="body")

    return app


def main():
    app = define_layout()

    @app.callback(
        Output("grafico", "figure"), Input("input_equacao_reta", "value")
    )
    def gera_grafico(selection):
        x = np.arange(10)
        y = np.arange(10)

        fig = go.Figure(go.Scatter(
            x=x,
            y=y,
            name='função linear',
            showlegend=True
        ))
        return fig

    app.run_server(debug=True)


if __name__ == "__main__":
    main()
