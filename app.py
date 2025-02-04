import streamlit as st
import pickle as pkl
import pandas as pd

st.title('Smart Tipper 🤑')
st.header('Upload the data :')

total_bill = st.number_input('Total Bill Amount', min_value=0.0, max_value=1000.0)
time = st.selectbox('Time',['Lunch','Dinner'])
size = st.number_input('Enter the numnber of people', min_value=1, max_value=10)

input_data = {'total_bill':total_bill,'time':time,'size':size}

input_df = pd.DataFrame([input_data])

input_df['time'] = input_df['time'].map({'Lunch':0,'Dinner':1})

df = pd.read_csv('x.csv')
column_list = [col for col in df.columns if col !=['Unnamed: 0']]

model = pkl.load(open('model.pkl','rb'))
prediction = model.predict(input_df)

if st.button('Predict'):
    # st.write('The amount of tip you can get is :',prediction[0])
    st.markdown(f"""
        <div style='
            background-color: #f0f0f0; 
            padding: 10px; 
            border-radius: 5px; 
            text-align: center; 
            font-size: 20px; 
            color: black;'>
            <strong>The Predicted tip =$ {prediction[0]:.2f}</strong>
        </div>
    """, unsafe_allow_html=True)
