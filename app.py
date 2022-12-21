import streamlit as st
import pandas as pd
from utils import data_preprocessing,predict
import time
import csv
from PIL import Image


menu = ["About","Predict Your Emotion!","Collect Your Data!","Contact Us"]
choice = st.sidebar.selectbox("Menu",menu)

if choice =="About":
    st.title("Taste Sense Preference Prediction")
    st.markdown(
        '''<div style="text-align: justify;">This study investigated the use of physiological data to assess the emotional state of users 
        after consuming a variety of drinks, as well as the use of neural networks to predict the emotional state of users based on their physiological data </div>''', unsafe_allow_html=True )

elif choice=="Predict Your Emotion!":
    st.subheader("Dataset")
    uploaded_files=st.file_uploader("Upload CSV",type=['csv'],accept_multiple_files=True)
    if st.button("Process"):
        data_preprocessing(uploaded_files[0],uploaded_files[1])
        # if uploaded_files[1].name.lower()=="hr.csv":
        #     st.write(uploaded_files[1].name)
            
        
        # if hrv_file is not None and hrv_file:
        #     input_model=data_preprocessing(hrv_file)
        #     result=predict(input_model)
        #     st.write(result)

elif choice=="Collect Your Data!":

    st.subheader("Collect Your Data!")


    with st.form(key='personal_information',clear_on_submit=True):
        st.write(" #### Consent Form \n\n"
        " I understand that the results will be treated with strictest confidence and no findings which could identify any individual participant will be published.  \n\n "
        "I understand that my participation is anonymous and no individual data will be published from the study.  \n\n "
        "I also understand that my participation is voluntary; that I can choose not to participate in part or all of the project, and that I can withdraw freely at any stage of the project. \n\n "
        "I am willing to participate in the investigation into Taste Preference Prediction conducted at University of Malaya, and for my data to be used in any publications arising from this research.")
        user_name=st.text_input("Name",value="")
        user_age=st.text_input("Age",value="")
        personal_information=[user_name,user_age]
        submit_button_1=st.form_submit_button(label="Submit")

    if submit_button_1:
        st.success("Hello {} you've submitted the your personal information".format(user_name))
    

    st.markdown(" #### Experimental Procedure  \n"
        '''<div style="text-align: justify;">-To begin, participants will seated into a private room that will be free from any outside distractions or \n\n 
stimuli that could influenced the results. \n\n -Participants will be asked to sit up straight and stare straight ahead, with both feet firmly planted on the floor in front of them. \n\n -At the start of the experiment,
participants will be connected to the Empatica device, which will remain connected throughout the period of data collection
participants are also advised to reduce their movement. \n\n
-To begin data analysis, participants will be asked relax themselves for 30 seconds after the counter starts. During data collection,  values were recorded
for BVP, EDA, and Heart Rate. \n\n -These procedures are repeated for each type of beverage. For 
each of the beverage, the participants will be asked to answer the SAM test. \n\n </div>''', unsafe_allow_html=True )
    
    arousal_image=Image.open("arousal_updated.png")



    valence_image=Image.open("valence_updated.png")
    st.markdown('<div style="text-align: justify;"> \n How excited or apathetic the emotion is, ranging from sleepiness or boredom to frantic excitement. </div>', unsafe_allow_html=True )
    st.image(arousal_image,caption="Arousal SAM Test")
    
    st.markdown('<div style="text-align: justify;">How positive or negative the emotion is, ranging from unpleasant feelings to pleasant feelings. \n\n  </div>', unsafe_allow_html=True)
    st.image(valence_image,caption="Valence SAM Test")
    
    
    st.markdown("\n\n\n #### Relax yourself for 1 minute! \n\n")

    col1, col2, col3, col4, col5, col6, col7= st.columns(7)
    if col4.button("Start"):
        with st.empty():
            ts=60
            while ts>=0:
                mins, secs = divmod(ts, 60)
                time_now = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"{time_now}")
                time.sleep(1)
                ts -= 1

    st.markdown("\n\n\n\n\n #### Are you ready! \n\n")
    cola, colb, colc, cold, cole, colf, cog= st.columns(7)
    if cold.button("Ready"):
        with st.empty():
            ts=60
            while ts>=0:
                mins, secs = divmod(ts, 60)
                time_now = '{:02d}:{:02d}'.format(mins, secs)
                st.header(f"{time_now}")
                time.sleep(1)
                ts -= 1

    with st.form(key='experiment_data',clear_on_submit=True):
        st.write(" ###### Question 1 \n"
        "Does this drink give you exciting sensation?")
        st.image(arousal_image)
        arousal=st.radio("",[1,2,3,4,5,6,7,8],horizontal=True)

        st.write("\n\n"
            "\n\n ###### Question 2 \n"
        "Do you like the drink?")
        st.image(valence_image)
        valence=st.radio(" ",[1,2,3,4,5,6,7,8],horizontal=True)
        experiment_data=[arousal,valence]
        submit_button_2=st.form_submit_button(label="Submit")

    if submit_button_2:
        data=personal_information+experiment_data
        with open('Database.csv','a',newline='') as f:
            writer= csv.writer(f)
            writer.writerow(data)
    
        st.success("Hello {} you've submitted the your data".format(user_name))

    

    
