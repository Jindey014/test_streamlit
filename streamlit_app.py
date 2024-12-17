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
  x_raw= df.drop('species', axis = 1)
  x_raw

  st.write('**Y**');
  y_raw = df.species
  y_raw

with st.expander('Data Visualization'):

  st.line_chart(data = df,x= 'bill_length_mm', y='body_mass_g' , color='species')

with st.sidebar:
  st.header('Input Parameters')
# "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"

  island = st.selectbox('Island',('Biscoe','Dream','Torgerson'))
  gender = st.selectbox('Gender',('male','female'))
  bill_length_mm = st.slider('Bill Length (mm)',32.1, 59.6 , 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0,  231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0 , 4207.0)

  #Creating a dataframe for the input parameters
  data = {'island':island,
         'bill_length_mm':bill_length_mm,
         'bill_depth_mm':bill_depth_mm,
         'flipper_length_mm': flipper_length_mm,
         'body_mass_g':body_mass_g,
         'sex':gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df,x_raw], axis = 0)

with st.expander('Input Features'):
  st.write('Input Penguins');
  input_df
  st.write('Combined Penguins Data');
  input_penguins

#Data Preparation
#Encoding the string columns of X
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins, columns = encode,prefix = encode)

#Encoding Y
target_mapper = {'Adelie':0,
                'Gentoo':1,
               'Chinstrap':2 };
def target_encode(val):
  return target_mapper[val]

y= y_raw.apply(target_encode)
y
y_raw



st.write('Encoded Input Penguins')
df_penguins[:1]



  

  

 





