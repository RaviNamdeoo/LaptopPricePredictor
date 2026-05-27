import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('FullPipeline.pkl', 'rb'))
df   = pickle.load(open('dataframe.pkl', 'rb'))

st.title('Laptop Price Predictor')

company       = st.selectbox('Brand', df['Company'].unique())

type_name     = st.selectbox('Type', df['TypeName'].unique())  

ram           = st.selectbox('Ram (in GBs)', [2,4,6,8,12,16,24,32,64])

weight        = st.number_input('Enter Weight (in KGs)', min_value=0.5, max_value=5.0, step=0.1)

touchscreen   = st.selectbox('Touchscreen', ['Yes', 'No'])

ips           = st.selectbox('IPS Display', ['Yes', 'No'])

screen_size   = st.number_input('Enter Screen Size (in Inches)', min_value=10.0, max_value=20.0, step=0.1)

resolution    = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900',

                                                    '3840x2160', '3200x1800', '2880x1800',

                                                    '2560x1600', '2560x1440', '2304x1440'])

cpu           = st.selectbox('CPU Brand', df['Cpu_brand'].unique())

cpu_tier      = st.selectbox('CPU Tier', df['Cpu_tier'].unique())      

cpu_speed     = st.selectbox('CPU Clock Speed', df['Cpu_speed_GHz'].unique())

hdd           = st.selectbox('HDD (in GBs)', [0, 128, 256, 512, 1024, 2048])

ssd           = st.selectbox('SSD (in GBs)', [0, 128, 256, 512, 1024])

flash         = st.selectbox('Flash Storage (in GBs)', df['Flash_Storage_Memory'].unique())

hybrid        = st.selectbox('Hybrid Memory (in GBs)', df['Hybrid_Memory'].unique())

gpu           = st.selectbox('GPU Brand', df['Gpu_brand'].unique())

os            = st.selectbox('Operating System', df['OS'].unique())

dedicated_gpu = st.selectbox('Dedicated GPU', ['Yes', 'No'])


if st.button('Predict Price'):

    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips         = 1 if ips == 'Yes' else 0
    dedicated_gpu = 1 if dedicated_gpu == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi   = (((X_res)**2) + ((Y_res)**2))**0.5 / screen_size

    query = pd.DataFrame([[
        company, type_name, ram, weight,
        ssd, hdd, flash, hybrid,
        touchscreen, ips, ppi,
        cpu, cpu_tier, cpu_speed,
        dedicated_gpu, gpu, os
    ]], columns=[
        'Company', 'TypeName', 'Ram', 'Weight',
        'SSD_Memory', 'HDD_Memory', 'Flash_Storage_Memory', 'Hybrid_Memory',
        'Touchscreen', 'IPS_Display', 'ppi',
        'Cpu_brand', 'Cpu_tier', 'Cpu_speed_GHz',
        'Is_dedicated_Gpu', 'Gpu_brand', 'OS'
    ])

    predicted_price = int(np.exp(pipe.predict(query)[0]))
    st.success(f'Estimated Laptop Price: ₹ {predicted_price:,}')