# -*- coding: utf-8 -*-
"""Copy of 4.6. Train Test Split.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kDLsr-GFtVmdxnMMdlVIJHaS8zc_jkgY

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis

PIMA Diabetes Dataset
"""

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

# printing the first 5 rows of the dataset
diabetes_dataset.head()

# number of rows and Columns in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""SPLITTING THE DATA INTO TRAINING DATA & TESTING DATA"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

