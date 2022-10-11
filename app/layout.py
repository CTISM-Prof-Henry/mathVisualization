import dash
import dash_bootstrap_components as dbc
from dash import html, dcc


def define_layout(app: dash.Dash) -> dash.Dash:
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
        dbc.ModalHeader(dbc.ModalTitle("Sessão finalizada")),
        dbc.ModalBody(['Você concluiu sua sessão! ',
                       'Nós salvamos alguns dados de movimento do mouse para aprimorar essa ferramenta no futuro.']),
        dbc.ModalBody(['Muito obrigado!']),
        dbc.ModalFooter(
            dbc.Button('Fechar', id='close_finish_session_modal', className='ms-auto', n_clicks=0)
        )
    ], id='finish_session_modal', is_open=False)

    header_menus = html.Header([
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
                html.Li(className="group_menu", hidden=True),
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
    ])

    main_content = html.Div([
        # start_session_modal,  # TODO reativar
        # finish_session_modal,  # TODO reativar
        html.Link(href='https://fonts.googleapis.com/css?family=Rubik Dirt', rel='stylesheet'),
        header_menus,
        # div central: contém reta, circunferência e gráfico
        html.Div([
            # div reta, circunferência
            html.Div([
                # div reta
                html.Div([
                    html.Div([
                        html.H1(["EQUAÇÃO DA RETA"], className="title", id="h1_reta"),
                    ], className='center'),
                    # div equações: reduzida, geral
                    html.Div([
                        # div equação reduzida
                        html.Div([
                            # div rótulo
                            html.Div([
                                html.Label(
                                    ["Digite a equação reduzida de uma reta: "],
                                    htmlFor="input_reduzida", className="label-inputs"
                                ),
                                html.P(["Dica: equação reduzida tem-se no formato y = mx + n"], className="dica"),
                            ], className='side-by-side-child'),
                            # div entrada
                            html.Div([
                                dcc.Input(
                                    id="input_reduzida",
                                    placeholder='',
                                    type='text',
                                    value='',
                                    className='inputs'
                                ),
                            ], className='side-by-side-child'),
                        ], className='side-by-side-parent-right'),
                        # div equação geral
                        html.Div([
                            # div rótulo
                            html.Div([
                                html.Label(
                                    ["Digite a equação geral de uma reta: "],
                                    htmlFor="input_geral", className="label-inputs"
                                ),
                                html.P(["Dica: equação geral tem-se no formato ax + by  + c = 0"], className="dica"),
                            ], className='side-by-side-child'),
                            # div entrada
                            html.Div([
                                dcc.Input(
                                    id="input_geral",
                                    placeholder='',
                                    type='text',
                                    value='',
                                    className='inputs'
                                ),
                            ], className='side-by-side-child'),
                        ], className='side-by-side-parent-right'),
                    ], className='center width-reta-equacoes'),  # div equações: reduzida, geral
                    # div coeficientes + título
                    html.Div([
                        html.Div([
                            html.H2(["Coeficientes"], className="title coeficientes center"),
                        ], className='center'),
                        # div coeficientes
                        html.Div([
                            # div coeficiente angular
                            html.Div([
                                html.Div([
                                    html.Label(
                                        ["angular (m): "], htmlFor="input_angular", className="label-inputs"
                                    ),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_angular",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                            # div coeficiente linear
                            html.Div([
                                html.Div([
                                    html.Label(["linear (n): "], htmlFor="input_linear", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_linear",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                            # div coeficiente A
                            html.Div([
                                html.Div([
                                    html.Label(["A: "], htmlFor="input_A", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_A",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                            # div coeficiente B
                            html.Div([
                                html.Div([
                                    html.Label(["B: "], htmlFor="input_B", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_B",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                            # div coeficiente C
                            html.Div([
                                html.Div([
                                    html.Label(["C: "], htmlFor="input_C", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_C",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                        ], className='center width-reta-coeficientes'),  # div coeficientes
                    ]),  # div coeficientes + título
                    # div ângulo reta / eixo x
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label(
                                    ["Ângulo formado pela reta e o eixo X: "],
                                    htmlFor="input_angulo", className="label-inputs"
                                ),
                            ], className='side-by-side-child'),
                            html.Div([
                                dcc.Input(
                                    id="input_angulo",
                                    placeholder='',
                                    type='text',
                                    value='',
                                    className='inputs'
                                ),
                            ], className='side-by-side-child')
                        ], className='side-by-side-parent-right'),  # div ângulo reta / eixo x
                    ], className='center width-reta-angulo'),
                ], className='center side-by-side-child-top'),  # div reta
                # div circunferência
                html.Div([
                    html.Div([
                        html.H1(["EQUAÇÃO DA CIRCUNFERÊNCIA"], className="title", id='h1_circunferencia'),
                    ], className='center'),
                    # div equação circunferência, centro e raio
                    html.Div([
                        # div equação circunferência
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label(
                                        ["Digite a equação reduzida da circunferência: "],
                                        htmlFor='input_circunferencia', className='label-inputs'
                                    ),
                                    html.P(["Dica: equação reduzida da circunferência "
                                            "tem-se na forma (x - a)**2 + (y - b)**2 = r**2"], className="dica"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_circunferencia",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),  # div equação circunferência
                        ], className='center width-circunferencia-equacao'),
                        # div centro e raio da circunferência
                        html.Div([
                            # div centro da circunferência
                            html.Div([
                                html.Div([
                                    html.Label(["Centro (a, b):  "], htmlFor="input_centro", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_centro",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child')
                            ], className='side-by-side-parent-right'),  # div centro
                            html.Div([
                                html.Div([
                                    html.Label(["Raio (r):  "], htmlFor="input_raio", className="label-inputs"),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_raio",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                        ], className='center width-circunferencia-centro-raio'),
                        # div relação reta, circunferência, coordenadas de interseção
                        html.Div([
                            # div relação reta / circunferência
                            html.Div([
                                html.Div([
                                    html.Label(
                                        'A reta e a circunferência são',
                                        htmlFor='seletor_intersecao_reta_circunferencia', className=''
                                    ),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.RadioItems(
                                        id="seletor_intersecao_reta_circunferencia",
                                        options=["Secantes", "Tangentes", "Disjuntas"],
                                        value="Secantes",
                                        labelClassName='selector-label'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                            # div coordenadas interseção
                            html.Div([
                                html.Div([
                                    html.Label(
                                        ["entre si e se interceptam no ponto: "],
                                        htmlFor="input_interceptam", className=''
                                    ),
                                ], className='side-by-side-child'),
                                html.Div([
                                    dcc.Input(
                                        id="input_interceptam",
                                        placeholder='',
                                        type='text',
                                        value='',
                                        size='30',
                                        className='inputs'
                                    ),
                                ], className='side-by-side-child'),
                            ], className='side-by-side-parent-right'),
                        ], className='center width-circunferencia-relacao'),  # div relação reta, circunferência, coordenadas de interseção
                    ], className=''),  # div equação circunferência, centro e raio
                ], className='side-by-side-child-top center'),  # div circunferência
            ], className='side-by-side-parent-center'),  # div reta, circunferência
            # div gráfico
            html.Div([
                dcc.Loading(dcc.Graph(id="grafico"), type="cube"),
            ], className='body graph'),  # div gráfico
        ], className='body'),  # div central: contém reta, circunferência e gráfico
    ], className='body', id='content')  # layout geral

    # parte interativa
    sidebar = html.Nav([
        html.Div([
            html.P(['Tempo restante: 00:00'], id='countdown_timer'),
            html.P(['Posição do mouse: '], id='mouse_position', hidden=True),
            html.P([''], id='mouse_position_value', hidden=True),
            html.P(['Mouse click?'], id='mouse_click', hidden=True),
            html.P([''], id='mouse_click_value', hidden=True),
            dbc.Button("Finalizar sessão", id="button_finish_session", n_clicks=0),
        ], className='')
    ], id='sidebar')

    app.layout = html.Div([
        sidebar,
        main_content
    ], className='wrapper body')

    return app