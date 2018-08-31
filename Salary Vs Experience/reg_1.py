import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train, Y_train)
#NOw finally we can predict the salries of the employees
#we will use another method from the class called predict to predict the result
results=reg.predict(X_test)
#now to visualize our training set
plt.scatter(X_train,Y_train,color='green')
plt.plot(X_train,reg.predict(X_train),color='red')
plt.title('Salary Vs Experience ')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()
#now its time to visualize our test set
plt.scatter(X_test,Y_test,color='green')
plt.plot(X_train,reg.predict(X_train),color='red')
plt.title('Salary Vs Experience ')
plt.xlabel('Years Of Experience')
plt.ylabel('Salary')
plt.show()