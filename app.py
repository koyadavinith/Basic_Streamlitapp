import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import seaborn as sns
import numpy as np

st.title('DashBoard for Iris Data set')

data = pd.read_csv(r'iris.csv')

st.text('Hy, guys My name is Vinith. This is the visualization dashboard to the Iris dataset')

st.dataframe(data)

columns = data.columns[1:5]

option = st.selectbox(
    'Which distribution u want to see ',
    tuple(columns))



st.write('You selected:', option)



st.plotly_chart(px.histogram(data,x = option))

