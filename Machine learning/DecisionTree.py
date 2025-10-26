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

# scaler = StandardScaler
#
# x_train = scaler.fit_transform(x_train)
# x_test = scaler.transform(x_test)

model1 =RandomForestClassifier(
    n_estimators=2,
    random_state=42
)
model1.fit(x_train,y_train)

pred = model1.predict(x_test)

ac= accuracy_score(y_test,pred)
print(ac)

from sklearn.decomposition import PCA

pc = PCA(n_components=2,random_state=42)

px_train = pc.fit_transform(x_train)
px_test = pc.transform(x_test)

model2 =RandomForestClassifier(
    n_estimators=2,
    random_state=42
)
model2.fit(x_train,y_train)

pred = model2.predict(x_test)

ac= accuracy_score(y_test,pred)
print(ac)

print(pc.explained_variance_ratio_)
import matplotlib.pyplot as plt
plt.bar(range(1, len(pc.explained_variance_ratio_) + 1),
            pc.explained_variance_ratio_)
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.title(f'Total Variance Explained: {pc.explained_variance_ratio_.sum():.2%}')
plt.show()