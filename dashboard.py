import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.title("Worldwide Billionaires Analysis")
df=pd.read_csv("Billionaire_clean.csv")
st.dataframe(df.head())


df2 = df.sort_values(by = ["NetWorth"], ascending=False).head(10)
fig=px.histogram(df2, x="Name",color="NetWorth",title="Top 10 Billionaires in the world")
st.plotly_chart(fig)

x=df["Source"].value_counts().head().index
y=df["Source"].value_counts().head().values
fig=px.pie(df,names=x,values=y,title="Top 5 Domains to Become a Billionaires",hole=0.3)
st.plotly_chart(fig)

w=df["Industry"].value_counts().head().index
z=df["Industry"].value_counts().head().values
fig=px.pie(df,names=w,values=z,title="Top 5 Industries with Most Number of Billionaires",hole=0.3)
st.plotly_chart(fig)
A=df["Country"].value_counts().head().index
B=df["Country"].value_counts().head().values
fig=px.pie(df,names=A,values=B,title="Top 5 Countries with Most Number of Billionaires",hole=0.3)
st.plotly_chart(fig)
