import streamlit as st
import pandas as pd

st.subheader("Loading the csv file")
df=st.file_uploader("Upload the csv file : ",type=['csv','excel'])

if df is not None:
    st.dataframe(df)

st.subheader('Loading the csv file')
df=pd.read_csv('Products.csv')
if df is not None:
    st.table(df.head())


st.subheader('Dealing with images directly')
st.image('img.png')


st.subheader('Dealing with images uploading')
img=st.file_uploader("Upload the Image : ",type=['png','jpeg'])
if img is not None:
    st.image(img)


st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time = 0)


st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())
    
    