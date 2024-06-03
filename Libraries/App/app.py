import streamlit as st
st.title('Here is the title')                         #title
st.header('This is the header ')                      #Header
st.subheader('This is the sub header')                #Subheader



st.markdown("# This is markdown")                     #Markdown
st.markdown("## This is markdown")
st.markdown("### This is markdown")
st.markdown("Markdwon without hastag")


st.success('Data is submitted')                   #Sucess
st.info("Information")                            #Info
st.warning('Warning')
st.error("Error in this data")

st.exception(ZeroDivisionError('Divsion is not possible with 0'))


st.help(ZeroDivisionError)                         #Help

st.write('range(1,10)')
st.write(range(1,10))

st.write("1+2+3")
st.write(1+2+3)

