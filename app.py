import streamlit as st
import pandas as pd
from utils import data_preprocessing,predict
import numpy as np
import webbrowser
import csv

menu = ["About","Predict Your Emotion!","Feedback"]
choice = st.sidebar.selectbox("Menu",menu)

if choice =="About":
    st.title("Taste Sense Preference Prediction")
    st.markdown(
        '''<div style="text-align: justify;">This study investigated the use of physiological data to assess the emotional state of users 
        after consuming a variety of drinks, as well as the use of neural networks to predict the emotional state of users based on their physiological data </div>''', unsafe_allow_html=True )

elif choice=="Predict Your Emotion!":
    st.markdown("\n\n\n\n ## Try Out With Our Sample Data ! \n\n")

    if st.button('Use Sample Data'):
        

        HR = open('HR.csv',"r")
        EDA=open("EDA.csv","r")
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
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScR7C1WY1GFew2Rqx-ykUNjbZZUyuxFxxyOw86aE0LOiUpZ0A/viewform?usp=sf_link'

    if st.button('Submit'):
        webbrowser.open_new_tab(url)

        
        



    

    
