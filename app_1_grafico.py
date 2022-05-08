# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

#app = Dash(__name__)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Base de dados
df = pd.read_excel('Vendas.xlsx')

# Plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")


# Seção do Layout
app.layout = html.Div(children=[

    html.H1(children=['Meu Dashboard', dbc.Badge("", className="ms-1")]),

    html.Div(children="Dashboard de vendas feito 100% com python"),

    html.H2(children=['Vendas de cada produto por loja', dbc.Badge("", className="ms-1")]),

    dcc.Graph(id='vendas_por_loja', figure=fig)

], style={"text-align": "center"})

# Seção Callback

if __name__ == '__main__':
    app.run_server(debug=True)