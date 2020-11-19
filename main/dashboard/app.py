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


#========================================================================================================================
# BEGIN - Init Dashboard
#========================================================================================================================
external_scripts=[
    {
        'src': 'https://code.jquery.com/jquery-3.5.1.min.js',
        'integrity': 'sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=',
        'crossorigin': 'anonymous'
    }
]

def init_dashboard(server):
    dash_app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/cluster/',
        external_scripts=external_scripts
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
#========================================================================================================================
# END - Init Dashboard
#========================================================================================================================





#========================================================================================================================
# BEGIN - Layout Functions
#========================================================================================================================
def init_layout(dash_app):

    optionsToSet = []
    optionsToSet += [{"label": ageLabels[i][0], "value": f'generateAgeMap{i}'} for i in range(len(ageLabels))]
    optionsToSet += [{"label": eduLabels[i][0], "value": f'generateEduMap{i}'} for i in range(len(eduLabels))]

    dash_app.layout = html.Div(
        id = "root",
        children =[
            html.Div(
                id = "header",
                style= {'color' : '#1f2630', 'text-align': 'center'},
                children = [
                    html.H4(children="A Clustered View of US Voter Demographics", style = {'color': "#03c9a1"}),
                    html.Br(),
                    html.Br(),
                    html.Br()
                ],
            ),
            
            html.Div(
                id = "app-container",
                style = {
                    'color' : '#1f2630',
                    'width': '50%',
                    'height': 'auto',
                    'display': 'block',
                    'float': 'left'
                },
                children=[
                    html.P(
                        id = "dropdown-text",
                        children="Choose a Demographic from the Dropdown",
                        style = {'color': "#03c9a1", 'text-align': 'center'},
                    ),
                    dcc.Dropdown(id="map_select",
                        options=optionsToSet,
                        multi=False,
                        value='generateAgeMap0',
                        style={"backgroundColor": '#0e131a','width':'75%','color': "#03c9a1", 'margin': 'auto'},
                    ),
                    html.Br(),
                    dcc.Graph(
                        id="map",
                        figure={}
                    ),
                ],
            ),

            html.Div(
                id="cluster-container",
                style= {
                    'color' : '#1f2630',
                    'width':'50%',
                    'height': 'auto',
                    'display': 'block',
                    'float': 'right'
                },
                children=[
                    html.P(
                        id="cluster-label",
                        children="Select Data on Right and Choose Graph Style Below",
                        style = {'color': "#03c9a1", 'text-align': 'center'}
                    ),
                    dcc.Dropdown(
                        id="graph-select",
                        options=[
                            {"label": "Line Graph", "value" : "line"},
                            {"label" : "Stacked Bar Chart", "value": "cluster"}],
                        multi=False,
                        value = "line",
                        style={"backgroundColor": '#0e131a','width':'75%','color': "#03c9a1", 'margin': 'auto'},
                    ),
                    html.Br(),
                    dcc.Graph(
                        id="cluster-graph",
                        figure={}
                    ),
                ],
            ),
        ],
    )
#========================================================================================================================
# END - Layout Functions
#========================================================================================================================





#========================================================================================================================
# BEGIN - Callback Functions
#========================================================================================================================
def init_callbacks(dash_app):

    @dash_app.callback(
        Output('map', 'figure'),
        [Input(component_id='map_select',component_property='value')],
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
        [Input(component_id='map',component_property='selectedData'),
        Input("graph-select", "value")],
        [State('cluster-graph', 'figure')]
    )
    def displaySelectedData(selectedData, selectedGraph, figure):
        print("Selected Graph is " + selectedGraph)
        if selectedData is None:
            return dict(
                layout=dict(
                    title="Click-drag on the map to select states",
                    paper_bgcolor="#0e131a",
                    plot_bgcolor="#0e131a",
                    font=dict(color="#03c9a1"),
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
                        paper_bgcolor="#0e131a",
                        plot_bgcolor="#0e131a",
                        font=dict(color="#03c9a1"),
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
    print(df)
    fig = px.bar(df, x = 'State', 
                y = ['19-29', '30-44', '45-64', '65+'], 
                title="Stacked Bar Chart Voter Rates of Selected States",)
    fig.update_layout(
        paper_bgcolor="#0e131a",
        plot_bgcolor="#0e131a",
        font=dict(color="#03c9a1"),
    )
    return fig

def getClusterEduFigure(name):
    # Everett, take charge
    return None

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
            locations = codes,
            z = rates,
            locationmode = 'USA-states',
            colorscale = px.colors.sequential.Viridis,
            colorbar_title = "Voting Percentage",
        ))
        fig.update_layout(
            title_text = ageLabels[index][1],
            geo_scope = 'usa',
            geo_bgcolor = "#0e131a",
            paper_bgcolor = "#0e131a",
            font_color='#03c9a1',
            autosize = True
        )
        #fig.show()
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
            locations = codes,
            z = rates,
            locationmode = 'USA-states',
            colorscale = 'Reds',
            colorbar_title = "Voting Percentage",))
        fig.update_layout(
            title_text = eduLabels[index][1],
            geo_scope = 'usa',
            geo_bgcolor = "#0e131a",
            paper_bgcolor = "#0e131a",
            font_color='#03c9a1',
            autosize = True
        )
        #fig.show()
        return fig
#========================================================================================================================
# END - Callback Functions
#========================================================================================================================