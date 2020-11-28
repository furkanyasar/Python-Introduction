
#selam ilk ders 8.10.18

#%% #burası section oluyor



print("Hello", "how are you?")

a="aliii"

b=type(a)
b

len(a)

#%%
#build in functions

celim=10.7
mecil=12

type(celim)
float(mecil)
int(celim)
round(celim)

#%% 
#20 agustos - user defined functs

def fonksiyonum(giris1, giris2): 
#tab pythonun syntaxıdır
    """
    buraya ne işe yaradığını anlatıyosun.
    tek mi çift mi?
    """
    output=(giris1*giris2+5)/8.2
    
    return output

home=fonksiyonum(8,6)

print(home)
    
#%%

#default funct

def fonsk(r,pi=3.14):
    output = 2*pi*r
    return output

#flexible
def fonsk2 (r, pi, *args):
    print(len(args))
    output = 2*pi*r
    return output


#%%
    
lamdafonkgelsunmii = lambda  x : x*x
print(lamdafonkgelsunmii(55))
