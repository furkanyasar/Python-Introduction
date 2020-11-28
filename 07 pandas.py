# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:30:37 2019

@author: user
"""

#data frame için etkili
#csv, txt gibi file input-output
#non-value, missing data için işimizi kolaylaştırıyor
#reshape ile datayı etkili kullanabilecek hale getirebileriz
#slicing ve indexing 
#time series data analizinde yardımcı
#her şeyden önemlisi HIZLIDIR OPTİMİZEDİR

#%%
import pandas as pd

dictionary = {"NAME":["ali","kenan","hilal","ayşe","evren"],
              "AGE":[21,22,25,29,35],
              "MAAS":[2249,1461,8951,4756,2354]}


dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head() #bastan 5 gösterir
tail = dataFrame1.tail() #sondan 5 gösterir
#tail = dataFrame1.tail(7) sondan 7 gösterir

#%% pandas basc methods

print(dataFrame1.columns) #filtreleme için lazım
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe()) #min max mean std 

#%% slicing indexng

print(dataFrame1["NAME"])

dataFrame1["yeni_feature"] = [1,2,3,-6,8]

print(dataFrame1.loc[:,"AGE"])  #LOCAtion EN ÇOK KULLANILAN FONKS DARA SCIENCE DE
print(dataFrame1.loc[:3,"AGE"]) #PANDASTA son sayı  inclusivedir
print(dataFrame1.loc[:3,"NAME":"AGE"])
print(dataFrame1.loc[:3,["NAME","MAAS"]])
print(dataFrame1.loc[::-1,:])
print(dataFrame1.loc[:,"NAME"])
print(dataFrame1.iloc[:,1])
print(dataFrame1.loc[:,"MAAS"])

#%% filtering

filtre1 = dataFrame1.MAAS > 2005


filtrelenmis_data=dataFrame1[filtre1]

filtre2 = dataFrame1.AGE > 25

dataFrame1[filtre1 & filtre2]

#%% list comprehension

import numpy as np

ortalama_maas= dataFrame1.MAAS.mean()
#ortalama_maas_np = mean(dataFrame1.MAAS) numpy ile

dataFrame1["maas_seviyesi"] = ["düsük" if ortalama_maas > each else "yüksek" for each in dataFrame1.MAAS]

#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("düsük")
#    else:
#        print("yüksek")

dataFrame1.columns

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

#boşluğu alıp yerine _ koyacak kod

#%% drop & concenating data


dataFrame1.drop(["yeni_feature"], axis=1,  inplace =True) 

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#verticala
data_concat = pd.concat([data1,data2],axis=0)

#horizontal
maas=dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)

#%% transmitting data

dataFrame1["list_comp"] = [each^2 for each in dataFrame1.age]

#apply

def multiply(age):
    return age^2

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)

    
    

