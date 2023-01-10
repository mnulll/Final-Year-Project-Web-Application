import streamlit as st
import pandas as pd
from utils import data_preprocessing,predict
import numpy as np
from bokeh.models.widgets import Div
import webbrowser
import csv
from PIL import Image

menu = ["About","Predict Your Emotion!","Feedback"]
choice = st.sidebar.selectbox("Menu",menu)

if choice =="About":
    st.title("Taste Sense Preference Prediction")
    st.markdown(
        '''<div style="text-align: justify;">This study investigated the use of physiological data to assess the emotional state of users 
        after consuming a variety of drinks, as well as the use of neural networks to predict the emotional state of users based on their physiological data </div>''', unsafe_allow_html=True )

    for i in range(3):
        st.write(" ")

    st.subheader("Guidance On Using Web Application")

    st.write("1. Click on the Predict Your Emotion")
    guidance1=Image.open("Guidance Images/1.png")
    st.image(guidance1)

    st.write("")
    st.write("2. Click on Use Sample Data if you want to demonstrate the prediction using the sample data ")
    guidance2=Image.open("Guidance Images/2.png")
    st.image(guidance2)

    st.write("")
    st.write("3. The web application will show the data analysis and the class prediction")
    guidance3=Image.open("Guidance Images/3.png")
    st.image(guidance3)

    st.write("")
    st.write("4. If you want to use your data for prediction , upload the files and click Process")
    guidance4=Image.open("Guidance Images/4.png")
    st.image(guidance4)

    st.write("")
    st.write("5. The web application will show the data analysis and the class prediction")
    st.image(guidance3)

    st.write("")
    st.write("6. Click on Feedback to give your feedback about the web application")
    guidance5=Image.open("Guidance Images/5.png")
    st.image(guidance5)

    st.write("")
    st.write("7. Click on Submit Button")
    guidance6=Image.open("Guidance Images/6.png")
    st.image(guidance6)

    st.write("")
    st.write("8.The page of Google Form will be prompted. You are required to answer all of the questions")
    guidance7=Image.open("Guidance Images/7.png")
    st.image(guidance7)




elif choice=="Predict Your Emotion!":
    st.markdown("\n\n\n\n ## Try Out With Our Sample Data ! \n\n")

    if st.button('Use Sample Data'):
        

        HR = open('Sample_HR.csv',"r")
        EDA=open("Sample_EDA.csv","r")
        input=data_preprocessing(HR,EDA)
        
        class_pred=predict(input)

        if class_pred==0:
            st.success("Class 0 - Low Arousal Negative Valence")
        elif class_pred==1:
            st.success("Class 1 - Low Arousal Positive Valence")
        elif class_pred==2:
            st.success("Class 2 - High Arousal Negative Valence")
        else:
            st.success("Class 3 - High Arousal Positive Valence")
    
    st.empty()
    st.markdown("\n\n\n\n ## Use Your Own Data ! \n\n")

    uploaded_files=st.file_uploader("*** Rename your heart rate file as \"hr.csv\" and your eda or gsr file as \"eda.csv\" *** ",type=['csv'],accept_multiple_files=True)
    if st.button("Process"):
        input=np.array([])
        if uploaded_files[0].name.lower()=="hr.csv" and uploaded_files[1].name.lower()=="eda.csv"  :
            input=data_preprocessing(uploaded_files[0],uploaded_files[1])
        else:
            input=data_preprocessing(uploaded_files[1],uploaded_files[0])
        
        class_pred=predict(input)

        if class_pred==0:
            st.success("Class 0 - Low Arousal Negative Valence")
        elif class_pred==1:
            st.success("Class 1 - Low Arousal Positive Valence")
        elif class_pred==2:
            st.success("Class 2 - High Arousal Negative Valence")
        else:
            st.success("Class 3 - High Arousal Positive Valence")
    
        # if hrv_file is not None and hrv_file:
        #     input_model=data_preprocessing(hrv_file)
        #     result=predict(input_model)
        #     st.write(result)


elif choice=="Feedback":
    st.subheader("Submit Your Feedback !")
    # url = 'https://docs.google.com/forms/d/e/1FAIpQLScR7C1WY1GFew2Rqx-ykUNjbZZUyuxFxxyOw86aE0LOiUpZ0A/viewform?usp=sf_link'

    # if st.button('Submit'):
    #     webbrowser.open_new_tab(url)

    if st.button('Submit'):
        js = "window.open('https://docs.google.com/forms/d/e/1FAIpQLScR7C1WY1GFew2Rqx-ykUNjbZZUyuxFxxyOw86aE0LOiUpZ0A/viewform?usp=sf_link')"  # New tab or window
        js = "window.location.href = 'https://docs.google.com/forms/d/e/1FAIpQLScR7C1WY1GFew2Rqx-ykUNjbZZUyuxFxxyOw86aE0LOiUpZ0A/viewform?usp=sf_link'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

        
        



    

    
