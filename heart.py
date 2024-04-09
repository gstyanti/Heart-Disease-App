import streamlit as st
import pickle
import pandas as pd
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

#create  a function to preprocess the data
def main():

    # Set page title
    st.set_page_config(page_title='Heart Disease Prediction App')
    #st.set_page_config(page_footer='Gusti Ayu Putu Febriyanti')

    # Set heading
    st.sidebar.title('Heart Disease Prediction App')

    # Input fields for features
    BMI = st.sidebar.selectbox('BMI', min_value=1, max_value=100, step=1)

    Smoking = st.sidebar.selectbox ('Smoking', ['Yes','No'])
    if Smoking=="Yes":
     Smoking=1
    else:
     Smoking=0

    AlcoholDrinking = st.sidebar.selectbox('Alcohol Drinking', ['Yes', 'No'])
    if AlcoholDrinking =="Yes":
     AlcoholDrinking =1
    else:
     AlcoholDrinking =0

    Stroke = st.sidebar.selectbox('Stroke', ['Yes', 'No'])
    if Stroke =="Yes":
     Stroke =1
    else:
     Stroke =0

    PhysicalHealth = st.sidebar.selectbox('Physica lHealth', min_value=1, max_value=100, step=1)

    MentalHealth = st.sidebar.selectbox('Mental Health', min_value=1, max_value=100, step=1)

    DiffWalking = st.sidebar.selectbox('DiffWalking', ['Yes', 'No'])
    if DiffWalking =="Yes":
     DiffWalking =1
    else:
     DiffWalking =0

    Sex = st.sidebar.selectbox('Sex', ['Yes', 'No'])
    if Sex =="Yes":
     Sex =1
    else:
     Sex =0


    AgeCategory = st.sidebar.selectbox('Age Category', ['18-24', '25-29', '30-34', '35-39','40-44','45-49','50-59','60-64','65-69','70-74','75-79','80 or older'])
    if AgeCategory == '18-24':
     AgeCategory = 1
    elif AgeCategory == '25-29' :
     AgeCategory = 2
    elif AgeCategory == '30-34' :
     AgeCategory = 3
    elif AgeCategory == '35-39' :
     AgeCategory = 4
    elif AgeCategory == '40-44' :
     AgeCategory = 5
    elif AgeCategory == '45-49' :
     AgeCategory = 6
    elif AgeCategory == '50-54' :
     AgeCategory = 7
    elif AgeCategory == '55-59' :
     AgeCategory = 8
    elif AgeCategory == '60-64' :
     AgeCategory = 9
    elif AgeCategory == '65-69' :
     AgeCategory = 10
    elif AgeCategory == '70-74' :
     AgeCategory = 11
    elif AgeCategory == '75-79' :
     AgeCategory = 12
    elif AgeCategory == '80 or older' :
     AgeCategory = 13
    
     Diabetic = st.sidebar.selectbox('Diabetic', ['Yes', 'No'])
    if Diabetic =="No":
     Diabetic =0
    elif Diabetic =="Yes":
     Diabetic =1
    elif Diabetic =="No, borderline diabetes":
     Diabetic =2
    elif Diabetic =="Yes (during pregnancy)":
     Diabetic =3

    PhysicalActivity = st.sidebar.selectbox('Physical Activity', ['Yes', 'No'])
    if PhysicalActivity =="Yes":
     PhysicalActivity =1
    else:
     PhysicalActivity =0

    GenHealth = st.sidebar.selectbox('GenHealth', ['Excellent', 'Very good', 'Good', 'Fair', 'Poor'])
    if GenHealth =="Excellent":
     GenHealth =1
    elif GenHealth =="Very good":
     GenHealth =2
    elif GenHealth =="Good":
     GenHealth =3
    elif GenHealth =="Fair":
     GenHealth =4
    elif GenHealth =="Poor":
     GenHealth =5

    SleepTime = st.sidebar.selectbox('Sleep Time', min_value=1, max_value=100, step=1)

    Asthma = st.sidebar.selectbox('Asthma', ['Yes', 'No'])
    if Asthma =="Yes":
     Asthma =1
    else:
     Asthma =0

     KidneyDisease = st.sidebar.selectbox('Kidney Disease', ['Yes', 'No'])
    if KidneyDisease =="Yes":
     KidneyDisease =1
    else:
     KidneyDisease =0

     SkinCancer = st.sidebar.selectbox('Skin Cancer', ['Yes', 'No'])
    if SkinCancer =="Yes":
     SkinCancer =1
    else:
     SkinCancer =0

    # Create a dictionary with input data
    input_data = {
    'BMI'	: [BMI],
    'Smoking'	: [Smoking],
    'AlcoholDrinking' : [AlcoholDrinking],
    'Stroke'	: [Stroke],
    'PhysicalHealth' : [PhysicalHealth],
    'MentalHealth'	: [MentalHealth],
    'DiffWalking'	: [DiffWalking],
    'Sex'	: [Sex],
    'AgeCategory' : [AgeCategory],
    'Diabetic' : [Diabetic],
    'PhysicalActivity' : [PhysicalActivity],
    'GenHealth'	: [GenHealth],
    'SleepTime'	: [SleepTime],
    'Asthma'	: [Asthma],
    'KidneyDisease'	: [KidneyDisease],
    'SkinCancer' : [SkinCancer]
    }

    #Create a Dataframe from the input data
    input_df = pd.DataFrame(input_data)

    # Train the model
    model = pickle.load(open('heartdisease.pkl', 'rb'))

    # Make predictions
    st.title('PREDIKSI PENYAKIT JANTUNG')
    st.write('Selamat Datang Di Website Kami!')

    # Display the prediction
    if prediction == 0:
     st.write("Tidak Memiliki Resiko Penyakit Jantung")
    else:
     st.write("Memiliki Resiko Penyakit Jantung")

    if __name__== '__main__' :
     main()
     


