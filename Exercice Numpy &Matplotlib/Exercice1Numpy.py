import numpy as np

def MAD(M, axis=None) :
    #Calculer la médiane de la matrice le long de l'axe spécifié
    medianne =np.median(M,axis,keepdims=True)
    print(medianne)
    mad=np.abs(M-medianne)
    print(medianne)
    return np.median(mad,axis)
M=np.random.randint(10,100,size=(2,5))
#M=np.arange(20).reshape(4,5)
#claculer MAD par colonne et ligne
mad_global = MAD(M)
print("MAD global de la matrice :", mad_global)
#claculer MAD par colonne
mad_colone =MAD(M,axis=0)
print("MAD de colonne  de la matrice :", mad_colone)
mad_ligne= MAD(M,axis=1)

print("MAD de colonne  de la matrice :", mad_ligne)