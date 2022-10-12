import dash
import numpy as np
from dash import Output, Input, State
from dash.exceptions import PreventUpdate
from plotly import graph_objects as go

from app.funcoes.angulo_eixo_x import main as angulo_eixo_x_func
from app.funcoes.calculo_raio_e_centro import main as calculo_raio_e_centro_func
from app.funcoes.coeficientes_geral import main as coeficientes_geral_func
from app.funcoes.coeficientes_reduzida import main as coeficientes_reduzida_func
from app.funcoes.posicao_relativa import main as posicao_relativa_func
from app.funcoes.reduzida_para_geral import main as reduzida_para_geral_func


def define_callbacks(app: dash.Dash):
    # TODO reativar
    # parte do modal
    # @app.callback(
    #     Output("start_session_modal", "is_open"),
    #     [Input("button_start_session", "n_clicks"),
    #      Input("close_finish_session_modal", "n_clicks")],
    #     [State("start_session_modal", "is_open")],
    # )
    # def toggle_start_session_modal(n1, n2, is_open):
    #     if n1 or n2:
    #         return not is_open
    #     return is_open
    #
    # @app.callback(
    #     Output("finish_session_modal", "is_open"),
    #     [Input("button_finish_session", "n_clicks"),
    #      Input("close_finish_session_modal", "n_clicks")],
    #     [State("finish_session_modal", "is_open")],
    # )
    # def toggle_finish_session_modal(n1, n2, is_open: bool):
    #     if n1 or n2:
    #         return not is_open
    #
    #     return is_open

    @app.callback(
        Output("grafico", "figure"),
        Input("input_angular", "value"),
        Input("input_linear", "value"),
        Input("input_circunferencia", "value"),
    )
    def update_graph(input_angular, input_linear, input_circunferencia):
        fig = go.Figure(
            layout=go.Layout(
                paper_bgcolor='#48D1CC',
                plot_bgcolor='#48D1CC',
                font={'color': 'white', 'family': 'Montserrat', 'size': 17.5},
                xaxis={'zerolinecolor': '#F08080', 'griddash': 'dot'},
                yaxis={'zerolinecolor': '#F08080', 'griddash': 'dot'},
            )
        )

        xc = 0  # centro da circunferência e do gráfico no eixo x
        r = 10  # raio da circunferência

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

        try:
            line_equation = lambda z: float(input_angular) * z + float(input_linear)

            X = np.arange(xc - 2 * r, xc + 2 * r)
            Y = [line_equation(x) for x in X]

            fig = fig.add_scatter(
                x=X,
                y=Y,
                name='reta',
                line={'color': '#c92222'},
                showlegend=True
            )
        except:
            pass

        return fig

    @app.callback(
        Output('input_geral', 'value'),
        Output('input_angular', 'value'),
        Output('input_linear', 'value'),
        Output('input_A', 'value'),
        Output('input_B', 'value'),
        Output('input_C', 'value'),
        Output('input_angulo', 'value'),
        [Input('button_submit_reduzida', 'n_clicks')],
        [State('input_reduzida', 'value')]
        # State("start_session_modal", "is_open"),
        # State("finish_session_modal", "is_open")
    )
    def on_button_submit_input_reduzida_pressed(
        button_submit_reduzida: int, input_reduzida: str  # , start_session_modal: bool, finish_session_modal: bool
    ):

        if button_submit_reduzida:
            try:
                input_geral = reduzida_para_geral_func(input_reduzida)
            except:
                input_geral = 'erro!'

            try:
                print('go!')
                input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
            except:
                input_angular, input_linear = 'erro!', 'erro!'

            try:
                input_A, input_B, input_C = coeficientes_geral_func(input_geral)
            except:
                input_A, input_B, input_C = 'erro!', 'erro!', 'erro!'

            try:
                input_angulo = angulo_eixo_x_func(input_reduzida)
            except:
                input_angulo = 'erro!'

            return input_geral, input_angular, input_linear, input_A, input_B, input_C, input_angulo
        else:
            print('not')
            raise PreventUpdate('')


    # @app.callback(
    #     Output("input_geral", "value"),
    #     Input("input_reduzida", "value")
    # )
    # def atualiza_geral_a_partir_da_reduzida(
    #         input_reduzida: str
    # ) -> str:
    #     try:
    #         input_geral = reduzida_para_geral_func(input_reduzida)
    #     except:
    #         input_geral = 'erro!'
    #
    #     return input_geral
    #
    # @app.callback(
    #     Output("input_angular", "value"),
    #     Output("input_linear", "value"),
    #     Input("input_reduzida", "value")
    # )
    # def atualiza_coeficientes_reduzida(
    #         input_reduzida: str
    # ) -> tuple:
    #
    #     try:
    #         input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
    #     except:
    #         input_angular, input_linear = 'erro!', 'erro!'
    #
    #     return input_angular, input_linear
    #
    # @app.callback(
    #     Output("input_A", "value"),
    #     Output("input_B", "value"),
    #     Output("input_C", "value"),
    #     Input("input_geral", "value")
    # )
    # def atualiza_coeficientes_geral(
    #         input_geral: str
    # ) -> tuple:
    #     try:
    #         input_A, input_B, input_C = coeficientes_geral_func(input_geral)
    #     except:
    #         input_A, input_B, input_C = 'erro!', 'erro!', 'erro!'
    #
    #     return input_A, input_B, input_C
    #
    # @app.callback(
    #     Output("input_angulo", "value"),
    #     Input("input_reduzida", "value")
    # )
    # def atualiza_angulo(
    #         input_reduzida: str
    # ) -> str:
    #     try:
    #         input_angulo = angulo_eixo_x_func(input_reduzida)
    #     except:
    #         input_angulo = 'erro!'
    #
    #     return input_angulo
    #
    # @app.callback(
    #     Output("input_centro", "value"),
    #     Output("input_raio", "value"),
    #     Input("input_circunferencia", "value")
    # )
    # def atualiza_centro_e_raio_circunferencia(
    #         input_circunferencia: str
    # ) -> tuple:
    #     try:
    #         xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)
    #     except:
    #         xc, yc, r = 'erro!', 'erro!', 'erro!'
    #
    #     return '({0}, {1})'.format(xc, yc), r
    #
    # @app.callback(
    #     Output("seletor_intersecao_reta_circunferencia", "value"),
    #     Output("input_interceptam", "value"),
    #     Input("input_reduzida", "value"),
    #     Input("input_circunferencia", "value")
    # )
    # def atualiza_posicao_relativa(
    #         input_reduzida: str, input_circunferencia: str
    # ) -> tuple:
    #     try:
    #         m, n = coeficientes_reduzida_func(input_reduzida)
    #         xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)
    #
    #         relacao, p1, p2 = posicao_relativa_func(xc, yc, r, m, n)
    #
    #     except:
    #         relacao, p1, p2 = 'erro!', ('erro!', 'erro!'), ('erro!', 'erro!')
    #
    #     if relacao == 'Disjuntas':
    #         return relacao, 'não se interceptam'
    #     if relacao == 'Secantes':
    #         return relacao, '({0}, {1})'.format(*p1)
    #     return relacao, '({0}, {1}) e ({2}, {3})'.format(*p1, *p2)

    return app
