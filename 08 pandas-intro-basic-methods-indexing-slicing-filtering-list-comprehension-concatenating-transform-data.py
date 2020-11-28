# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:12:16 2018

@author: user
"""

# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedbilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)


head = dataFrame1.head()
tail = dataFrame1.tail()

# %%
# pandas basic method

print(dataFrame1.columns)

print(dataFrame1.info())

print(dataFrame1.dtypes)

print(dataFrame1.describe())  # numeric feature = columns (age,maas)

# %% indexing and slicing


print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:, "AGE"])

print(dataFrame1.loc[:3, "AGE"])

print(dataFrame1.loc[:3, "AGE":"NAME"])

print(dataFrame1.loc[:3, ["AGE","NAME"]])

print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"NAME"])

print(dataFrame1.loc[:,"NAME"])

print(dataFrame1.iloc[:,2])

# %% filtering

filtre1 = dataFrame1.MAAS > 200





















