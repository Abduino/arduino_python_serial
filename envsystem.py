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

    #query = "INSERT INTO smart_agri (soil_moisture,water_level,temperature,humidity,light,pressure ,gas,altitudevar,rain) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
    vsoil_moisture= rows[0]
    vwater_level= 10
    vtemperature=rows[1]
    vhumidity=rows[2]
    vlight=rows[3]
    vpressure=rows[5]
    vgas=rows[4]
    valtitude=rows[6]
    vrain=10
