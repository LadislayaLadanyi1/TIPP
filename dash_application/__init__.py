import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output




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
            figure= px.bar(k2_df, x="Months", y="Number of incidents", title="Incidents solved")
        ),  
        
    )

    return dash_app






#GET KPI4

KPI4 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/BL/" #change
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
            figure= px.bar(k2_df, x="Months", y="Number of incidents", title="Incidents backlog per month")
        ),  
        
    )

    return dash_app

#GET KPI5

KPI5 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/av/201801" #change
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
            figure= px.bar(k5_df, x="Critical service", y="Unavailability (min)", color="Months", hover_name="Percentage availability", barmode="group", title="Critical Services availability")
        ),  
        
    )

    return dash_app 



#GET KPI6

KPI6 = "https://bd4d4ihd6rrarpw-ladislayal.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/monav/201801"
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
            figure= px.bar(k6_df, x="Months", y="Monthly average availability", title="Average monthly availability of critical services")
        ),  

    )

    return dash_app

