import plotly.graph_objects as go
import plotly.subplots as sp
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sqlite3
from sqlite3 import Error

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

mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"

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
dash_app = dash.Dash()
app = dash_app.server
#connection = create_connection("Age.db")

#ageRecords = fetchAge(connection)
#eduRecords = fetchEducation(connection)
dash_app.layout = html.Div(
    id = "root",
    children =[
        html.Div(
            id = "header",
            children = [
            html.H4(children="16-CAM Final Project"),
            html.P(
                id = "description",
                children="A Clustered View of US Voter Demographics",
            ),
            ],
        ),
        
        html.Div(
            id = "app-container",
            children=[
                html.Div(
                    id = "left-column",
                    children=[
                        html.P(
                            id = "dropdown-text",
                            children="Choose a demographic from the dropdown",
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
                            style={"color": "#7fafdf"}),
                    ],
                ),
                html.Div(
                    id="heatmap-container",
                    children=[
                        dcc.Graph(
                            id="usa-choropleth",
                            figure=dict(
                                layout=dict(
                                    mapbox=dict(
                                        layers=[],
                                        accesstoken=mapbox_access_token,
                                        style=mapbox_style,
                                        center=dict(
                                            lat=38.72490, lon=-95.61446
                                        ),
                                        pitch=0,
                                        zoom=3.5,
                                    ),
                                    autosize=True,
                                )
                            )
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            id="cluster-container",
            children=[
            html.P(id="cluster-label", children="Select Data on Right"),
            dcc.Graph(
                id="cluster-graph",
                figure=dict(
                    data=[dict(x=0,y=0)],
                    layout=dict(
                        paper_bgcolor="#F4F4F8",
                        plot_bgcolor="#F4F4F8",
                        autofill=True,
                        margin=dict(t=75, r=50, b=100, l=50),
                        ),
                    ),
            ),
            ],
        ),
    ],
)

@dash_app.callback(
    Output("usa-choropleth", "figure"),
    [Input(component_id='map_select',component_property='value')],
    [State("usa-chorpleth","figure")]
)

def update_Graph(selected,figure):
    connection = sqlConnect("CensusData.db")
    annotations = [
        dict(
            showarrow=False,
            align="right",
            text="<b>Voting Percentage</b>",
            font=dict(color="#2cfec1"),
            bgcolor="#1f2630",
            x=0.95,
            y=0.95,
        )
    ]
    layout = dict(
        mapbox=dict(
            layers=[],
            accesstoken=mapbox_access_token,
            style=mapbox_style,
            zoom=3.5,
        ),
        hovermode="closest",
        margin=dict(r=0, l=0, t=0, b=0),
        annotations=annotations,
        dragmode="box",
    )
    method_name = selected
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    fig = method(connection)
    fig.layout = layout

    return fig



if __name__ == "__main__":
    dash_app.run_server(host='0.0.0.0', port='80')
