import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[: , :-1].values
Y=dataset.iloc[: , 4 ].values
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
label=LabelEncoder()
X[: , 3]=label.fit_transform(X[: , 3])
ohe=OneHotEncoder(categorical_features=[3])
X=ohe.fit_transform(X).toarray()
X=X[:,1:]#to avoid the dummy variable trap
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
results_y=regressor.predict(X_test)
