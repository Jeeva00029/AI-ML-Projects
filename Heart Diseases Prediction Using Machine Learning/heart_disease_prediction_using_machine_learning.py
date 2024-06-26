# -*- coding: utf-8 -*-
"""Heart Disease prediction using Machine Learning

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14iRfkSceSEjDRnq6VQkSWArGQ4FQiJjG

import the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import(train_test_split)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")

"""Data Collection and Precessing"""

heart_data=pd.read_csv('/content/heart.csv')
heart_data.head()

heart_data.shape

heart_data.info()

heart_data['target'].value_counts()

"""1--> DEFECTIVE HEART

0--> HEALTHY HEART

Split the dependent parameter and independent parameter:
"""

x=heart_data.drop(columns='target',axis=1)
y=heart_data['target']
print(x)

print(y)

"""**Split the Train data and Test data:**

x_train-->independent data(80%)
x_test--->independent data(20%)
y_train-->dependent data(80%)
y_test--->dependent data(20%)
TO split it random manner with order of given number.
"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,
                                               stratify=y,random_state=2)

"""**Model Training**

Using Logistic Regression Algorithm
"""

model=LogisticRegression()

model.fit(x_train,y_train)

"""**Accuracy for Trained Model**

>


"""

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)
print("Accuracy on Training data:",training_data_accuracy)

"""**Model Testing**"""

input_data=(71,0,0,112,149,0,1,125,0,1.6,1,0,2)
#change the input data to array
input_data_array=np.asarray(input_data)
#reshape the array for our predicting o/p be either 0 or 1
input_data_reshaped=input_data_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==1):
  print("This Person Have a Heart Diseases")
else:
  print("This Person are Healthy. Don't Worry... ")

input_data=(54,1,0,122,286,0,0,116,1,3.2,1,2,2)
#change the input data to array
input_data_array=np.asarray(input_data)
#reshape the array for our predicting o/p be either 0 or 1
input_data_reshaped=input_data_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==1):
  print("This Person Have a Heart Diseases")
else:
  print("This Person are Healthy. Don't Worry... ")

"""**Accuracy for Testing Model**"""

x_test_prediction=model.predict(x_test)
tested_data_accuracy=accuracy_score(x_test_prediction,y_test)
print("Accuracy on Testing data:",tested_data_accuracy)

"""
save a model"""

import joblib
joblib.dump(model,"heartdisprediction.pkl")