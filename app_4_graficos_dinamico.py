# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_auth

dict_usuarios = {
    "Teste": "123456789",
    "Teste2": "qwert1234"
}

#app = Dash(__name__)
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
auth = dash_auth.BasicAuth(app, dict_usuarios)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Base de dados
df = pd.read_excel('Vendas.xlsx')

lista_marcas = list(df['Marca'].unique())
lista_marcas.append('Todas')

# Plotly
#fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
#fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# Seção do Layout
app.layout = html.Div(children=[

    html.H1(children=['Meu Dashboard', dbc.Badge("", className="ms-1")]),

    html.Div(children="Dashboard de vendas feito 100% com python"),

    html.H2(children=['Vendas de cada produto por loja', dbc.Badge("", className="ms-1")], id='Subtitulo'),

    dcc.RadioItems(lista_marcas, value="Todas", id="Selecao_de_marcas"),

    dcc.Graph(id='vendas_por_loja'),

    dcc.Graph(id='distribuicao_vendas'),

    

], style={"text-align": "center"})

# Seção Callback
# O callback é o que liga os botões aos gráficos.

@app.callback(
    Output("Subtitulo", 'children'), # Quem será modificado pelo input
    Output('vendas_por_loja', 'figure'), # Quem será modificado pelo input
    Output('distribuicao_vendas', 'figure'), # Quem será modificado pelo input
    Input('Selecao_de_marcas', 'value') # Quem está modificando ou de onde vamos pegar a informação que está fazendo o filtro
)

def selecionar_marca(marca):
    if marca == 'Todas':
        texto = 'Vendas de cada produto por loja'
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    else:
        df_filtrado = df.loc[df['Marca']==marca, :]
        texto = f'Vendas de cada produto por loja da marca {marca}'
        fig = px.bar(df_filtrado, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df_filtrado, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    
    return texto, fig, fig2 # Deve obedecer a ordem dos outputs cadastrados


if __name__ == '__main__':
    app.run_server(debug=True)