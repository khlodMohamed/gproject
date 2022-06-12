import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

portfastapi = os.getenv('PORTFastapi',default="8000")
portfastapi=str(portfastapi)
print(portfastapi)
########################################################################

def handle_click_wo_button():
    if st.session_state.kind_of_action:
        st.session_state.type=st.session_state.kind_of_action
    elif st.session_state.disease_chosen:
        st.session_state.type=st.session_state.disease_chosen

########################################################################
        
def option_chosen(option):
    if option=='Not present':
      return 0
    elif option=='Low intermediate value':
      return 1
    elif option=='High intermediate value':
      return 2
    else:
      return 3

########################################################################
    
def heart_insert_features():
    
    form1 = st.form(key='form1')

    Age = form1.number_input('Age', min_value=0, step=1)
    Sex = form1.selectbox('Sex', ['Male', 'Female'])
    ChestPainType = form1.selectbox('Chest Pain Type', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
    RestingBP = form1.number_input('Resting BP', min_value=0, step=1)
    Cholesterol = form1.number_input('Cholesterol', min_value=0, step=1)
    FastingBS = form1.selectbox('Fasting BS', ['FastingBS > 120 mg/dl', 'otherwise'])
    RestingECG = form1.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'])
    MaxHR = form1.number_input('Max HR', min_value=0, step=1)
    ExerciseAngina = form1.selectbox('Exercise Angina', ['Yes', 'No'])
    Oldpeak = form1.number_input('Oldpeak', step=0.1, format="%.1f")
    ST_Slope = form1.selectbox('ST Slope', ['upsloping', 'flat', 'downsloping'])

    if Sex=='Male':
      Sex = 0
    else:
      Sex = 1
      
    if ChestPainType=='Typical angina':
      ChestPainType = 0
    elif ChestPainType=='Atypical angina':
      ChestPainType = 1
    elif ChestPainType=='Non-anginal pain':
      ChestPainType = 2
    else:
      ChestPainType = 3            

    if FastingBS=='FastingBS > 120 mg/dl':
      FastingBS = 1
    else:
      FastingBS = 0
  
    if RestingECG=='Normal':
      RestingECG = 0
    elif RestingECG=='ST':
      RestingECG = 1
    else:
      RestingECG = 2

    if ExerciseAngina=='Yes':
      ExerciseAngina = 1
    else:
      ExerciseAngina = 0

    if ST_Slope=='upsloping':
      ST_Slope = 0
    elif ST_Slope=='flat':
      ST_Slope = 1
    else:
      ST_Slope = 2            
     
    input = {"input_list": [Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]}
    url = "http://fastapi:"+str(portfastapi)+"/heart_disease_model"

    if form1.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='1':
            form1.success("Probability to have Heart Disease: " + response.json()["Probability"] + "%")
        else:
            form1.success("Probability to have No Heart Disease: " + response.json()["Probability"] + "%")
    
        
########################################################################

def breast_cancer_insert_features():
    
    form2 = st.form(key='form2')
    
    area_mean = form2.number_input('area mean', min_value=0.0, step=1e-6, format="%.6f")
    concavity_mean = form2.number_input('concavity mean', min_value=0.0, step=1e-6, format="%.6f")
    concave_points_mean = form2.number_input('concave points mean', min_value=0.0, step=1e-6, format="%.6f")
    radius_worst = form2.number_input('radius worst', min_value=0.0, step=1e-6, format="%.6f")
    texture_worst = form2.number_input('texture worst', min_value=0.0, step=1e-6, format="%.6f")
    perimeter_worst = form2.number_input('perimeter worst', min_value=0.0, step=1e-6, format="%.6f")
    area_worst = form2.number_input('area worst', min_value=0.0, step=1e-6, format="%.6f")
    concave_points_worst = form2.number_input('concave points worst', min_value=0.0, step=1e-6, format="%.6f")
    
    input = {"input_list": [area_mean, concavity_mean, concave_points_mean, radius_worst, texture_worst, perimeter_worst, area_worst, concave_points_worst]}
    url = "http://fastapi:"+portfastapi+"/breast_cancer_model"

    if form2.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='1':
            form2.success("Probability to have Breast Cancer: " + response.json()["Probability"] + "%")
        else:
            form2.success("Probability to have No Breast Cancer: " + response.json()["Probability"] + "%")

########################################################################

def erythemato_insert_features():

    form3 = st.form(key='form3')

    options_list = ['Not present', 'Low intermediate value', 'High intermediate value', 'Large value']

    erythema = option_chosen(form3.selectbox('erythema', options_list))
    scaling = option_chosen(form3.selectbox('scaling', options_list))
    definite_borders = option_chosen(form3.selectbox('definite borders', options_list))
    itching = option_chosen(form3.selectbox('itching', options_list))
    koebner_phenomenon = option_chosen(form3.selectbox('koebner phenomenon', options_list))
    polygonal_papules = option_chosen(form3.selectbox('polygonal papules',  options_list))
    follicular_papules = option_chosen(form3.selectbox('follicular papules', options_list))
    knee_and_elbow_involvement = option_chosen(form3.selectbox('knee and elbow involvement', options_list))
    family_history = option_chosen(form3.selectbox('family history', options_list))
    eosinophils_in_the_infiltrate = option_chosen(form3.selectbox('eosinophils in the infiltrate', options_list))
    pnl_infiltrate = option_chosen(form3.selectbox('pnl infiltrate', options_list))
    fibrosis_of_the_papillary_dermis = option_chosen(form3.selectbox('fibrosis of the papillary dermis', options_list))
    acanthosis = option_chosen(form3.selectbox('acanthosis', options_list))
    hyperkeratosis = option_chosen(form3.selectbox('hyperkeratosis', options_list))
    parakeratosis = option_chosen(form3.selectbox('parakeratosis', options_list))
    inflammatory_monoluclear_infiltrate = option_chosen(form3.selectbox('inflammatory monoluclear infiltrate', options_list))
    age = form3.number_input('age', min_value=0, step=1)

    input = {"input_list": [erythema, scaling, definite_borders, itching, koebner_phenomenon, polygonal_papules, follicular_papules, knee_and_elbow_involvement, family_history, eosinophils_in_the_infiltrate, pnl_infiltrate, fibrosis_of_the_papillary_dermis, acanthosis, hyperkeratosis, parakeratosis, inflammatory_monoluclear_infiltrate, age]}
    url = "http://fastapi:"+portfastapi+"/eryhemato_model"

    if form3.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='1':
            form3.success("Probability to have Psoriasis: " + response.json()["Probability"] + "%")
        elif response.json()["PredictionClass"]=='2':
            form3.success("Probability to have Seboreic Dermatitis: " + response.json()["Probability"] + "%")
        elif response.json()["PredictionClass"]=='3':
            form3.success("Probability to have Lichen Planus: " + response.json()["Probability"] + "%")
        elif response.json()["PredictionClass"]=='4':
            form3.success("Probability to have Pityriasis Rosea: " + response.json()["Probability"] + "%")
        elif response.json()["PredictionClass"]=='5':
            form3.success("Probability to have Chronic Dermatitis: " + response.json()["Probability"] + "%")
        else:
            form3.success("Probability to have Pityriasis Rubra Pilaris: " + response.json()["Probability"] + "%")

########################################################################

def kidney_insert_features():

    form4 = st.form(key='form4')

    age = form4.number_input('age', min_value=0, step=1)
    blood_pressure = form4.number_input('blood pressure', min_value=0, step=1)
    specific_gravity = form4.number_input('specific gravity', min_value=0.0, step=0.001, format="%.3f")
    albumin = form4.number_input('albumin', min_value=0.0, step=0.1, format="%.1f")
    sugar = form4.number_input('sugar', min_value=0, step=1)
    red_blood_cells = form4.selectbox('red blood cells', ['normal', 'abnormal'])            
    pus_cell = form4.selectbox('pus cell', ['normal', 'abnormal'])
    pus_cell_clumps = form4.selectbox('pus cell clumps', ['notpresent', 'present'])
    bacteria = form4.selectbox('bacteria', ['notpresent', 'present'])
    blood_glucose_random = form4.number_input('blood glucose random', min_value=0, step=1)
    blood_urea = form4.number_input('blood urea', min_value=0.0, step=0.1, format="%.1f")
    serum_creatinine = form4.number_input('serum creatinine', min_value=0.0, step=0.01, format="%.2f")
    sodium = form4.number_input('sodium', min_value=0.0, step=0.1, format="%.1f")
    potassium = form4.number_input('potassium', min_value=0.0, step=0.1, format="%.1f")
    haemoglobin = form4.number_input('haemoglobin', min_value=0.0, step=0.1, format="%.1f")
    packed_cell_volume = form4.number_input('packed cell volume', min_value=0.0, step=0.1, format="%.1f")
    white_blood_cell_count = form4.number_input('white blood cell count', min_value=0.0, step=0.1, format="%.1f")
    red_blood_cell_count = form4.number_input('red blood cell count', min_value=0.0, step=0.1, format="%.1f")
    hypertension = form4.selectbox('hypertension', ['yes', 'no'])
    diabetes_mellitus = form4.selectbox('diabetes mellitus', ['yes', 'no'])
    coronary_artery_disease = form4.selectbox('coronary artery disease', ['yes', 'no'])
    appetite = form4.selectbox('appetite', ['good', 'poor'])
    peda_edema = form4.selectbox('peda edema', ['yes', 'no'])
    aanemia = form4.selectbox('aanemia', ['yes', 'no'])
                
    if red_blood_cells=='normal':
      red_blood_cells = 1
    else:
      red_blood_cells = 0
      
    if pus_cell=='normal':
      pus_cell = 1
    else:
      pus_cell = 0
      
    if pus_cell_clumps=='notpresent':
      pus_cell_clumps = 0
    else:
      pus_cell_clumps = 1
      
    if bacteria=='notpresent':
      bacteria = 0
    else:
      bacteria = 1
      
    if hypertension=='yes':
      hypertension = 1
    else:
      hypertension = 0
      
    if diabetes_mellitus=='yes':
      diabetes_mellitus = 1
    else:
      diabetes_mellitus = 0
      
    if coronary_artery_disease=='yes':
      coronary_artery_disease = 1
    else:
      coronary_artery_disease = 0
      
    if appetite=='good':
      appetite = 0
    else:
      appetite = 1
      
    if peda_edema=='yes':
      peda_edema = 1
    else:
      peda_edema = 0
      
    if aanemia=='yes':
      aanemia = 1
    else:
      aanemia = 0
      
    input = {"input_list": [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]}
    url = "http://fastapi:"+portfastapi+"/kidney_model"
    
    if form4.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='0':
            form4.success("Probability to have Chronic Kidney Disease: " + response.json()["Probability"] + "%")
        else:
            form4.success("Probability to have No Chronic Kidney Disease: " + response.json()["Probability"] + "%")

########################################################################

def diabetes_insert_features():
    
    form5 = st.form(key='form5')

    Pregnancies = form5.number_input('Pregnancies', min_value=0, step=1)
    Glucose = form5.number_input('Glucose', min_value=0, step=1)
    BloodPressure = form5.number_input('Blood Pressure', min_value=0, step=1)
    SkinThickness = form5.number_input('Skin Thickness', min_value=0, step=1)
    Insulin = form5.number_input('Insulin', min_value=0, step=1)
    BMI = form5.number_input('BMI', min_value=0.0, step=0.1, format="%.1f")
    DiabetesPedigreeFunction = form5.number_input('Diabetes Pedigree Function', min_value=0.0, step=0.001, format="%.3f")
    Age = form5.number_input('Age', min_value=0, step=1)
    
    input = {"input_list": [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]}
    url = "http://fastapi:"+portfastapi+"/diabetes_model"
    
    if form5.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='1':
            form5.success("Probability to have Diabetes: " + response.json()["Probability"] + "%")
        else:
            form5.success("Probability to have No Diabetes: " + response.json()["Probability"] + "%")
        
########################################################################

def lung_cancer_insert_features():

    form6 = st.form(key='form6')
    
    Gender = form6.selectbox('Gender', ['Male', 'Female'])
    Age = form6.number_input('Age', min_value=0, step=1)
    Smoking = form6.selectbox('Smoking', ['yes', 'no'])
    YellowFingers = form6.selectbox('Yellow Fingers', ['yes', 'no'])
    Anxiety = form6.selectbox('Anxiety', ['yes', 'no'])
    Peerpressure  = form6.selectbox('Peer pressure', ['yes', 'no'])
    ChronicDisease  = form6.selectbox('Chronic Disease', ['yes', 'no'])
    Fatigue = form6.selectbox('Fatigue', ['yes', 'no'])
    Allergy = form6.selectbox('Allergy', ['yes', 'no'])
    Wheezing = form6.selectbox('Wheezing', ['yes', 'no'])
    Alcohol = form6.selectbox('Alcohol', ['yes', 'no'])
    Coughing = form6.selectbox('Coughing', ['yes', 'no'])
    Shortnessofbreath = form6.selectbox('Shortness of breath', ['yes', 'no'])
    SwallowingDifficulty = form6.selectbox('Swallowing Difficulty', ['yes', 'no'])
    Chestpain = form6.selectbox('Chest pain', ['yes', 'no'])
    
    if Gender=='Male':
      Gender = 1
    else:
      Gender = 0
      
    if Smoking=='yes':
      Smoking = 1
    else:
      Smoking = 0
      
    if Anxiety=='yes':
      Anxiety = 1
    else:
      Anxiety = 0              
      
    if YellowFingers=='yes':
      YellowFingers = 1
    else:
      YellowFingers = 0
      
    if Peerpressure=='yes':
      Peerpressure = 1
    else:
      Peerpressure = 0
      
    if ChronicDisease=='yes':
      ChronicDisease = 1
    else:
      ChronicDisease = 0
      
    if Fatigue=='yes':
      Fatigue = 1
    else:
      Fatigue = 0
      
    if Allergy=='yes':
      Allergy = 1
    else:
      Allergy = 0
      
    if Wheezing=='yes':
      Wheezing = 1
    else:
      Wheezing = 0
      
    if Alcohol=='yes':
      Alcohol = 1
    else:
      Alcohol = 0
      
    if Coughing=='yes':
      Coughing = 1
    else:
      Coughing = 0
      
    if Shortnessofbreath =='yes':
      Shortnessofbreath = 1
    else:
      Shortnessofbreath = 0
      
    if SwallowingDifficulty=='yes':
      SwallowingDifficulty = 1
    else:
      SwallowingDifficulty = 0

    if Chestpain=='yes':
      Chestpain = 1
    else:
      Chestpain = 0                     
     
    input = {"input_list": [Gender, Age, Smoking, YellowFingers, Anxiety, Peerpressure , ChronicDisease, Fatigue, Allergy, Wheezing, Alcohol, Coughing, Shortnessofbreath, SwallowingDifficulty, Chestpain]}
    url = "http://fastapi:"+portfastapi+"/lung_cancer_model"
    
    if form6.form_submit_button('Predict'):
        response = requests.post(url, json = input)
        if response.json()["PredictionClass"]=='1':
            form6.success("Probability to have Lung Cancer: " + response.json()["Probability"] + "%")
        else:
            form6.success("Probability to have No Lung Cancer: " + response.json()["Probability"] + "%")
        
########################################################################

def main():
    
    st.set_page_config(page_title="Doctor's Assistant", page_icon=":smile:")
    st.sidebar.title("Diagnosis Prediction")
    diseases = ['', 'Heart Disease', 'Chronic Kidney Disease', 'Diabetes', 'Breast Cancer', 'Erythemato-Squamous Disease', 'Lung Cancer']
    st.session_state['option'] = st.sidebar.selectbox('Choose a Disease:', diseases, on_change=handle_click_wo_button, key='disease_chosen')
    st.session_state['kind'] = st.sidebar.radio('What kind of action?',['Insert Features', 'More Information'], on_change=handle_click_wo_button, key='kind_of_action')

    if st.session_state['kind']=='Insert Features':
        
        if st.session_state['option']=='Heart Disease':
            heart_insert_features()
            
        elif st.session_state['option']=='Breast Cancer':
            breast_cancer_insert_features()
                
        elif st.session_state['option']=='Erythemato-Squamous Disease':
            erythemato_insert_features()
            
        elif st.session_state['option']=='Chronic Kidney Disease':
            kidney_insert_features()
            
        elif st.session_state['option']=='Diabetes':
            diabetes_insert_features()
            
        elif st.session_state['option']=='Lung Cancer':
            lung_cancer_insert_features()

        else:
            st.image('doctor.gif')

    else:
        
        if st.session_state['option']=='Heart Disease':
            st.write('A typical goal is to classify the input into one of two states, heart disease or normal according to eleven user-provided features. This dataset was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for research purposes.')           
            st.image('heart1.png')
            st.write('The source of the dataset can be found at: https://archive.ics.uci.edu/ml/machine-learningdatabases/heart-disease/')
            st.write('The final best model used for Heart Disease prediction was found to be the Random Forest Classifier model with all features and an accuracy of 0.913')
            st.image('heart2.png')

        elif st.session_state['option']=='Breast Cancer':
            st.write('The Wisconsin Diagnostic Breast Cancer dataset is a real-valued multivariate data that consists of two classes, where each class signifies whether a patient has breast cancer or not. The two categories are: malignant and benign. Each record represents data for one breast cancer case. Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.')
            st.image('breastcancer1.png')
            st.write('The source of the dataset can be found at: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)')
            st.write('The final best model used for Breast Cancer prediction was found to be the Random Forest Classifier model with a feature selection method of Recursive Feature Elimination using 8 features selected out of 30 and an accuracy of 0.9736842105263158.')
            st.image('breastcancer2.png')
            
        elif st.session_state['option']=='Erythemato-Squamous Disease':
            st.write('The differential diagnosis of erythemato-squamous diseases is a real problem in dermatology. They all share the clinical features of erythema and scaling, with very little differences. The diseases in this group are: 1-psoriasis 2- seboreic dermatitis 3-lichen planus 4- pityriasis rosea 5- cronic dermatitis 6- pityriasis rubra pilaris. The goal of erythemato-squamous predection is to classificate between the previous six diseases.')
            st.image('eryhemato1.jpg')
            st.write('The source of the dataset can be found at: https://archive.ics.uci.edu/ml/machine-learningdatabases/dermatology/')
            st.write('The final best model used for Erythemato-Squamous Disease prediction was found to be the Logistic Regression Classifier model with a feature selection method of Pearson Correlation using 17 features selected out of 34 and an accuracy of 0.9090909090909091.')
            st.image('eryhemato2.jpg')
            
        elif st.session_state['option']=='Chronic Kidney Disease':
            st.write('The data was taken over a 2-month period in India with 25 features (eg, red blood cell count, white blood cell count, etc). The target is the "classification", which is either "ckd" or "notckd" - ckd=chronic kidney disease. There are 400 rows in the dataset.')
            st.image('kidney1.jpg')
            st.write('0: Chronic Kidney Disease       1: No Chronic Kidney Disease')
            st.write('The source of the dataset can be found at: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease')
            st.write('The final best model used for Chronic Kidney Disease prediction was found to be the Gradient Boost Classifier model with all features and an accuracy of 0.99166.')
            st.image('kidney2.png')
                     
        elif st.session_state['option']=='Diabetes':
            st.write('The data was collected and made available by "National Institute of Diabetes and Digestive and Kidney Diseases" as part of the Pima Indians Diabetes Database. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here belong to the Pima Indian heritage (subgroup of Native Americans), and are females of ages 21 and above.')
            st.image('diabetes1.jpg')
            st.write('0: No Diabetes       1: Diabetes')
            st.write('The source of the dataset can be found at: https://www.kaggle.com/datasets/kandij/diabetes-dataset')
            st.write('The final best model used for Diabetes prediction was found to be the Random forest Classifier model with all features and an accuracy of 0.8226950.')
            st.image('diabetes2.jpg')
            
        elif st.session_state['option']=='Lung Cancer':
            st.write('The effectiveness of cancer prediction system helps the people to know their cancer risk with low cost and it also helps the people to take the appropriate decision based on their cancer risk status. The data is collected from the website online lung cancer prediction system. The dataset contains 16 attributes.')
            st.image('lung1.jpg')
            st.write('The source of the dataset can be found at: https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer')
            st.write('The final best model used for Lung Cancer prediction was found to be the Random Forest Classifier model with all features and an accuracy of 0.903614.')
            st.image('lung2.jpg')

        else:
            st.image('doctor.gif')

########################################################################

if __name__ == '__main__':
    main()
