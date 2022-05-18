import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title("This is a title")
st.text("This some text")
st.markdown("Streamlit is ***really cool*** :+1:")
st.header('This is a header')
st.subheader('This is a subheader')

#succes info error
st.success('This is a succes message')
st.info('This is a info message')
st.error('This is a error message')

#st.help(range)

st.write('Hello, world!')
st.write('Hello, *World!* :sunglasses:')

#image
img = Image.open('images.jpeg')
st.image(img, caption='cattie',width=300)

#video
#my_video = open('ml.mov', 'rb')
#st.video(my_video)
#st.video('https://www.youtube.com/watch?v=uHKfrz65KSU')

#checkbox
cbox = st.checkbox('Hide and Seek')
if cbox:
    st.write('Hide')
else:
    st.write('seek')

#radio button
st.radio('Select a color', ('blue', 'orange', 'yellow'))

status = st.radio('Select a color', ('Blue', 'Red', 'Yellow'))
st.write('Your favourite color is {}.'.format(status))

#button
st.button('Button')

if st.button('Press me'):
    st.success('Analyze results are...')

#select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option:", occupation)
sn = st.selectbox("Select a number",[1,2,3,4,5])

#multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

#slider
option1 = st.slider('select a number', min_value=50, max_value=300, value=100, step=5)
option2 = st.slider('select a number', 20, 100, step=1)
option1*option2
option2 = st.slider('select a number')

#text_input
name = st.text_input('Enter your name', placeholder='Your name is')

if st.button('Submit'):
    st.write('Hello {}!'.format(name.title()))

#code
st.code('import pandas as pd\nimport numpy as np')

with st.echo():
    import pandas as pandas
    import numpy as numpy
    df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
    df

#date input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

d = st.date_input('When is your birthday?', datetime.date(2022,4,28))

#time_input
the_time = st.time_input('The time is', datetime.time(8,45))

st.sidebar.title('Sidebar Title')
a=st.sidebar.slider('input1', 0, 5, 2, 1)
x=st.sidebar.slider('input2')
st.success(a*x)

#dataframe
#3 methods: write-table-dataframe

df=pd.read_csv('Advertising.csv', nrows=100)
st.table(df.head())
st.write((df.head()))
st.dataframe(df.head())

# using trained model
import pickle
from sklearn.linear_model import LinearRegression

filename = 'finalized_model.sav'
model = pickle.load(open(filename,'rb'))
pred = model.predict([[17000,35000, 50000]])
st.write('prediction:', pred)

TV=st.sidebar.slider('TV', 0, 300000, 150000, 100) 
Radio=st.sidebar.slider('Radio', 0, 100000, 50000, 50)
Newspaper=st.sidebar.slider('Newspaper', 0, 50000, 25000, 50)
pred = model.predict([[TV,Radio,Newspaper]])
st.write('prediction:', pred)


a = st.sidebar.number_input("TV:",value=230, step=10)
b = st.sidebar.number_input("radio:",value=37, step=10)
c = st.sidebar.number_input("newspaper:",value=69, step=10)
if st.button("Predict"): 
    pred = model.predict([[a,b,c]])
    st.write(pred)


html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)


tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))
def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample
df = single_customer()
st.table(df)