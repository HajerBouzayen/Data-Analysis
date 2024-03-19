import numpy as np
import Exercice1Numpy as ex
M=np.random.randint(10,100,size=(2,5))

#claculer MAD par colonne et ligne
mad_global = ex.MAD(M)
print("MAD global de la matrice :", mad_global)
#claculer MAD par colonne
mad_colone =ex.MAD(M,axis=0)
print("MAD de colonne  de la matrice :", mad_colone)
mad_ligne= ex.MAD(M,axis=1)

print("MAD de colonne  de la matrice :", mad_ligne)