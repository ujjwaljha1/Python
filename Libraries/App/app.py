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

st.code('x=10 \n'
        'for i in range(1,10):\n'                     #For witing code
        '\tprint(i)')


st.checkbox('Male')                                 #Check box
st.checkbox('Female')                               #Checkbox is Multiple always

if(st.checkbox('Adult')):
    st.success("You are adult")
else:
    st.error("You are not adult")

st.radio('Select: ',('Male','Female','Transgender'))                  #Radio is single

radiobutton=st.radio('Select your gender: ',('Male','Female'))   
if(radiobutton=='Male'):
    st.write('You are a male')
elif(radiobutton=='Female'):
    st.write('You are a female') 
else:
    st.error("Please select one option")

st.subheader("Select Box")
selectBox=st.selectbox("Data Science: ",['Data analysis','Web Development','AI/ML',
                               'Cloud Computing','AWS','Mern-Stack',
                              'Image Processing','NLP','Deep Learning',
                              'Web scrapping'])
st.write("You have selected: ",selectBox)

st.subheader("Multi select box")
Multi=st.multiselect("Data Science: ",['Data analysis','Web Development','AI/ML',
                               'Cloud Computing','AWS','Mern-Stack',
                              'Image Processing','NLP','Deep Learning',
                              'Web scrapping'])
st.write('You have selected: ',len(Multi)," Courses",Multi)


st.subheader("Button")
if(st.button('Click Me')):
    st.success("Thanks for clicking this!!")

st.subheader("Slider")
var=st.slider('Select the volume',1,100,step=1)
st.write("The volume ism : ",var)

st.subheader("Text input")
name=st.text_input("Enter your name : ")
if(name):
    st.write("Hi ",name,"to my website")
else:
    st.write("Please enter your name")


password=st.text_input('Password: ',type='password')

st.subheader("Text area")
st.text_area("Write something interesting about yourselg in 20 words",height=20)


st.subheader("Input number")
st.number_input("Select your age",1,100)

st.subheader("input date")
st.date_input("Select date: ")

st.subheader("Input time")
st.time_input('Select time : ')