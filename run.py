import os
from dash import Dash
import dash_bootstrap_components as dbc

from app.callbacks import define_callbacks
from app.layout import define_layout


def main():
    app = Dash(
        __name__,
        assets_folder=os.path.join(os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1]), 'app', 'assets'),
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,  # botões bootstrap
            'https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css'  # sidebar
        ],
        external_scripts=[
            'https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js',  # fileSaver JS
            'https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js'  # Boostrap
        ]
    )

    app = define_layout(app)
    app = define_callbacks(app)

    app.run_server(debug=True)


if __name__ == "__main__":
    main()
