# Here we load all the models we need for the project
import time
import pickle
import warnings
import numpy as np


def load_models():
    print('Loading Models')
    breast_cancer_model = get_model('BreastCancer', [[1001, 0.3001, 0.1471, 25.38, 17.33, 184.6, 2019, 0.2654]])
    heart_disease_model = get_model('HeartDisease', [[40,1,0,130,289,0,0,172,0,0,0]])
    eryhemato_model = get_model('EryhematoSquamous', [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
    kidney_model = get_model('Kidney',[[50.0, 80.0, 1.02, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 219.0, 176.0, 13.8, 136.0, 4.5, 8.6, 24.0, 13200.0, 2.7, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0]] )
    lung_cancer_model = get_model('LungCancer', [[1, 55, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])
    diabetes_model = get_model('Diabetes', [[6,148,72,35,0,33.6,0.627,50]])

    print('Models Loaded Successfully')

    return {
        'breast_cancer_model': breast_cancer_model,
        'heart_disease_model': heart_disease_model,
        'eryhemato_model': eryhemato_model,
        'kidney_model': kidney_model,
        'lung_cancer_model': lung_cancer_model,
        'diabetes_model': diabetes_model
    }


def get_model(modelName, input):
    warnings.filterwarnings("ignore")
    print(f'Loading {modelName} model')
    filename = f'models/{modelName}.sav'
    model = pickle.load(open(filename, 'rb'))
    print('Testing The Model')
    prediction = model.predict_proba(input)
    np.set_printoptions(suppress=True)
    print('Prediction: ' + str(prediction) + '%')
    print(f'{modelName} Model Loaded Successfully')
   
    return model