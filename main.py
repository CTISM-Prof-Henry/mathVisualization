import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
from funcoes import *


def define_layout() -> dash.Dash:
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        external_scripts=['https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js']
    )
    # app.scripts.config.serve_locally = False

    # parte interativa
    interactive = html.Div([
            html.P(['Tempo restante: 00:00'], id='countdown_timer'),
            html.P(['Posição do mouse: '], id='mouse_position', hidden=True),
            html.P([''], id='mouse_position_value', hidden=True),
            html.P(['Mouse click?'], id='mouse_click', hidden=True),
            html.P([''], id='mouse_click_value', hidden=True),
            dbc.Button("Finalizar sessão", id="button_finish_session", n_clicks=0),
        ], id="div_interactive"
    )

    # modal com introdução
    start_session_modal = dbc.Modal([
        # html.Span(['x'], id='span_start_session_modal', className='close'),
        dbc.ModalHeader(dbc.ModalTitle("MathVisualization")),
        dbc.ModalBody([
            'Bem-vindo à turma dos caras legais! Aqueles que gostam de estudar matemática. ',
            'Mas se você não gosta de estudá-la, você também pode fazer parte da turma. Basta ter iniciativa! ',
            'Convidamos você a testar esta ferramenta, desenvolvida com muita dedicação, para você fixar ou aprender '
            'sobre o básico da geometria analítica: reconhecer e compreender as características de uma reta por meio '
            'de suas equações.'
        ]),
        dbc.ModalBody([
            'Bom trabalho! ',
            'Ficamos felizes por você querer fazer parte da nossa turma!'
        ]),
        dbc.ModalBody([
            "Aperte o botão abaixo para começar uma sessão do desafio. ",
            "Você terá até 5 minutos para mexer na ferramenta."]),
        dbc.ModalBody([
            "Você pode tentar quantas vezes quiser, mas cada sessão dura no máximo 5 minutos!"
        ]),
        dbc.ModalFooter(
            dbc.Button(
                "Começar!", id="button_start_session", className="ms-auto", n_clicks=0
            )
        ),
    ], id="start_session_modal", is_open=True)

    # modal de finalização
    finish_session_modal = dbc.Modal([
        # html.Span(['x'], id='span_finish_session_modal', className='close'),
        dbc.ModalHeader(dbc.ModalTitle("Sessão finalizada")),
        dbc.ModalBody(['Você concluiu sua sessão! ',
                       'Nós salvamos alguns dados de movimento do mouse para aprimorar essa ferramenta no futuro.']),
        dbc.ModalBody(['Muito obrigado!']),
        dbc.ModalFooter(
            dbc.Button('Fechar', id='close_finish_session_modal', className='ms-auto', n_clicks=0)
        )
    ], id='finish_session_modal', is_open=False)

    app.layout = html.Div([
        start_session_modal,
        finish_session_modal,
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
                    html.A(["Equação da reta"], href="main.py#h1_reta", className="menu__link r-link text-underlined"),
                    html.A(["Equação da Circunferência"], href="main.py#h1_circunferencia",
                           className="menu__link r-link text-underlined"),
                    html.A(["Gráfico"], href="main.py#grafico", className="menu__link r-link text-underlined"),
                ], className="menu"),
            ], className="page"),
            html.Div([
                # DIV PARA O TITULO COMO CONTAINER PARA ESTILIZAR MELHOR
                html.Section(),
            ], className="container"),
        ]),
        interactive,
        html.Br(),
        html.Br(),
        html.Div([
            html.Div([
                html.Div([
                    # RETA:
                    html.H1(["EQUAÇÃO DA RETA"], className="title center", id="h1_reta"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        html.Label(["Digite a equação reduzida de uma reta: "], htmlFor="input_reduzida",
                                   className="label_esquerda"),
                        dcc.Input(
                            id="input_reduzida",
                            placeholder='',
                            type='text',
                            value='',
                            className='inputs'
                        ),
                        html.P(["Dica: equação reduzida tem-se no formato: y = mx + n"], className="dica"),
                        html.Br(),
                        html.Label(["Digite a equação geral de uma reta: "], htmlFor="input_geral",
                                   className="label_esquerda"),
                        dcc.Input(
                            id="input_geral",
                            placeholder='',
                            type='text',
                            value='',
                            className='inputs'
                        ),
                        html.P(["Dica: equação geral tem-se no formato: ax + by  + c = 0"], className="dica"),
                        html.Br(),
                        html.Div([
                            html.Div([
                                html.H2(["Coeficientes: "], className="title coeficientes center"),
                            ], className='center'),
                            html.Div([
                                html.Br(),
                                html.Label(["angular (m): "], htmlFor="input_angular",
                                           className="label_esquerda"),
                                dcc.Input(
                                    id="input_angular",
                                    placeholder='',
                                    type='text',
                                    value='',
                                    className='inputs'
                                ),
                                html.Br(),
                                html.Br(),
                                html.Label(["linear (n): "], htmlFor="input_linear",
                                           className="label_esquerda"),
                                dcc.Input(
                                    id="input_linear",
                                    placeholder='',
                                    type='text',
                                    value='',
                                    className='inputs'
                                ),
                                html.Br(),
                                html.Br(),
                            ], className='body float-child'),
                            html.Div([
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
                            ], className='body float-child'),
                        ], className='body center float-container'),
                        html.Br(),
                        html.Label(["Ângulo formado pela reta e o eixo X: "], htmlFor="input_angulo",
                                   className="label_esquerda"),
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
                ], className='body'),
            ], className='body float-child'),
            html.Div([
                # CIRCUFERENCIA:
                html.H1(["EQUAÇÃO DA CIRCUNFERÊNCIA"], className="title center", id='h1_circunferencia'),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Label(["Digite a equação reduzida da circunferência: "], htmlFor="label_esquerda",
                           className="label_esquerda"),
                dcc.Input(
                    id="input_circunferencia",
                    placeholder='',
                    type='text',
                    value='',
                    className='inputs'
                ),
                html.P(["Dica: equação reduzida da circunferência tem-se na forma: (x - a)**2 + (y - b)**2 = r**2"],
                       className="dica"),
                html.Br(),
                html.Br(),
                html.Label(["Centro (a, b):  "], htmlFor="input_centro", className="label_esquerda"),
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
                html.Label(["entre si e se interceptam no ponto: "], htmlFor="input_interceptam",
                           className="label_esquerda"),
                dcc.Input(
                    id="input_interceptam",
                    placeholder='',
                    type='text',
                    value='',
                    size='30',
                    className='inputs'
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
            ], className='body float-child'),
            # GRAFICO:
            html.Div([
                dcc.Loading(dcc.Graph(id="grafico"), type="cube"),
            ], className='body float-graph'),
        ], className='body float-container'),
    ], className="body")

    return app


def define_callbacks(app: dash.Dash):

    # parte do modal
    @app.callback(
        Output("start_session_modal", "is_open"),
        [Input("button_start_session", "n_clicks"),
         Input("close_finish_session_modal", "n_clicks")],
        [State("start_session_modal", "is_open")],
    )
    def toggle_start_session_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    @app.callback(
        Output("finish_session_modal", "is_open"),
        [Input("button_finish_session", "n_clicks"),
         Input("close_finish_session_modal", "n_clicks")],
        [State("finish_session_modal", "is_open")],
    )
    def toggle_finish_session_modal(n1, n2, is_open: bool):
        if n1 or n2:
            return not is_open

        return is_open

    @app.callback(
        Output("grafico", "figure"),
        Input("input_angular", "value"),
        Input("input_linear", "value"),
        Input("input_circunferencia", "value"),
    )
    def gera_grafico(input_angular, input_linear, input_circunferencia):
        fig = go.Figure(
            layout=go.Layout(
                paper_bgcolor='#48D1CC',
                plot_bgcolor='#48D1CC',
                font={'color': 'white', 'family': 'Montserrat', 'size': 17.5},
                xaxis={'zerolinecolor': '#F08080', 'griddash': 'dot', },
                yaxis={'zerolinecolor': '#F08080', 'griddash': 'dot'},
                height=600,
                margin={'pad': 20}
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
                line={'color': '#c92222'},
                showlegend=True,
            )
        except:
            pass

        try:
            xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)

            fig.add_shape(
                type="circle",
                xref="x", yref="y",
                x0=xc - r, y0=yc - r, x1=xc + r, y1=yc + r,
                name='circunferência',
                line={'color': '#c92222'},
            )

        except Exception as e:
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

    @app.callback(
        Output("input_angular", "value"),
        Output("input_linear", "value"),
        Input("input_reduzida", "value")
    )
    def atualiza_coeficientes_reduzida(
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

    app.run_server(debug=False)


if __name__ == "__main__":
    main()
