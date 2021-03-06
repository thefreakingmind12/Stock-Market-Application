#Regression for Stock Data
#User Quandl as a Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl as q
import math
from sklearn import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture

# Google Dataset for Test
df = q.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. Close', 'Adj. High', 'Adj. Low', 'Adj. Volume']]
df['HLT'] = df['Adj. Open'] - df['Adj. Close']/df['Adj. Close'] * 100
df['PCT_CHANGE'] = df['Adj. High'] - df['Adj. Low']/df['Adj. Low'] * 100
forcast_column = 'Adj. Close'
df.fillna(-9999, inplace=True)
forcast_out = int(math.ceil(0.1*(len(df))))
df['label'] = df[forcast_column].shift(-forcast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x = preprocessing.scale(x)
df.dropna(inplace=True)
y = np.array(df['label'])

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.3)
linear_regression = LinearRegression()
linear_regression.fit(x_train, y_train)
accuracy = linear_regression.score(x_test, y_test)
svm = svm.SVR()
svm.fit(x_train, y_train)
new_acc = svm.score(x_test, y_test)
gmm = GaussianMixture(n_components=3, covariance_type='diag')
gmm.fit(x_train, y_train)
score = gmm.score(x_test, y_test)
print("Score for GMM is",score)
print("Accuracy of Support Vector Machine", new_acc)
print("Accuracy of Linear Regression",  accuracy)

