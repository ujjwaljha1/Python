import streamlit as st
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['Line-1','Line-2','Line-3'])
st.subheader('Line Chart')
st.line_chart(chart_data)

st.subheader('Area chart')
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.header("Data visualization with Matplotlin & Seaborn")
st.subheader('Loading the dataFrames')
df=pd.read_csv('iris.csv')
st.dataframe(df)
st.subheader("Distribution Plot with Matplotlib")
fig=plt.figure(figsize=(15,10))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)


st.subheader("Distribution Plot with Seaborn")
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('Multiple header')
#st.subheader("Distribution Plot with Seaborn")
col1,col2=st.columns(2)
with col1:
    col1.header='KDE=False'
  #  col1.write('KDE=False')
    fig1=plt.figure()
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)

with col1:
    col1.header='Hist=False'
  #  col1.write('KDE=False')
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)

st.header("Changing style")
col1,col2=st.columns(2)
with col1:
  #  col1.write('KDE=False')
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    fig=plt.figure()
    sns.distplot(df['petal_length'],kde=False)
    st.pyplot(fig)

with col1:
  #  col1.write('KDE=False')
    sns.set_theme(context='poster',style='darkgrid')
    fig3=plt.figure()
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig3)

st.header('5. Exploring Different Graphs')
st.subheader('5.1 Scatter Plot')
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'species')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'species', y = 'petal_length')
st.pyplot(fig)