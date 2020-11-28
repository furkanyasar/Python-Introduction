# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:36:15 2019

@author: user
"""

import numpy as np #np olarak kullan
    
array = np.array([1,2,3,4]) #vektör, matris

a=array.reshape(2,2)

print("shape: ",a.shape)

print("dimension :", a.ndim)

array2 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3x3 matrix
print(array2)


np.zeros((3,4)) #allocation yer ayırtma

#attend metodu memory i çok yorar yer ayırtma daha makul

c=np.empty(5,6)
d=np.ones(6,8)

aasdasd= np.arange(1,96,8)

#%% math operations
angle=61
print(5+6)
print(8-5)
print(a**2)
print(np.sin(angle)) 
array3 = np.array([[1,2,3],[4,-5,6],[7,8,9]])
array4 = np.array([[1,2,-3],[4,5,6],[7,8,-9]])

#ELEMENt product
print("element: ", array3*array4)

#matrix product
print("matrix çarpımı", array3.dot(array4))
#array4.dot(a.T) #transposunu alır
print("exp: ", np.exp(angle))

randomm = np.random.random((5,5))
print(randomm.min())
print(randomm.max())
print(randomm.sum(axis=0)) #axis 0 rows dur
print(randomm.sum(axis=1)) #axis 1 columns dur

print(np.sqrt(a))
print(np.square(a))
np.add(a,a)

#%% indexing and slicing

arrayin=np.array([1,5,8,7,545]) #rand ile 1 satırlık matris oluşuyo array diye işlemiyo
print(arrayin[0])
reverse_ary=arrayin[::-1]
print(reverse_ary)

randar=np.random.random((5,5))
print(randar)
print("1. sütun ",randar[:,1])
print("1. satırın nokta adresi",randar[1,1:4])
print("son satır", randar[-1,:])

#%% shape manipulation

arrays=np.array([[1,5,8],[7,545,-4],[61,14,78]])

#flatten
d=arrays.ravel()

reshaped=d.reshape(3,3)
arrayT = reshaped.T

array6=np.array([[1,2],[3,4],[5,6]])
array6.resize(2,3)

#%% stacking arrays

arrayst= np.array([[1,2],[3,4]])
arrayst2=np.array([[-1,-2],[-5,-6]])
arraystackv= np.vstack((arrayst,arrayst2))
arraystackh=np.hstack((arrayst,arrayst2))

#%% convert copy array list || array ve list farklıdır array matrixtir

liste=[1,2,3,4,5,6]
print(type(liste))
arraylist= np.array(liste)
print(type(arraylist))
liste2 = list(array)
print(type(liste2))

copylendi = arraylist.copy() #hafızadaki değişimlerden etkilememek için kopyala
