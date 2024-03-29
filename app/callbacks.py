import dash
import numpy as np
from dash import Output, Input, State
from dash.exceptions import PreventUpdate

from app.funcoes import get_number
from app.funcoes.angulo_eixo_x import main as angulo_eixo_x_func
from app.funcoes.calculo_raio_e_centro import main as calculo_raio_e_centro_func
from app.funcoes.coeficientes_geral import main as coeficientes_geral_func
from app.funcoes.coeficientes_geral_para_equacao_geral import main as coeficientes_geral_para_equacao_geral_func
from app.funcoes.coeficientes_geral_para_equacao_reduzida import main as coeficientes_geral_para_equacao_reduzida_func
from app.funcoes.coeficientes_reduzida import main as coeficientes_reduzida_func
from app.funcoes.geral_para_reduzida import main as geral_para_reduzida_func
from app.funcoes.posicao_relativa import main as posicao_relativa_func
from app.funcoes.reduzida_para_geral import main as reduzida_para_geral_func
from app.layout import get_default_graph


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
        Input("input_centro", "value"),
        Input("input_raio", "value"),
        prevent_initial_call=True
    )
    def update_graph(input_angular, input_linear, input_centro, input_raio):
        fig = get_default_graph()

        xc = 0  # centro da circunferência e do gráfico no eixo x
        r = 10  # raio da circunferência

        try:
            xc, yc = eval(input_centro)
            xc = get_number(xc)
            yc = get_number(yc)
            r = get_number(input_raio)

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
            line_equation = lambda z: get_number(input_angular) * z + get_number(input_linear)

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
        Output('input_reduzida', 'value'),
        Output('input_geral', 'value'),
        Output('input_angular', 'value'),
        Output('input_linear', 'value'),
        Output('input_A', 'value'),
        Output('input_B', 'value'),
        Output('input_C', 'value'),
        Output('input_angulo', 'value'),
        [Input('button_submit_reduzida', 'n_clicks'),
         Input('button_submit_geral', 'n_clicks'),
         Input('button_submit_coeficientes_reduzida', 'n_clicks'),
         Input('button_submit_coeficientes_geral', 'n_clicks')],
        [State('button_submit_reduzida', 'n_clicks_timestamp'),
         State('button_submit_geral', 'n_clicks_timestamp'),
         State('button_submit_coeficientes_reduzida', 'n_clicks_timestamp'),
         State('button_submit_coeficientes_geral', 'n_clicks_timestamp'),
         State('input_reduzida', 'value'),
         State('input_geral', 'value'),
         State('input_angular', 'value'),
         State('input_linear', 'value'),
         State('input_A', 'value'),
         State('input_B', 'value'),
         State('input_C', 'value')]
        # State("start_session_modal", "is_open"),
        # State("finish_session_modal", "is_open")
    )
    def on_line_buttons_pressed(
        button_submit_reduzida: str,
        button_submit_geral: str,
        button_submit_coeficientes_reduzida: str,
        button_submit_coeficientes_geral: str,
        button_submit_reduzida_timestamp: str,
        button_submit_geral_timestamp: str,
        button_submit_coeficientes_reduzida_timestamp: str,
        button_submit_coeficientes_geral_timestamp: str,
        input_reduzida: str,
        input_geral: str,
        input_angular: str,
        input_linear: str,
        input_A: str,
        input_B: str,
        input_C: str,
            # start_session_modal: bool, finish_session_modal: bool
    ):
        # if button_submit_reduzida and not start_session_modal and not finish_session_modal:  # TODO reativar

        try:
            dict_buttons = {
                'button_submit_reduzida': button_submit_reduzida_timestamp,
                'button_submit_geral': button_submit_geral_timestamp,
                'button_submit_coeficientes_reduzida': button_submit_coeficientes_reduzida_timestamp,
                'button_submit_coeficientes_geral': button_submit_coeficientes_geral_timestamp
            }
            last_clicked_time = -np.inf
            last_clicked = None
            for k, v in dict_buttons.items():
                try:
                    if v > last_clicked_time:
                        last_clicked_time = v
                        last_clicked = k
                except TypeError:
                    pass
        except:
            raise PreventUpdate()

        if last_clicked == 'button_submit_reduzida':
            try:
                input_geral = reduzida_para_geral_func(input_reduzida)
            except:
                input_geral = 'erro!'

        elif last_clicked == 'button_submit_geral':
            try:
                input_reduzida = geral_para_reduzida_func(input_geral)
            except:
                input_reduzida = 'erro!'

        elif last_clicked == 'button_submit_coeficientes_reduzida':
            try:
                input_reduzida = 'y = {0}x {1:+}'.format(get_number(input_angular), get_number(input_linear))
                input_geral = reduzida_para_geral_func(input_reduzida)
            except:
                input_reduzida = 'erro!'
                input_geral = 'erro!'
        elif last_clicked == 'button_submit_coeficientes_geral':
            try:
                input_geral = coeficientes_geral_para_equacao_geral_func(input_A, input_B, input_C)
                input_reduzida = coeficientes_geral_para_equacao_reduzida_func(input_A, input_B, input_C)
            except:
                input_geral = 'erro!'
                input_reduzida = 'erro!'
        else:
            raise PreventUpdate('')

        if last_clicked != 'button_submit_coeficientes_reduzida':
            try:
                input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
            except:
                input_angular, input_linear = 'erro!', 'erro!'

        if last_clicked != 'button_submit_coeficientes_geral':
            try:
                input_A, input_B, input_C = coeficientes_geral_func(input_geral)
            except:
                input_A, input_B, input_C = 'erro!', 'erro!', 'erro!'

        try:
            input_angulo = angulo_eixo_x_func(input_reduzida)
        except:
            input_angulo = 'erro!'

        return input_reduzida, input_geral, input_angular, input_linear, input_A, input_B, input_C, input_angulo

    @app.callback(
        Output('input_circunferencia', 'value'),
        Output('input_centro', 'value'),
        Output('input_raio', 'value'),
        [Input('button_submit_circunferencia', 'n_clicks'),
         Input('button_submit_centro_raio', 'n_clicks')],
        [State('button_submit_circunferencia', 'n_clicks_timestamp'),
         State('button_submit_centro_raio', 'n_clicks_timestamp'),
         State('input_circunferencia', 'value'),
         State('input_centro', 'value'),
         State('input_raio', 'value')]
    )
    def on_circunference_buttons_pressed(
        button_submit_circunferencia: str,
        button_submit_centro_raio: str,
        button_submit_circunferencia_timestamp: str,
        button_submit_centro_raio_timestamp: str,
        input_circunferencia: str,
        input_centro: str,
        input_raio: str,
    ):
        xc = None
        yc = None
        r = None

        if button_submit_circunferencia or button_submit_centro_raio:
            try:
                dict_buttons = {
                    'button_submit_circunferencia': button_submit_circunferencia_timestamp,
                    'button_submit_centro_raio': button_submit_centro_raio_timestamp
                }
                last_clicked_time = -np.inf
                last_clicked = None
                for k, v in dict_buttons.items():
                    try:
                        if v > last_clicked_time:
                            last_clicked_time = v
                            last_clicked = k
                    except TypeError:
                        pass
            except:
                raise PreventUpdate()
        else:
            raise PreventUpdate()

        if last_clicked == 'button_submit_circunferencia':
            try:
                xc, yc, r = calculo_raio_e_centro_func(input_circunferencia)
            except:
                xc, yc, r = 'erro!', 'erro!', 'erro!'

            input_raio = str(r)
            input_centro = '({0}, {1})'.format(xc, yc)

        elif last_clicked == 'button_submit_centro_raio':
            try:
                xc, yc = eval(input_centro)
                xc = get_number(xc)
                yc = get_number(yc)
                r = get_number(input_raio)

                input_circunferencia = '(x - {0})**2 + (y - {1})**2 = {2}**2'.format(xc, yc, r)
            except:
                input_circunferencia = 'erro!'

        return input_circunferencia, input_centro, input_raio

    @app.callback(
        Output('input_interceptam', 'value'),
        Output('seletor_intersecao_reta_circunferencia', 'value'),
        [Input('button_submit_reduzida', 'n_clicks'),
         Input('button_submit_geral', 'n_clicks'),
         Input('button_submit_coeficientes_reduzida', 'n_clicks'),
         Input('button_submit_coeficientes_geral', 'n_clicks'),
         Input('button_submit_circunferencia', 'n_clicks'),
         Input('button_submit_centro_raio', 'n_clicks'),
         Input('seletor_intersecao_reta_circunferencia', 'value')],  # para caso do usuário tentar selecionar o valor
        [State('input_angular', 'value'),
         State('input_linear', 'value'),
         State('input_centro', 'value'),
         State('input_raio', 'value')]
    )
    def update_intercept_point(
            button_submit_reduzida, button_submit_geral,
            button_submit_coeficientes_reduzida, button_submit_coeficientes_geral,
            button_submit_circunferencia, button_submit_centro_raio,
            seletor_intersecao_reta_circunferencia,
            input_angular, input_linear, input_centro, input_raio
    ):
        try:
            m = get_number(input_angular)
            n = get_number(input_linear)

            xc, yc = eval(input_centro)
            xc = get_number(xc)
            yc = get_number(yc)
            r = get_number(input_raio)

            seletor_intersecao_reta_circunferencia, p1, p2 = posicao_relativa_func(xc, yc, r, m, n)

            if seletor_intersecao_reta_circunferencia == 'Disjuntas':
                input_interceptam = 'não se interceptam'
            elif seletor_intersecao_reta_circunferencia == 'Secantes':
                input_interceptam = '({0}, {1})'.format(*p1)
            else:
                input_interceptam = '({0}, {1}) e ({2}, {3})'.format(*p1, *p2)

        except:
            input_interceptam = 'erro!'
            seletor_intersecao_reta_circunferencia = 'erro!'


        return input_interceptam, seletor_intersecao_reta_circunferencia

    return app
