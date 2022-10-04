import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import numpy as np
from funcoes import *


def define_layout() -> dash.Dash:
    app = Dash(__name__)

    app.layout = html.Div([
        html.Link(href='https://fonts.googleapis.com/css?family=Rubik Dirt', rel='stylesheet'),
        html.Header([
            html.Div(
                className="app-main",
                children=[
                    html.Div(className="app-main--title")
                ]
            ),
            html.Div([
                html.Nav(className="page__menu page__custom-settings menu"),
                html.Ul([
                    # INSERINDO O MENU HORIZONTAL SUPERIOR
                    html.Li(className="group_menu"),
                    html.A(["Equação de uma reta"], href="main.py#Reta", className="menu__link r-link text-underlined"),
                    html.A(["Equação de uma Circuferência"], href="main.py#Circuferencia",
                           className="menu__link r-link text-underlined"),
                    html.A(["Gráfico"], href="main.py#Gráfico", className="menu__link r-link text-underlined"),
                ], className="menu"),
            ], className="page"),
            html.Div([
                # DIV PARA O TITULO COMO CONTAINER PARA ESTILIZAR MELHOR
                html.Section(),
            ], className="container"),
        ]),
        html.Br(),
        html.Br(),
        # RETA:
        html.P(["EQUAÇÃO DE UMA RETA"], className="name_reta", id="Reta"),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div([
            html.Label(["Digite a equação reduzida de uma reta: "], htmlFor="input_reduzida", className="label_esquerda"),
            dcc.Input(
                id="input_reduzida",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.P(["dica: equação reduzida tem-se no formato: y = mx + n"], className="dica1"),
            html.Br(),
            html.Br(),
            html.Label(["Digite a equação geral de uma reta: "], htmlFor="input_geral", className="label_esquerda"),
            dcc.Input(
                id="input_geral",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.P(["dica: equação geral tem-se no formato: ax + by  + c = 0"], className="dica2"),
            html.Br(),
            html.Br(),
            html.Label(["Digite o coeficiente angular (m): "], htmlFor="input_angular", className="label_esquerda"),
            dcc.Input(
                id="input_angular",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Label(["Digite o coeficiente linear (n): "], htmlFor="input_linear", className="label_esquerda"),
            dcc.Input(
                id="input_linear",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(["Coeficientes: "], className="coeficientes"),
            html.Br(),
            html.Label(["A: "], htmlFor="input_A", className="label_esquerda"),
            dcc.Input(
                id="input_A",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Label(["B: "], htmlFor="input_B", className="label_esquerda"),
            dcc.Input(
                id="input_B",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Label(["C: "], htmlFor="input_C", className="label_esquerda"),
            dcc.Input(
                id="input_C",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.Label(["Ângulo formado pela equação da reta e o eixo X: "], htmlFor="input_angulo", className="label_esquerda"),
            dcc.Input(
                id="input_angulo",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
        ], className="inputs_reta"),
        # CIRCUFERENCIA:
        html.P(["EQUAÇÃO DA CIRCUFERÊNCIA"], className="name_circulo"),
        html.Div([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Label(["Digite uma equação reduzida de uma circuferência: "], htmlFor="label_esquerda", className="label_esquerda"),
            dcc.Input(
                id="input_circunferencia",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.P(["dica: equação reduzida da circuferência tem-se na forma: (x - a)**2 + (y - b)**2 = r**2"],
                   className="dica3"),
            html.Br(),
            html.Br(),
            html.Label(["Centro: (a, b):  "], htmlFor="input_centro", className="label_esquerda"),
            dcc.Input(
                id="input_centro",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.Label(["Raio (r):  "], htmlFor="input_raio", className="label_esquerda"),
            dcc.Input(
                id="input_raio",
                placeholder='',
                type='text',
                value='',
                className='inputs'
            ),
            html.Br(),
            html.Br(),
            html.P('A reta e a circunferência são', className='label_esquerda'),
            dcc.RadioItems(
                id="seletor_intersecao_reta_circunferencia",
                options=["Secantes", "Tangentes", "Disjuntas"],
                value="Secantes",
                className='label_esquerda'
            ),
            # html.Br(),
            html.Label(["entre si e se interceptam no ponto: "], htmlFor="input_interceptam", className="label_esquerda"),
            dcc.Input(
                id="input_interceptam",
                placeholder='',
                type='text',
                value='',
                size='30',
                className='inputs'
            ),
        ], className="circuferencia"),
        html.Br(),
        html.Br(),
        html.Br(),
        # GRAFICO:
        dcc.Loading(dcc.Graph(id="grafico"), type="cube"),
    ], className="body")

    return app


def define_callbacks(app: dash.Dash):
    old_reduzida = 'erro!'
    new_reduzida = 'erro!'

    @app.callback(
        Output("grafico", "figure"),
        Input("input_angular", "value"),
        Input("input_linear", "value"),
        Input("input_circunferencia", "value"),
    )
    def gera_grafico(input_angular, input_linear, input_circunferencia):
        fig = go.Figure(
            layout=go.Layout(
                paper_bgcolor='#F08080',
                plot_bgcolor='#F08080',
                # bordercolor='#709CEE',
            )
        )

        try:
            line_equation = lambda z: input_angular * z + input_linear

            X = np.arange(-10, 10)
            Y = [line_equation(x) for x in X]

            fig = fig.add_scatter(
                x=X,
                y=Y,
                name='reta',
                color='#48D1CC',
                thickness='5px',
                showlegend=True
            )
        except:
            pass

        try:
            xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)

            # Add circles
            fig.add_shape(
                type="circle",
                xref="x", yref="y",
                x0=xc, y0=yc, x1=xc + r, y1=yc + r,
                # line_color="#48D1CC",  # TODO não funciona por algum motivo...
                name='circunferência',
                color='#48D1CC',
                thickness='5px',
                showlegend=True
            )

        except:
            pass

        return fig

    @app.callback(
        Output("input_geral", "value"),
        Input("input_reduzida", "value")
    )
    def atualiza_geral_a_partir_da_reduzida(
            input_reduzida: str
    ) -> str:
        try:
            input_geral = reduzida_para_geral_func(input_reduzida)
        except:
            input_geral = 'erro!'

        return input_geral

    # @app.callback(
    #     Output("input_reduzida", "value"),
    #     Input("input_geral", "value")
    # )
    # def atualiza_reduzida_a_partir_da_geral(
    #         input_geral: str
    # ) -> str:
    #     try:
    #         input_reduzida = geral_para_reduzida_func(input_geral)
    #     except:
    #         input_reduzida = 'erro!'
    #
    #     return input_reduzida

    @app.callback(
        Output("input_angular", "value"),
        Output("input_linear", "value"),
        Input("input_reduzida", "value")
    )
    def atualiza_coefientes_reduzida(
            input_reduzida: str
    ) -> tuple:

        try:
            input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
        except:
            input_angular, input_linear = 'erro!', 'erro!'

        return input_angular, input_linear

    @app.callback(
        Output("input_A", "value"),
        Output("input_B", "value"),
        Output("input_C", "value"),
        Input("input_geral", "value")
    )
    def atualiza_coeficientes_geral(
            input_geral: str
    ) -> tuple:
        try:
            input_A, input_B, input_C = coeficiente_geral_func(input_geral)
        except:
            input_A, input_B, input_C = 'erro!', 'erro!', 'erro!'

        return input_A, input_B, input_C

    @app.callback(
        Output("input_angulo", "value"),
        Input("input_reduzida", "value")
    )
    def atualiza_angulo(
            input_reduzida: str
    ) -> str:
        try:
            input_angulo = angulo_eixo_x_func(input_reduzida)
        except:
            input_angulo = 'erro!'

        return input_angulo

    @app.callback(
        Output("input_centro", "value"),
        Output("input_raio", "value"),
        Input("input_circunferencia", "value")
    )
    def atualiza_centro_e_raio_circunferencia(
            input_circunferencia: str
    ) -> tuple:
        try:
            xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)
        except:
            xc, yc, r = 'erro!', 'erro!', 'erro!'

        return '({0}, {1})'.format(xc, yc), r

    @app.callback(
        Output("seletor_intersecao_reta_circunferencia", "value"),
        Output("input_interceptam", "value"),
        Input("input_reduzida", "value"),
        Input("input_circunferencia", "value")
    )
    def atualiza_posicao_relativa(
            input_reduzida: str, input_circunferencia: str
    ) -> tuple:
        try:
            m, n = coeficientes_reduzida_func(input_reduzida)
            xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)

            relacao, p1, p2 = posicao_relativa_func(xc, yc, r, m, n)

        except:
            relacao, p1, p2 = 'erro!', ('erro!', 'erro!'), ('erro!', 'erro!')

        if p1 == p2:
            return relacao, '({0},{1})'.format(*p1)
        return relacao, '({0},{1}) e ({2}, {3})'.format(*p1, *p2)

    return app


def main():
    app = define_layout()
    app = define_callbacks(app)

    app.run_server(debug=True)


if __name__ == "__main__":
    main()
