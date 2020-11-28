# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:22:38 2019

@author: user
"""

#%% class-constructors

class Personel:
    
    zamorani= 6.1 #class variable
    counter=0
       
    def __init__(self,isim,soyisim,maas): #constructor: nesnenin temel özellikleri burda
            self.isim = isim
            self.soyisim = soyisim
            self.maas = maas
            self.email = isim+soyisim+"@promanage.com"
            
            Personel.counter = Personel.counter+1 #burda self.counter koymama sebebimiz metod içinden üstteki cl.vr etkilemeye çalışmamız
        
    def giveNameSurname(self):
            return self.isim + " "+self.soyisim
        
    def maasaZam(self):
            self.maas = self.maas + (self.maas*self.zamorani)/100 #zamoranina ulaşmakk için self koy
            
        
personel1 = Personel("ali","yasar",2249)
print(personel1.giveNameSurname())
print(personel1.maas)
personel1.maasaZam()
print(personel1.maas)
print(Personel.counter)
personel2 = Personel("berk","torun",1449)
print(Personel.counter)
personel3 = Personel("eren","dalk",549)
personel4 = Personel("cevat","sikidusmez",561)
Personeller = [personel1, personel2, personel3,personel4]
maxMaas=-1
index=-1
for each in Personeller:
    if(each.maas>maxMaas):
        maxMaas=each.maas
        index=each

print(maxMaas)
print(index.giveNameSurname())



