# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:12:31 2019

@author: user
"""

#matploblib
#visualisation
#line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique())

print(df.info())

print(df.describe())

setosa =df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


print(setosa.describe())
print(versicolor.describe())

#%% matplotlib

import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)

#df1.plot()
#plt.show()

plt.plot(setosa.Id, setosa.PetalLengthCm, color ="red", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color ="blue", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color ="green", label="virginica")


plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

#df1.plot(grid=True, linestyle = ":")
df1.plot(grid=True, alpha=0.5) #♣saydamlık
plt.show()

#%% scatter

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm, color = "red", label="setosa-ptl L-w" )
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color = "blue", label="versicolor-ptl L-w" )
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm, color = "green", label="virginica-ptl L-w" )
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.legend()
plt.show()

#%% histogram

plt.hist(setosa.PetalLengthCm, bins=15)
plt.xlabel("PetalLengthCm")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

#%% barplot

import numpy as np

x= np.array([1,2,3,4,5,6])
y=x*2+5
plt.xlabel("x")
plt.ylabel("y")
plt.title("bar plot")
plt.show()

#%%


def crash_course(dltr):
    result = 0
    temp =1
    
    for i in range(1, dltr):
       # print("i=", i)
        temp = temp * i
        #print("temp=", temp)
        for k in range(i):
            #print("k=", k)
            result += temp
           # print("result=", result)
    return result



crash_course(4)

#%%

import numpy as np

a=[[1,2],[2,1]]
b=[[4,1],[2,2]]

np.cross(a,b)


#%%

arr=[1,2,3,4]
x = arr.pop(2)
print(x)
arr
#%%
a=5
if (a>4):
    print("tebrikler")
    
#%%
def y(x):
    global a
    a=4
    return 0

def f(a):
    a=3
    print(a)
    return a

a=5
f(a)
print(a)
y(a)
print(a)
f(a)
print(a)

#%%

import numpy as np
a=[[1,2],[2,1]]
b=[[4,1],[2,2]]

np.dot(a,b)

            
