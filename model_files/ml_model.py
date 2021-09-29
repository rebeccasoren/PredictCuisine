import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle

##functions
def transform_input(x):
    ingredients = pd.read_csv('https://raw.githubusercontent.com/rebeccasoren/PredictCuisine/master/model_files/mycsv?token=AMMDH2B6QG36LUGYJHIFQYDBLVGZQ', encoding="latin_1")   
    test = pd.DataFrame(columns=ingredients.columns, index = [0])    
    for col in test.columns:
        test[col].values[:] = 0
        if (col in x):
            test[col].values[:] = 1            
    return test

def predict_cuisine(x, model):
    test = transform_input(x)
    y_pred = model.predict(test)[0]
    return y_pred