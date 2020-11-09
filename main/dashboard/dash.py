import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from . import db
# import pyodbc

#Globals
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"
stateCodes = [
"AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL",
"GA","HI","IA","ID","IL","IN","KS","KY","LA","MA",
"MD","ME","MI","MN","MS","MO","MT","NC","NE","NH",
"NJ","NM","NV","NY","ND","OH","OK","OR","PA","RI",
"SC","SD","TN","TX","UT","VT","VA","WA","WV","WI",
"WY"]

DEFAULT_COLORSCALE = [
    "#f2fffb","#bbffeb","#98ffe0","#79ffd6","#6df0c8",
    "#69e7c0","#59dab2","#45d0a5","#31c194","#2bb489",
    "#1e906d","#188463","#157658","#11684d","#10523e",
]

ageLabels = [
    ("Ages 18 to 29", "Voter Rates of Ages 18-29"),
    ("Ages 30 to 44", "30-44 Voter Rates by State"),
    ("Ages 45 to 64", "45-64 Voter Rates by State"),
    ("Ages 65+", "65+ Voter Rates by State")
]

eduLabels = [
    ("<9th Grade Attainment", "<9th Grade Voter Rates by State"),
    ("9th to 12th Grade Attainment", "9th-12th Grade Voter Rates by State"),
    ("High School Graduate Attainment", "High School Graduate Voter Rates by State"),
    ("Current College Student Attainment", "Current College Student Voter Rates by State"),
    ("Associate's Degree Attainment", "Associate's Degree Voter Rates by State"),
    ("Bachelor's Degree Attainment", "Bachelors's Degree Voter Rates by State"),
    ("Graduate's Degree Attainment", "Graduate Degree Voter Rates by State"),
    (">High School Attainment", ">High School Attainment Voter Rates by State"),
    (">Bachelor's Degree Attainment", ">Bachelor's Degree Attainment Voter Rates by State")   
]

def genAgeMap(index):
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
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        font_color='#2cfec1',
        autosize = True,
    )
    #fig.show()
    return fig

def genEduMap(index):
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
        geo_bgcolor = "#1f2630",
        paper_bgcolor = "#1f2630",
        font_color='#2cfec1',
        autosize = True,)
    #fig.show()
    return fig

optionsToSet = []
optionsToSet += [{"label": ageLabels[i][0], "value": f'genAgeMap{i}'} for i in range(len(ageLabels))]
optionsToSet += [{"label": eduLabels[i][0], "value": f'genEduMap{i}'} for i in range(len(eduLabels))]

