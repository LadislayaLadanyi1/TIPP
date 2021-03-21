import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output
from flask_login import login_required




#GET KPI1

KPI1 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/"
r = requests.get(KPI1)
KPI1JSON = r.json()["items"]



k1_months = []
k1_incidences_numbers = []
k1_priorities = []

for dict in KPI1JSON:
    k1_months.append(dict["month"])
    k1_incidences_numbers.append(dict["incidences_number"])
    k1_priorities.append(dict["priority"])


k1_df = pd.DataFrame({
    "Months": k1_months,
    "Number of incidents": k1_incidences_numbers,
    "Priority": k1_priorities
})


def create_kpi1(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi1", url_base_pathname='/kpi1/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi1-graph',
            figure= px.bar(k1_df, x="Months", y="Number of incidents", color="Priority", barmode="group", title="Total Incidents raised")
        ),  
        
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app




#GET KPI2

KPI2 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi2/incsolved"
r = requests.get(KPI2)
KPI2JSON = r.json()["items"]

k2_months = []
k2_incidences_numbers = []

for dict in KPI2JSON:
    k2_months.append(dict["month"])
    k2_incidences_numbers.append(dict["incidences_number"])

k2_df = pd.DataFrame({
    "Months": k2_months,
    "Number of incidents": k2_incidences_numbers,
    
})

def create_kpi2(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi2", url_base_pathname='/kpi2/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi2-graph',
            figure= px.bar(k2_df, x="Months", y="Number of incidents", title="Total Incidents solved")
        ),  
        
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app



#GET KPI3
KPI3 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/sla/" 
r3 = requests.get(KPI3)
KPI3JSON = r3.json()["items"]


sla= {}
for i in KPI3JSON:
    if i['month'] in sla:
        sla[i['month']].append(i['brbaja'],i['mtbaja'],i['brmedia'],i['mtmedia'],i['bralta'],i['mtalta'],i['brcritica'],i['mtcritica'])
    else: 
        sla[i['month']]= [i["brbaja"],i['mtbaja'],i['brmedia'],i['mtmedia'],i['bralta'],i['mtalta'],i['brcritica'],i['mtcritica']]

def create_kpi3(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi3", url_base_pathname='/kpi3/')    
    
    dash_app.layout = html.Div(children=[
        
        dcc.Dropdown(
            id="month",
            options=[{"label": 'January 2018', "value":'201801'},
                    {"label": 'February 2018', "value":'201802'},
                    {"label": 'March 2018', "value":'201803'}
                    ],
            value="201801"
        ),
        dcc.Graph(
            id='kpi3',
            figure={
                'data':[],         
            }
            
        )  
    ])



    @dash_app.callback(
    Output(component_id="kpi3",component_property="figure"),
    [Input(component_id="month", component_property="value")]
    )
    def update_KPI3(value):
        return {
            "data": [
            {'x': ['BR BAJA','MT BAJA','BR MEDIA','MT MEDIA','BR ALTA','MT ALTA','BT CRITICA','MT CRITICA'], 'y': sla[value], 'type': 'bar', 'name': value},
            
            ]
        }

        for view_function in dash_app.server.view_functions:
            if view_function.startswith(dash_app.config.url_base_pathname):
                dash_app.server.view_functions[view_function] = login_required(
                    dash_app.server.view_functions[view_function]
            )

        return dash_app



#GET KPI4

KPI4 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/BL/" 
r = requests.get(KPI4)
KPI4JSON = r.json()["items"]

k4_months = []
k4_incidences_numbers = []

for dict in KPI4JSON:
    k4_months.append(dict["month"])
    k4_incidences_numbers.append(dict["incidences_number"])

k4_df = pd.DataFrame({
    "Months": k4_months,
    "Number of incidents": k4_incidences_numbers,
    
})


def create_kpi4(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi4", url_base_pathname='/kpi4/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi4-graph',
            figure= px.bar(k4_df, x="Months", y="Number of incidents", barmode="group", title="Monthly Incidents backlog" )
        ),  
        
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

#GET KPI5

KPI5 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/" #change
r = requests.get(KPI5)
KPI5JSON = r.json()["items"]

k5_months = []
k5_service_name = []
k5_unavailabilty_time = []
k5_availability_percentage = []


for dict in KPI5JSON:
    k5_months.append(dict["month"])
    k5_service_name.append(dict["service_name"])
    k5_unavailabilty_time.append(dict["unavailability_time"])
    k5_availability_percentage.append(dict["availability_percentage"])

k5_df = pd.DataFrame({
    "Months": k5_months,
    "Critical service": k5_service_name,
    "Unavailability (min)": k5_unavailabilty_time,
    "Percentage availability": k5_availability_percentage,
    
})
print (k5_df)

def create_kpi5(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi5", url_base_pathname='/kpi5/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi5-graph',
            figure= px.bar(k5_df, x="Months", y="Unavailability (min)", color="Critical service", hover_name="Percentage availability", barmode="group", title="Critical Services unavailability ('%' availability)")
        ),  
        
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app



#GET KPI6

KPI6 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/"
r = requests.get(KPI6)
KPI6JSON = r.json()["items"]

k6_months = []
k6_mothly_av = []

for dict in KPI6JSON:
    k6_months.append(dict["month"])
    k6_mothly_av.append(dict["monthly_av"])


k6_df = pd.DataFrame({
    "Months": k6_months,
    "Monthly average availability": k6_mothly_av,
    
})

def create_kpi6(flask_app):
    dash_app = dash.Dash(server=flask_app, name="kpi6", url_base_pathname='/kpi6/')
    
    dash_app.layout = html.Div(
        dcc.Graph(
            id='kpi6-graph',
            figure= px.bar(k6_df, x="Months", y="Monthly average availability", barmode="group", title="Average monthly availability of critical services")
        ),  

    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

