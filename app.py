# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:32:37 2020

@author: Jitendra Agarwal

PNAME: BMI WEB APP
"""

import streamlit as st
from PIL import Image

st.title('Welcome to BMI Calculator')

img = Image.open("bmi.jpg")
st.image(img, width = 700)

h_mode = 0

weight = st.number_input("Enter your weight(in kgs)")

status = st.radio('Select your height format: ',('cms','m','feet'))

if(status == 'cms'):
    h_mode = 0
    height = st.number_input("Centimeter")

elif(status == 'm'):
    h_mode = 1
    height = st.number_input("Meters")
    
else:
    h_mode = 2
    height = st.number_input("Feets")
    
if(st.button("Calculate BMI")):
    if(h_mode == 0):
        bmi = weight / ((height/100)**2)
        st.text(bmi)
    elif(h_mode == 1):
        bmi = weight / (height**2)
        st.text(bmi)
    else:
        bmi = weight / ((height/3.28)**2)
        st.text(bmi)
    
    
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
        st.balloons()
        
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")
