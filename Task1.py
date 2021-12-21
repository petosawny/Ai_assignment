# addition.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Run python autograder.py
"""
#add libraries
import pandas as pd
import matplotlib.pyplot as plt

#read dataset
ds = pd.read_csv('Wuzzuf_Jobs.csv')
ds.head()

#Summary of Data
ds.describe()

#Clean data or remove null and duplicated data
ds.isnull().sum()
sum(ds.duplicated())
ds.drop_duplicates(inplace =True)
sum(ds.duplicated())
ds.drop_duplicates(inplace =True)
sum(ds.duplicated())

#What are the most demanding companies for jobs?
companies = ds["Company"].value_counts()
companies
l = companies[:5].index
values = companies[:5].values
plt.pie(values ,labels =l )
plt.legend()
plt.figure(figsize=(40, 40))
plt.show();

#the Most Common job Titles
jobs =ds["Title"].value_counts()
jobs 
labels = jobs.index[:10]
values = jobs.values [:10]
plt.bar (labels ,values )
plt.title("The Most Popular Job Titles" ,fontsize=25)
plt.xlabel("Jobs" ,fontsize =20)
plt.ylabel ("Number OF Jobs" ,fontsize =20)
plt.xticks(rotation=90)
plt.show()

#The Most Popular Areas
areas =ds["Location"].value_counts()
areas
labels = areas.index[:10]
values = areas.values [:10]
plt.bar (labels ,values )
plt.title("The Most Popular Areas" ,fontsize=25)
plt.xlabel("Areas" ,fontsize =20)
plt.ylabel ("Number" ,fontsize =20)
plt.xticks(rotation=90)
plt.show()

#Find The Most Important Skills
skill =ds["Skills"].str.cat(sep =",")
skills_count =pd.Series (skill.split(",")).value_counts()
skills_count
labels = skills_count.index[:10]
values = skills_count.values [:10]
plt.bar (labels ,values )
plt.title("The Most Popular Skills" ,fontsize=25)
plt.xlabel("Skill" ,fontsize =20)
plt.ylabel ("Number" ,fontsize =20)
plt.xticks(rotation=90)
plt.show()

