from dash import Dash
import dash_bootstrap_components as dbc

from app.callbacks import define_callbacks
from app.layout import define_layout


def main():
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        external_scripts=['https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js']
    )

    app = define_layout(app)
    app = define_callbacks(app)

    app.run_server(debug=True)


if __name__ == "__main__":
    main()
