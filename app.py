import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.express as px
import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sqlite3
from sqlite3 import Error
import pyodbc
from sklearn.cluster import KMeans
import numpy

#Globals
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"
stateCodes = [
"AK",
"AL",
"AR",
"AZ",
"CA",
"CO",
"CT",
"DC",
"DE",
"FL",
"GA",
"HI",
"IA",
"ID",
"IL",
"IN",
"KS",
"KY",
"LA",
"MA",
"MD",
"ME",
"MI",
"MN",
"MS",
"MO",
"MT",
"NC",
"NE",
"NH",
"NJ",
"NM",
"NV",
"NY",
"ND",
"OH",
"OK",
"OR",
"PA",
"RI",
"SC",
"SD",
"TN",
"TX",
"UT",
"VT",
"VA",
"WA",
"WV",
"WI",
"WY"]

def getAllAgeRates(connection, namesIn):
    sql_Select = "select * from Age"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()
    age1 = []
    age2 = []
    age3 = []
    age4 = []

    for row in records:
        for name in namesIn:
            if(name == row[0]):
                age1.append(row[3]/row[2])
                age2.append(row[4]/row[2])
                age3.append(row[5]/row[2])
                age4.append(row[6]/row[2])
       
    
    return age1, age2, age3, age4

def sqlConnect(path):
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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

    data = go.Choropleth(
        locations = codes,
        z = rates,
        locationmode = 'USA-states',
        colorscale = px.colors.sequential.Viridis,
        colorbar_title = "Voting Percentage",)

    layout = go.Layout(
        title="Voter Rates of Ages 18-29",
        font=dict(color="#2cfec1"),
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
    #fig.show()
    #return fig
    return go.Figure(data = data, layout = layout)

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
        colorscale = px.colors.sequential.Viridis,
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "30-44 Voter Rates by State",
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        colorscale = px.colors.sequential.Viridis,
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "45-64 Voter Rates by State",
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
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
        colorscale = px.colors.sequential.Viridis,
        colorbar_title = "Voting Percentage",))
    fig.update_layout(
        title_text = "65+ Voter Rates by State",
        geo_scope = 'usa',
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        autosize = True,)
    #fig.show()
    return fig



DEFAULT_COLORSCALE = [
    "#f2fffb",
    "#bbffeb",
    "#98ffe0",
    "#79ffd6",
    "#6df0c8",
    "#69e7c0",
    "#59dab2",
    "#45d0a5",
    "#31c194",
    "#2bb489",
    "#25a27b",
    "#1e906d",
    "#188463",
    "#157658",
    "#11684d",
    "#10523e",
]
dash_app = dash.Dash(__name__)
app = dash_app.server
#connection = create_connection("Age.db")

#ageRecords = fetchAge(connection)
#eduRecords = fetchEducation(connection)
dash_app.layout = html.Div(
    id = "root",
    style= {'backgroundColor' : '#1f2630'},
    children =[
        html.Div(
            id = "header",
            style= {'color' : '#1f2630'},
            children = [
            html.H4(children="16-CAM Final Project", style = {'color': "#2cfec1"}),
            html.P(
                id = "description",
                children="A Clustered View of US Voter Demographics",
                style = {'color': "#2cfec1"}
            ),
            ],
        ),
        
        html.Div(
            id = "app-container",
            style = {'color' : '#1f2630', 'width':'49%','display': 'inline-block', 'vertical-align': 'top'},
            children=[
                html.Div(
                    id = "left-column",
                    children=[
                        html.P(
                            id = "dropdown-text",
                            children="Choose a Demographic from the Dropdown",
                            style = {'color': "#2cfec1"},
                        ),
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
                            style={"backgroundColor": '#1f2630','width':'75%','color': "#2cfec1"},
                            ),
                    ],
                ),
                html.Div(
                    id="heatmap-container",
                    style= {'color' : '#1f2630'},
                    children=[
                        dcc.Graph(
                            id="map",
                            figure={}
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            id="cluster-container",
            style= {'color' : '#1f2630','width':'49%','display': 'inline-block', 'vertical-align': 'top'},
            children=[
            html.P(id="cluster-label", children="Select Data on Right and Choose Graph Style Below", style = {'color': "#2cfec1"}),
            dcc.Dropdown(
                id="graph-select",
                options=[
                    {"label": "Line Graph", "value" : "line"},
                    {"label" : "Stacked Bar Chart", "value": "cluster"}],
                multi=False,
                value = "line",
                style={"backgroundColor": '#1f2630','width':'75%','color': "#2cfec1"},
            ),
            dcc.Graph(
                id="cluster-graph",
                figure={}
            ),
            ],
        ),
    ],
)

@dash_app.callback(
    Output('map', 'figure'),
    [Input(component_id='map_select',component_property='value')],
    [State('map', 'figure')]
)

def update_Graph(selected, figure):
    connection = sqlConnect("CensusData.db")
    method_name = selected
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    fig = method(connection)
    return fig

@dash_app.callback(
    Output('cluster-graph', 'figure'),
    [Input(component_id='map',component_property='selectedData'),
    Input("graph-select", "value")],
    [State('cluster-graph', 'figure')]
)
def displaySelectedData(selectedData, selectedGraph, figure):
    connection = sqlConnect("CensusData.db")
    print("Selected Graph is " + selectedGraph)
    if selectedData is None:
        return dict(
            data=[dict(x=0, y=0)],
            layout=dict(
                title="Click-drag on the map to select states",
                paper_bgcolor="#1f2630",
                plot_bgcolor="#1f2630",
                font=dict(color="#2cfec1"),
                margin=dict(t=75, r=50, b=100, l=75),
            ),
        )
    data = selectedData["points"]
    name = []
    z = []
    for point in data:
        z.append(point['z'])
        name.append(point['location'])
    print(name)
    print(z)
    if (selectedGraph == 'line'):
        return dict(
                data=[dict(x=name, y=z)],
                layout=dict(
                    title="Voter Rates of Selected States",
                    paper_bgcolor="#1f2630",
                    plot_bgcolor="#1f2630",
                    font=dict(color="#2cfec1"),
                    margin=dict(t=75, r=50, b=100, l=75),
                ),
            )
    elif(selectedGraph == 'cluster'):
        age1, age2, age3, age4 = getAllAgeRates(connection, name)
        data = {}
        data['State'] = name
        data['19-29'] = age1
        data['30-44'] = age2
        data['45-64'] = age3
        data['65+'] = age4
        df = pd.DataFrame(data)
        print(df)
        fig = px.bar(df, x = 'State', 
                    y = ['19-29', '30-44', '45-64', '65+'], 
                    title="Stacked Bar Chart Voter Rates of Selected States",)
        fig.update_layout(
            paper_bgcolor="#1f2630",
            plot_bgcolor="#1f2630",
            font=dict(color="#2cfec1"),
            margin=dict(t=75, r=50, b=100, l=75),
        )
        return fig
        





if __name__ == "__main__":
    dash_app.run_server (host='0.0.0.0', port='80')
