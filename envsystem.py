#Importing Libraries
import serial
import time
import mysql.connector
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import numpy as np 
import random
import pygal


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=50)
while True:
    data = arduino.readline().decode('ascii')
    rows = data.split(',')


    vsoil_moisture= rows[0]
    vwater_level= 10
    vtemperature=rows[1]
    vhumidity=rows[2]
    vlight=rows[3]
    vpressure=rows[5]
    vgas=rows[4]
    valtitude=rows[6]
    vrain=10

    with placeholder.container():

        st.write("---")
        
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            value = int(float(vsoil_moisture)),
            title = {'text': "Soil Moisture"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 1000]}},
            domain = {'row': 0, 'column': 0}))
        fig.add_trace(go.Indicator(
            value = int(float(vhumidity)),
            title = {'text': "Humidity"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 100]}},
            domain = {'row': 0, 'column': 1}))
        fig.add_trace(go.Indicator(
            value = int(float(vtemperature)),
            title = {'text': "Tempreture"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 100]}},
            domain = {'row': 0, 'column': 2}))
        fig.add_trace(go.Indicator(
            value = int(float(vlight)),
            title = {'text': "Light"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 1000]}},
            domain = {'row': 1, 'column': 0}))
        fig.add_trace(go.Indicator(
            value = int(float(vpressure)),
            title = {'text': "Presure"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 5000]}},
            domain = {'row': 1, 'column': 1}))
        fig.add_trace(go.Indicator(
            value = int(float(vrain)),
            title = {'text': "Rain"},
            delta = {'reference': 50},
            gauge = {'axis': {'range': [None, 100]}},
            domain = {'row': 1, 'column': 2}))
        fig.update_layout(
            title_font_size=40,
            grid = {'rows': 2, 'columns': 3, 'pattern': "independent"},
            template = {'data' : {'indicator': [{  
                'mode' : "number+delta+gauge",
                'delta' : {'reference': 50}}]
                                     }})
        fig.update_yaxes(automargin=True)
        st.plotly_chart(fig)
        time.sleep(5)
    
