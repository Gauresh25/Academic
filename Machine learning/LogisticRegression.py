import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,BaggingClassifier,GradientBoostingClassifier
import pandas as pd


df = pd.read_csv("Iris.csv")

le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

x= df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = df['Species']


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

samples= len(x_train)
feat = x.shape[1]



def sigmoid(z):
    return(1/(1 + np.exp(-z)))

lr =0.01

allWeight=[]
allbias=[]

for i in range(3):

    y_temp = (y_train == i).astype(int)

    weights = np.zeros(feat)
    bias =0

    for _ in range(1000):
        z =np.dot(x_train,weights)+bias
        pred = sigmoid(z)

        err = pred - y_temp

        weights = weights - lr*(1/samples)*np.dot(x_train.T,err)

        bias = bias - lr*np.sum(err)*1/samples

    allWeight.append(weights)
    allbias.append(bias)

prob=[]
for i in range(3):
    z = np.dot(x_test,allWeight[i]) + allbias[i]
    pred = sigmoid(z)

    pred = (pred>=0.5).astype(int)
    prob.append(pred)

prob = np.array(prob)

final = np.argmax(prob,axis=0)

print(accuracy_score(y_test,final))