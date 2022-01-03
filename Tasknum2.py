# import libraries
import pandas as pd 
import matplotlib.pyplot as plt

#Read data and convert it to Data
d = pd.read_csv("Wuzzuf_Jobs.csv")
d.head()

#Summary of Data
d.describe()

#Clean data or remove null and duplicated data
d.isnull().sum()
sum(d.duplicated())
d.drop_duplicates(inplace =True)
sum(d.duplicated())

#1: Factorize the YearsExp feature and convert it to numbers in new col
d["YearsExp"].value_counts()
d["Factorize-YearsExp"] =pd.factorize(d["YearsExp"])[0]
d.head()

#2:Apply K-means for job title and companies.
#First we factorize title and company feature
d["Factorize-Title"] =pd.factorize(d["Title"])[0]
d["Factorize-Company"] =pd.factorize(d["Company"])[0]
d.head()
M = d.iloc[: ,[-2,-1]]
from sklearn.cluster import KMeans
wcss=[]
for i in  range (1 ,11):
    km = KMeans(n_clusters = i ,init ='k-means++' ,random_state = 42 ,max_iter = 500)
    km.fit(M)
    wcss.append(km.inertia_)
plt.plot(range(1,11) , wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

#From the graph we choose 2 clusters
km =KMeans(n_clusters =2 , init ='k-means++' ,random_state = 42)
y_mean = km.fit_predict(M)
y_mean
M['target'] = y_mean 
M.head() 
plt.scatter(M.iloc[:,0] , M.iloc[:,1] , color = 'blue')
plt.show()


#filter rows of original data
filtered_label0 = M.loc[M.target == 0]
filtered_label1 = M.loc[M.target == 1]
 
#Plotting the results
plt.figure(figsize =(20 ,8))
plt.scatter(filtered_label0.iloc[:,0] , filtered_label0.iloc[:,1] , color = 'red' , s=50 , label ='cluster 1')
plt.scatter(filtered_label1.iloc[:,0] , filtered_label1.iloc[:,1] , color = 'black' , s=50 ,label = 'cluster 2')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s =500, c = 'yellow', label = 'Centroids')
plt.xlabel("Jobs Title")
plt.ylabel("Company")
plt.title("Clusters of employees")
plt.legend()
plt.show()

