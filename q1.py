import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the csv data file
df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv', encoding = 'utf-8')

# Create X and Y dataset
data = df[['total_items', 'order_amount']]
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

# Split X and Y into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2)

# Create best fit line using linear regression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
Y_predict = regressor.predict(X_test)

print(regressor.coef_[0]) # result of a

print(regressor.intercept_) # result of b

# Plot the line
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.show()