import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("knn.pkl", "rb")

cla = pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def mobile_price_prediction(battery_power, four_g, int_memory, pc, ram, sc_h, sc_w):
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

    prediction = cla.predict([[battery_power, four_g, int_memory, pc, ram, sc_h, sc_w]])
    print(prediction)
    if prediction == 0:
        prediction = "10,000 to 20,000"
    elif prediction == 1:
        prediction = "20,000 to 30,000"
    elif prediction == 2:
        prediction = "30,000 to 40,000"
    elif prediction == 3:
        prediction = "30,000 and Above "

    return prediction


def main():
    st.title(" Mobile_Price_Range_Prediction ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Mobile Price Range Prediction MLapp</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    battery_power = st.text_input("Battery Backup(mAH)")
    four_g = st.text_input("Four_G(yes=1 or No =0)")
    int_memory = st.text_input("Internal Memory (GB)")
    pc = st.text_input("Primary Camera(MP)")
    ram = st.text_input("Ram (Mhz i.e 1GB = 1000 Mhz)")
    sc_h = st.text_input("Screen Height(cm)")
    sc_w = st.text_input("Screen width(cm)")
    result = ""
    if st.button("Predict"):
        result = mobile_price_prediction(battery_power, four_g, int_memory, pc, ram, sc_h, sc_w)
        st.success('The Price of your Mobile must range between {}'.format(result))
    if st.button("App info"):
        st.text("This app is built with Streamlit and Knn Algorithm")
        st.text("With Accuracy of 83% and Mean square Error of 17%")
    if st.button("About"):
        add_link = "[Github link](https://github.com/ninad555/)"
        linkedin = "[Linked in](https://www.linkedin.com/in/ninad-kadam-4439081b0/)"
        st.markdown(add_link)
        st.markdown(linkedin)

if __name__ == '__main__':
    main()
