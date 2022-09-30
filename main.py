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
                html.A(["Equação de uma Circuferência"], href="main.py#Circuferencia",  className="menu__link r-link text-underlined"),
                html.A(["Grafico"], href="main.py#Grafico",  className="menu__link r-link text-underlined"),
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
        html.P(["EQUAÇÃO DE UMA RETA"], className = "name_reta", id="Reta"),  
         html.Br(),
                html.Br(),
                html.Br(),
        html.Div([
            html.Label(["Digite a equação reduzida de uma reta: "], htmlFor="input_reduzida", className="reduzida"),
                dcc.Input(
                    id="input_reduzida",
                    placeholder='',
                    type='text',
                    value=''
                ),
                   html.P(["dica: equação reduzida tem-se no formato: y = mx + n"], className="dica1"),
            html.Br(),
            html.Br(),
            html.Label(["Digite a equação geral de uma reta: "], htmlFor="input_geral", className="geral"),
                dcc.Input(
                    id="input_geral",
                    placeholder='',
                    type='text',
                    value=''
                ), 
                  html.P(["dica: equação geral tem-se no formato: ax + by  + c = 0"],className="dica2"),
            html.Br(),
            html.Br(),          
            html.Label(["Digite o coeficiente angular (m): "], htmlFor="input_angular", className="angular"),
                dcc.Input(
                    id="input_angular",
                    placeholder='',
                    type='text',
                    value=''
                ), 
                html.Br(),
                html.Br(),
                html.Br(),
            html.Label(["Digite o coeficiente linear (n): "], htmlFor="input_linear", className="linear"),
                dcc.Input(
                    id="input_linear",
                    placeholder='',
                    type='text',
                    value=''
                ),
                html.Br(),
                html.Br(),
                html.Br(),
              html.P(["Coeficientes: "], className = "coeficientes"), 
            html.Br(), 
            html.Label(["A: "], htmlFor="input_A", className="A"),
            
                dcc.Input(
                    id="input_A",
                    placeholder='',
                    type='text',
                    value=''
                ),
                html.Br(),
                html.Br(),
                html.Br(),
            html.Label(["B: "], htmlFor="input_B", className="B"),
            
                dcc.Input(
                    id="input_B",
                    placeholder='',
                    type='text',
                    value=''
                ),
                html.Br(),
                html.Br(),
                html.Br(),
            html.Label(["C: "], htmlFor="input_C", className="C"),
            
                dcc.Input(
                    id="input_C",
                    placeholder='',
                    type='text',
                    value=''
                ),
            html.Br(),
            html.Br(),
            html.Label(["Ângulo formado pela equação da reta e o eixo X: "], htmlFor="input_angulo", className="angulo"),
                dcc.Input(
                    id="input_angulo",
                    placeholder='',
                    type='text',
                    value=''
                ),
            html.Br(),
            html.Br(),
            html.Br(),
        ], className="inputs_reta"),
        # CIRCUFERENCIA:
        html.P(["EQUAÇÃO DA CIRCUFERÊNCIA"], className = "name_circulo"),
        html.Div([
         html.Br(),
            html.Br(),
            html.Br(),
            html.Label(["Digite uma equacao reduzida de uma circuferência: "], htmlFor="input_circuferencia", className="circuferencia"),
                dcc.Input(
                    id="input_circuferencia",
                    placeholder='',
                    type='text',
                    value=''
                ),
                html.P(["dica: equação reduzida da circuferência tem-se na forma: (x - a)**2 + (y - b)**2 = r**2"],className="dica3"),
            html.Br(),
            html.Br(),
            html.Label(["Centro: (a, b):  "], htmlFor="input_centro", className="centro"),
                dcc.Input(
                    id="input_centro",
                    placeholder='',
                    type='text',
                    value=''
                ),
            html.Br(),
            html.Br(),
            html.Label(["Raio (r):  "], htmlFor="input_raio", className="raio"),
                dcc.Input(
                    id="input_raio",
                    placeholder='',
                    type='text',
                    value=''
                ),
            html.Br(),
            html.Br(),
        
        dcc.RadioItems(
            id="seletor_intersecao_reta_circunferencia",
            options=["Secante", "Tangente", "Disjuntas"],
            value="Secante",
        ),
        html.Br(),
         html.Label(["entre si e se interceptam no ponto: "], htmlFor="input_interceptam", className="interceptam"),
                dcc.Input(
                    id="input_interceptam",
                    placeholder='',
                    type='text',
                    value=''
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
    @app.callback(
        Output("grafico", "figure"), Input("input_reduzida", "value")
    )
    def gera_grafico(input_reduzida):
        x = np.arange(10)
        y = np.arange(10)

        fig = go.Figure(go.Scatter(
            x=x,
            y=y,
            name='função linear',
            showlegend=True
        ))
        return fig

    @app.callback(
        Output("input_geral", "value"),
        Output("input_angular", "value"),
        Output("input_linear", "value"),
        Output("input_A", "value"),
        Output("input_B", "value"),
        Output("input_C", "value"),
        Output("input_angulo", "value"),
        Input("input_reduzida", "value")
    )
    def atualiza_inputs_a_partir_da_reduzida(
            input_reduzida: str
    ) -> tuple:
        try:
            input_geral = reduzida_para_geral_func(input_reduzida)
        except:
            input_geral = 'erro!'

        try:
            input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
        except:
            input_angular, input_linear = 'erro!', 'erro!'

        try:
            input_A, input_B, input_C = coeficiente_geral_func(input_geral)
        except:
            input_A, input_B, input_C = 'erro!', 'erro!', 'erro!'

        try:
            input_angulo = angulo_eixo_x_func(input_reduzida)
        except:
            input_angulo = 'erro!'

        return input_geral, input_angular, input_linear, input_A, input_B, input_C, input_angulo

    # @app.callback(
    #     Output("input_reduzida", "value"),
    #     Output("input_angular", "value"),
    #     Output("input_linear", "value"),
    #     Output("input_A", "value"),
    #     Output("input_B", "value"),
    #     Output("input_C", "value"),
    #     Output("input_angulo", "value"),
    #     Input("input_geral", "value")
    # )
    # def atualiza_inputs_a_partir_da_geral(
    #         input_geral: str
    # ) -> tuple:
    #     input_reduzida = geral_para_reduzida_func(input_geral)
    #     input_angular, input_linear = coeficientes_reduzida_func(input_reduzida)
    #     input_A, input_B, input_C = coeficiente_geral_func(input_geral)
    #     input_angulo = angulo_eixo_x_func(input_reduzida)
    #
    #     return input_reduzida, input_angular, input_linear, input_A, input_B, input_C, input_angulo


def main():
    app = define_layout()
    define_callbacks(app)

    app.run_server(debug=True)


if __name__ == "__main__":
    main()
