import numpy as np
import pandas as pd


df = pd.read_csv("Salary_dataset.csv")

df = df.dropna()

print(df.head())

X = df[['YearsExperience']].values #add multiple columns if required
Y = df['Salary'].values

split= int(0.8 * len(X))

x_train = X[:split]
x_test= X[split:]
y_train = Y[:split]
y_test = Y[split:]

x_train = (x_train - x_train.mean(axis= 0))/x_train.std(axis = 0)
x_test = (x_test - x_test.mean(axis= 0))/x_test.std(axis = 0)


x_train = np.c_[np.ones(len(x_train)),x_train]
x_test = np.c_[np.ones(len(x_test)),x_test]

weights = np.zeros(x_train.shape[1])

lr = 0.01
epochs = 20000

for i in range(epochs):
    y_pred = x_train @ weights
    error = y_pred - y_train

    gradient = x_train.T @error /len(x_train)

    weights = weights - lr *gradient

y_pred = x_test @weights
rmse = np.sqrt(np.mean((y_pred-y_test)**2))
print(rmse)