import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.write("Author:@Mahmoud Elgizawy")
st.title("Udemy Course Eda")
df = pd.read_csv("udemy_courses.csv")
st.dataframe(df.head())
st.markdown("---")

col1, col2 =st.columns(2)
with col1:
    st.subheader("how many courses in each subject")
    fig=px.bar(data_frame=df,x=df['subject'])
    fig.update_layout(width=500,height= 500)
    st.plotly_chart(fig )

with col2:
    st.subheader("what is the average price for each subject") 
    dic=dict(df.groupby('subject')['price'].mean())
    fig=px.bar(df,x=dic.keys(),y=dic.values())
    fig.update_xaxes(title='subject')
    fig.update_yaxes(title='average price')
    fig.update_layout(width=500,height= 500)
    st.plotly_chart(fig ) 
st.subheader ("how many paid/unpaid courses for each subject")
option=st.selectbox("select an option ",['is_paid','level'] )
fig=px.bar(df,x=df['subject'],color=option)
st.plotly_chart(fig )