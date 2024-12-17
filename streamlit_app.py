import streamlit as st
import pandas as pd
import numpy as np

st.title('Machine Learning App')

st.info('This app diffrentiates penguins based on various parameters')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**');
  x = df.drop('species', axis = 1)
  x

  st.write('**Y**');
  y= df.species
  y

with st.expander('Data Visualization'):

  st.line_chart(data = df,x= 'bill_length_mm', y='body_mass_g' , color='species')


# Data Preparations
with st.sidebar:
  st.header('Input Parameters')
# "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"

  island = st.selectbox('Island',('Biscoe','Dream','Torgerson'))
  gender = st.selectbox('Gender',('Male','Female'))
  bill_depth_mm = st.slider('Bill Length (mm)',32.1, 59.6 , 43.9)

 





