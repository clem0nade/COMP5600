import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from .vars import *
from . import db
from flask import current_app
# import pyodbc


# ========================================================================================================================
# BEGIN - Init Dashboard
# ========================================================================================================================
def init_dashboard(server):
    dash_app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dash/'
    )

    # Initializing layout after app is loaded
    dash_app.title = "16-CAM"
    init_layout(dash_app)
    with current_app.app_context():
        # Global var for setting graph category. Default is age.
        current_app.categorySelected = "generateAgeMap"

    # Initializing callbacks after app is loaded
    init_callbacks(dash_app)

    return dash_app.server
# ========================================================================================================================
# END - Init Dashboard
# ========================================================================================================================


# ========================================================================================================================
# BEGIN - Layout Functions
# ========================================================================================================================
def init_layout(dash_app):

    optionsToSet = []
    optionsToSet += [{"label": ageLabels[i][0], "value": f'generateAgeMap{i}'}
                     for i in range(len(ageLabels))]
    optionsToSet += [{"label": eduLabels[i][0], "value": f'generateEduMap{i}'}
                     for i in range(len(eduLabels))]

    dash_app.layout = html.Div(
        id="root",
        style={'backgroundColor': '#1f2630'},
        children=[
            html.Div(
                id="header",
                style={'color': '#1f2630'},
                children=[
                    html.H4(children="A Clustered View of US Voter Demographics", style={
                            'color': "#2cfec1"}),
                    html.Br(),
                    html.Br(),
                    html.Br()
                ],
            ),

            html.Div(
                id="app-container",
                style={'color': '#1f2630', 'width': '49%',
                       'display': 'inline-block', 'vertical-align': 'top'},
                children=[
                    html.Div(
                        id="left-column",
                        children=[
                            html.P(
                                id="dropdown-text",
                                children="Choose a Demographic from the Dropdown",
                                style={'color': "#2cfec1"},
                            ),
                            dcc.Dropdown(id="map_select",
                                         options=optionsToSet,
                                         multi=False,
                                         value='generateAgeMap0',
                                         style={"backgroundColor": '#1f2630',
                                                'width': '75%', 'color': "#2cfec1"},
                                         ),
                        ],
                    ),
                    html.Div(
                        id="heatmap-container",
                        style={'color': '#1f2630'},
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
                style={'color': '#1f2630', 'width': '49%',
                       'display': 'inline-block', 'vertical-align': 'top'},
                children=[
                    html.P(id="cluster-label", children="Select Data on Right and Choose Graph Style Below",
                           style={'color': "#2cfec1"}),
                    dcc.Dropdown(
                        id="graph-select",
                        options=[
                            {"label": "Line Graph", "value": "line"},
                            {"label": "Stacked Bar Chart", "value": "cluster"}],
                        multi=False,
                        value="line",
                        style={"backgroundColor": '#1f2630',
                               'width': '75%', 'color': "#2cfec1"},
                    ),
                    dcc.Graph(
                        id="cluster-graph",
                        figure={}
                    ),
                ],
            ),
        ],
    )
# ========================================================================================================================
# END - Layout Functions
# ========================================================================================================================


# ========================================================================================================================
# BEGIN - Callback Functions
# ========================================================================================================================
def init_callbacks(dash_app):

    @dash_app.callback(
        Output('map', 'figure'),
        [Input(component_id='map_select', component_property='value')],
        [State('map', 'figure')]
    )
    def update_Graph(selected, figure):
        index = selected[-1]
        method_name = selected[:-1]
        with current_app.app_context():
            current_app.categorySelected = method_name
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        fig = method(int(index))
        return fig

    @dash_app.callback(
        Output('cluster-graph', 'figure'),
        [Input(component_id='map', component_property='selectedData'),
         Input("graph-select", "value")],
        [State('cluster-graph', 'figure')]
    )
    def displaySelectedData(selectedData, selectedGraph, figure):
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
        if selectedGraph == 'line':
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
        elif selectedGraph == 'cluster':
            categorySelected = ""
            with current_app.app_context():
                categorySelected = current_app.categorySelected

            if categorySelected == "generateAgeMap":
                return getClusterAgeFigure(name)
            elif categorySelected == "generateEduMap":
                return getClusterEduFigure(name)
            else:
                pass


def getClusterAgeFigure(name):
    age1, age2, age3, age4 = db.getAllAgeRates(name)
    data = {}
    data['State'] = name
    data['19-29'] = age1
    data['30-44'] = age2
    data['45-64'] = age3
    data['65+'] = age4
    df = pd.DataFrame(data)
    fig = px.bar(df, x='State',
                 y=['19-29', '30-44', '45-64', '65+'],
                 title="Stacked Bar Chart Voter Rates of Selected States",)
    fig.update_layout(
        paper_bgcolor="#1f2630",
        plot_bgcolor="#1f2630",
        font=dict(color="#2cfec1"),
        margin=dict(t=75, r=50, b=100, l=75),
    )
    return fig


def getClusterEduFigure(name):
    edu1, edu2, edu3, edu4, edu5, edu6, edu7, edu8, edu9 = db.getAllEducation(
        name)
    data = {}
    data['State'] = name
    data['<9th Grade'] = edu1
    data['9th-12th Grade'] = edu2
    data['High School Graduate'] = edu3
    data['Current College Student'] = edu4
    data['Associate`s Degree'] = edu5
    data['Bachelor`s Degree'] = edu6
    data['Graduate Degree'] = edu7
    data['>High School'] = edu8
    data['>Bachelor`s Degree'] = edu9
    df = pd.DataFrame(data)
    fig = px.bar(df, x='State',
                 y=['<9th Grade', '9th-12th Grade', 'High School Graduate', 'Current College Student',
                     'Associate`s Degree', 'Bachelor`s Degree', 'Graduate Degree', '>High School', '>Bachelor`s Degree'],
                 title="Stacked Bar Chart Voter Rates of Selected States",)
    fig.update_layout(
        paper_bgcolor="#1f2630",
        plot_bgcolor="#1f2630",
        font=dict(color="#2cfec1"),
        margin=dict(t=75, r=50, b=100, l=75),
    )
    return fig


def generateAgeMap(index):
    records = db.fetchAge()
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[index+3]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations=codes,
        z=rates,
        locationmode='USA-states',
        colorscale=px.colors.sequential.Viridis,
        colorbar_title="Voting Percentage",
    ))
    fig.update_layout(
        title_text=ageLabels[index][1],
        geo_scope='usa',
        geo_bgcolor="#1f2630",
        paper_bgcolor="#1f2630",
        font_color='#2cfec1',
        autosize=True,
    )
    # fig.show()
    return fig


def generateEduMap(index):
    records = db.fetchEducation()
    names = [0] * 51
    rates = [0] * 51
    codes = [0] * 51
    i = 0
    for row in records:
        codes[i] = row[0]
        names[i] = row[1]
        rates[i] = row[index+3]/row[2]
        i += 1
    fig = go.Figure(data=go.Choropleth(
        locations=codes,
        z=rates,
        locationmode='USA-states',
        colorscale='Reds',
        colorbar_title="Voting Percentage",))
    fig.update_layout(
        title_text=eduLabels[index][1],
        geo_scope='usa',
        geo_bgcolor="#1f2630",
        paper_bgcolor="#1f2630",
        font_color='#2cfec1',
        autosize=True,)
    # fig.show()
    return fig
# ========================================================================================================================
# END - Callback Functions
# ========================================================================================================================
