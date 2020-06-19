import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('ex.csv')
npmatrix=np.matrix(dataset)
X,Y=npmatrix[:,0],npmatrix[:,1]

regression=linear_model.LinearRegression()
regression.fit(X,Y)

a=regression.intercept_
b=regression.coef_[0]
x=input("enter the X values ")
y=float(round(((b*x)+a),2))
print("corrosponding Y value is ",y)
#print("coefficients: this is the slope 'b' \n",b)
#print("coefficients: this is the intercept 'a' \n",a)

