from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,classification_report
import pandas as pd

df = pd.read_csv("Iris.csv")

#print(df.head)

df['Species'] = df['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
#print(df.head)

x= df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = df['Species']

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform((x_test))

model = SVC(kernel='rbf', random_state=42)
model.fit(x_train_scaled,y_train)

pred = model.predict(x_test_scaled)

conf = confusion_matrix(y_test,pred)
print(conf)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred,average='weighted')
recall = recall_score(y_test, pred, average='weighted')
report = classification_report(y_test, pred)


print("\nEvaluation Metrics")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")

print("\nClassification Report")
print(report)

