import pandas as pd
from scipy.signal import filtfilt
import scipy
from sklearn import preprocessing
import numpy as np
from scipy import signal
from tensorflow import keras
import streamlit as st

def data_preprocessing(hrv,eda):
    input_data=pd.DataFrame()

    hrv_df=pd.read_csv(hrv)

    column_name_hrv=hrv_df.columns[0]
    hrv_df=hrv_df.rename(columns={column_name_hrv:"Heart Rate Visualization"})

    st.line_chart(hrv_df)

    hrv_df=hrv_df.iloc[-60:]
    hrv_df=hrv_df.values
    hrv_df=hrv_df.reshape(-1, 1)
    min_max_scaler=preprocessing.MinMaxScaler()
    normalized_HRV_value=min_max_scaler.fit_transform(hrv_df)
    
    normalized_phasic_HRV= pd.DataFrame(normalized_HRV_value,columns=["HR"])
    input_data=pd.concat([input_data,normalized_phasic_HRV],axis=1,ignore_index=True)

    eda_df=pd.read_csv(eda)

    column_name_eda=eda_df.columns[0]
    eda_df=eda_df.rename(columns={column_name_eda:"EDA Visualization"})

    st.line_chart(eda_df)

    eda_df=eda_df.iloc[-60:]

    eda_df=eda_df.astype('float64')
    filtered_EDA=scipy.signal.medfilt(eda_df,kernel_size=3)
    phasic_EDA=eda_df-filtered_EDA


    phasic_EDA_value=phasic_EDA.values
    phasic_EDA_value=phasic_EDA_value.reshape(-1, 1)
    min_max_scaler=preprocessing.MinMaxScaler()
    normalized_phasic_EDA_value=min_max_scaler.fit_transform(phasic_EDA_value)

    normalized_phasic_EDA= pd.DataFrame(normalized_phasic_EDA_value,columns=["EDA"])
    input_data=pd.concat([input_data,normalized_phasic_EDA],axis=1,ignore_index=True)
    input_data=input_data.to_numpy()
    input_data=input_data.transpose()
    input_data=np.expand_dims(input_data,0)
    return input_data
    

def predict(input):

    model=keras.models.load_model("./model")
    prediction=model.predict(input)
    classes_pred=np.argmax(prediction,axis=1)

    return classes_pred[0]

