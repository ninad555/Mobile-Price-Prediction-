# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:57:12 2020

@author: kadam
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("knn.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def mobile_price_prediction(battery_power, four_g,	int_memory,	pc,	ram, sc_h, sc_w):
    
    """Let's Predict the PriceRange of mobile 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: battery_power
        in: query
        type: number
        required: true
      - name: four_g
        in: query
        type: number
        required: true
      - name: int_memory
        in: query
        type: number
        required: true
      - name: pc
        in: query
        type: number
        required: true
      - name: ram
        in: query
        type: number
        required: true
      - name: sc_h
        in: query
        type: number
        required: true
      - name: sc_w
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[battery_power, four_g,	int_memory,	pc,	ram, sc_h, sc_w]])
    print(prediction)
    return prediction



def main():
    st.title(" Mobile_Price_Prediction ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Mobile Price Prediction ML app</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    battery_power = st.text_input("Battery Backup","Type Here")
    four_g = st.text_input("Four_G(yes=1 or No =0)","Type Here")
    int_memory = st.text_input("Internal Memory ","Type Here")
    pc = st.text_input("Primary Camera","Type Here")
    ram = st.text_input("Ram (Mhz)","Type Here")
    sc_h = st.text_input("Screen Height","Type Here")
    sc_w= st.text_input("Screen width","Type Here")
    result=""
    if st.button("Predict"):
        result=mobile_price_prediction(battery_power, four_g,	int_memory,	pc,	ram, sc_h, sc_w)
    st.success('The output is {}'.format(result))
    st.text("0 = 10k - 20k")
    st.text("1 = 20k - 30k")
    st.text("2 = 30k - 40k")
    st.text("3= 30k and Above ")

if __name__=='__main__':
    main()
