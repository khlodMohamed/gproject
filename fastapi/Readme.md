## Dependencies 
- FastAPI
- uvicorn
- sklearn
- scikit-learn
- numpy

```bash

pip3 install "fastapi[all]" "uvicorn[standard]" sklearn scikit-learn numpy

```

## Run the Code
```bash

uvicorn main:app --reload

```

## End Points
We have 2 end points, one dummy ``('/')`` and one for serving our models ``('/{model}')`` we're using 6 different models to predict 6 different diseases
```pyhton

breast_cancer_model
heart_disease_model
eryhemato_model
kidney_model
lung_cancer_model
diabetes_model

```

## Prediction
In order to pridect a disease send the symptoms to the backend as a post request body to `http://localhost:8000/{model}` after deployment the `localhost` will be replaced by the `baseurl` 
### Request Body
the symptoms is required as a list of float. 
```python

  url = "http://localhost:8000/lung_cancer_model"
  input = {"input_list": [1, 55, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}

```

### Response 
the server will respond to the post request with the prediction probabilty, and its class. 
```json

{ 
  "Probability": "78.0375457875458",
  "PredictionClass": "0" 
 }

```
