import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('save_steps.pkl','rb') as file:
       data= pickle.load(file)
    return data

data=load_model()

model = data["model"]
Co_enc  = data["Co_enc"]
Ed_enc=data["Ed_enc"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""###We need some information to predict the salary""")
    countries = (
    "United States",       
    "India",                
    "United Kingdom",     
    "Germany",              
    "Canada",               
    "Brazil",                
    "France",                
    "Spain",                 
    "Australia",              
    "Netherlands",          
    "Poland",                
    "Italy",                
    "Russian Federation", 
    "Sweden"  
    )
    education =("Bachelors degree", 'Masters degree', 'Less than a Bachelors',
        'Post Graduation')

    country=st.selectbox("select country",countries)
    Education=st.selectbox("Select Education",education)
    experience=st.slider("years of experience",0,5,3)

    ok=st.button("click to predict salary")

    if ok:
        x=np.array([[country,Education,experience]])
        x[:,0] =Co_enc.transform(x[:,0])
        x[:,1] =Ed_enc.transform(x[:,1])
        x=x.astype(float)

        salary=model.predict(x)
        st.subheader(f"The estimated Salary is ${salary[0]:.2f}")
    

