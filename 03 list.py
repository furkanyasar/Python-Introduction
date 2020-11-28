# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:02:20 2019

@author: user
"""

#%%
malzemeler = [1,2,3,4,5,6,8,7,2,0,5,6]
malzzzz =  ["alo","kskks","ksksk"]
c=type(malzzzz)
print(c)
print(malzemeler[-1])
print(malzemeler[2:5])



malzemeler.append(7)
#malzemeler.remove(9)
malzemeler.reverse()
print(malzemeler)

#%% tuple

t=(1,2,2,3,4,5,6)
dir(t)
t.count(2)

#%% dictonary

dic= {"ali":32, "veli":45, "furkan":21}

#%% conditionals

#if else statement
a=6
b=7
if (a>b):
    print("a büyüktür b den")
elif (a==b):
    print ("eşitler aga")
else:
    print("a küçük b den")
    
liste=[1,2,2,3,4,5,6]
print("değer giriniz:" )
value =input() #düzgün çalışmıyor stringe çevirmek lazım

if value in liste:
    print("evet  {} değeri listenin içinde".format(value))
else:
    print("hayır {} değeri listenin içinde bulunmamakta".format(value))

#%% if quiz 
    inp=120
    if (inp<100):
        print("ilk yüzyıldasın")
    elif (100<=inp<200):
        print("2. yüzyıdasınl")
    else:
        print("5. yüzyıl")
        
        ## gibi gibi devam eder. ancak reis derste string dönüşümü yaparak çözdü. çok daha kısa
        ## tabi for ile de yazılabilir
        ## 100. yıl 1. yüzyıla dahildir cahil seni
        
#%% loops
        # for loop
for each in range (1,11): ##11 dahil değil
    print(each)
for each in "trabzon of rize":
    print(each)
for each in "trabzon of rize".split():
    print(each)
#%% while
    
i=0
while(i<4):
    print(i)
    i=i+1
#%%  listenin içindeki en küçük sayıyı bul
    
listeli=[1,2,3,4,5,6,-500,-601,-611,-661,-1000]
f=0
y=1
enkucuk=0
while (y<len(listeli)):
    if listeli[f]<listeli[y]:
        enkucuk=listeli[f]
    else:
        enkucuk=listeli[y]
    y+=1
    f+=1
print("listedeki en kucuk deger {} sayısıdır.".format(enkucuk))

#teeerrrtemiz çok kral yaptım beee
     
     
     
     
     
     
     
     
     
     
     
