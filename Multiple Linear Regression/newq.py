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
X=ohe.transform(X).toarray()
X=X[:,1:]
from sklearn.cross_validation import train_test_split
X_train,Y_train,X_test,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
results=regressor.predict(X_test)
plt.scatter(X_train,Y_train,color="Red")
plt.plot(X_train),regressor.predict(X_test),color="Green")
plt.title("Salary with Mutiple Regression")
plt.xlabel("Features")
plt.ylabel('Salary')
