# Importing the libraries
import pandas as pd

#Reading Data
Data =pd.read_csv("diabetes.csv")
Data.head()

#Summary about Data
Data.describe()    
Data.isna().sum()  ## chaecking for null values
Data.columns
X = Data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']]
X
y =Data['Outcome']
y
y.value_counts()
from sklearn.model_selection import train_test_split
X_train ,X_test ,y_train ,y_test = train_test_split(X ,y , test_size =0.2  , random_state =42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Modeling
#1. K_nearest_neighbours (KNN)`
#Training
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
k =10
knn =KNeighborsClassifier(k)
knn.fit(X_train ,y_train)

#Predicting
y_pred = knn.predict(X_test)
y_pred

#Calculate Acuuracy
print('The accuracy of KNN is {}%'.format((accuracy_score(y_test, y_pred)*100)))

#2.Logisitc Regression
from sklearn.linear_model import LogisticRegression

#Training
LR = LogisticRegression(C=0.2, solver='liblinear')
LR.fit(X_train,y_train)

#Predicting
y_pred = LR.predict(X_test)
y_pred

#Calculate Acuuracy
print("The Acuracy of Logistic {}% ". format(accuracy_score(y_test ,y_pred) *100))

#3. Decision Tree
from sklearn.tree import DecisionTreeClassifier

#Training
outcomeTree = DecisionTreeClassifier(criterion="entropy", max_depth =2)
outcomeTree.fit(X_train, y_train)

#Predicting
y_pred = outcomeTree.predict(X_test)
y_pred

#Calculate Acuuracy
print('The accuracy is {}%'.format((accuracy_score(y_test, y_pred))*100))

