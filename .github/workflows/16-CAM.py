import sqlite3
from sqlite3 import Error
import plotly.graph_objects as go
import plotly.subplots as sp
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pyodbc

def sqlConnect():
    driver='{ODBC Driver 17 for SQL Server}'
    server='comp5600.database.windows.net'
    database='CensusData'
    username='mec0086'
    password='QuadsMarimbas22'
    connection = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

    return connection

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def fetchAge(connection):
    sql_Select = "select * from Age"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()

    return records

def fetchEducation(connection):
    sql_Select = "select * from Education"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()

    return records

def edu1(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[3]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "<9th Grade Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu2(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[4]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "9th-12th Grade Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu3(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[5]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "High School Graduate Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu4(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[6]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "Current College Student Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu5(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[7]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "Associate's Degree Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu6(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[8]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "Bachelors's Degree Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu7(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[9]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "Graduate Degree Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu8(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[10]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = ">High School Attainment Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def edu9(connection):
    records = fetchEducation(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[11]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Reds',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = ">Bachelor's Degree Attainment Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig



def age1(connection):
    records = fetchAge(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[3]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Blues',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "18-29 Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def age2(connection):
    records = fetchAge(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[4]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Blues',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "30-44 Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def age3(connection):
    records = fetchAge(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[5]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Blues',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "45-64 Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def age4(connection):
    records = fetchAge(connection)
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[6]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = 'Blues',
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "65+ Voter Rates by State",
        geo_scope = 'usa',)
    #fig.show()
    return fig

def main():
    app = dash.Dash(__name__)
    #connection = create_connection("Age.db")
    connection = sqlConnect()
    #ageRecords = fetchAge(connection)
    #eduRecords = fetchEducation(connection)
    app.layout = html.Div([
        html.H1("16-CAM COMP-5600 Final Project", style={'text-align': 'center'}),

        dcc.Dropdown(id="map_select",
                     options=[
                         {"label": "Ages 18 to 29", "value": "age1"},
                         {"label": "Ages 30 to 44", "value": "age2"},
                         {"label": "Ages 45 to 64", "value": "age3"},
                         {"label": "Ages 65+", "value": "age4"},
                         {"label": "<9th Grade Attainment", "value": "edu1"},
                         {"label": "9th to 12th Grade Attainment", "value": "edu2"},
                         {"label": "High School Graduate Attainment", "value": "edu3"},
                         {"label": "Current College Student Attainment", "value": "edu4"},
                         {"label": "Associate's Degree Attainment", "value": "edu5"},
                         {"label": "Bachelor's Degree Attainment", "value": "edu6"},
                         {"label": "Graduate's Degree Attainment", "value": "edu7"},
                         {"label": ">High School Attainment", "value": "edu8"},
                         {"label": ">Bachelor's Degree Attainment", "value": "edu9"}],
                     multi=False,
                     value = "age1",
                     style={'width': "40%"}),
        html.Div(id='output_container', children=[]),
        html.Br(),
        dcc.Graph(id="map", figure={})
        ])

    @app.callback(
        [Output(component_id='output_container', component_property='children'),
         Output(component_id='map', component_property = 'figure')],
         [Input(component_id='map_select',component_property='value')]
         )
    def update_Graph(selected):
        container = "The Graph Chosen was: {}".format(selected)

        method_name = selected
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        fig = method(connection)


        return container, fig
    app.run_server(debug=False)


if __name__ == "__main__":
    main()
