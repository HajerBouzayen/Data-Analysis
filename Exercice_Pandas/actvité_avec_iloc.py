from pandas import DataFrame
from numpy import nan 
Boxes={'color':['Green','Green','Blue','Blue','Red','Green','Red','Blue'],
       'shape':['rectangle','rectangle','square','rectangle','square','square','square','rectangle'],
       'price':[10,15,nan,5,10,nan,15,5]}
df=DataFrame(Boxes,columns=['color','shape','price'])
print(df)
#1
print("index par colonne",'\n')
print(df.loc[:,['color','shape']],'\n')
#2 a )Color=Green 
print("affichez seulement les colonnes Shape et Price en résultat",'\n')
print(df.loc[df['color']=='Green',['price','shape']])
#b) Price < 15
print(df.loc[df['price']<15])
#c) Color =Green et Shape = Rectangle 
print("affichez seulement la colonne Price en résultat",'\n')
print(df.loc[(df['color']=='Green')&(df['shape']=='rectangle'),['price']])
#d) Color est dans cette Liste [‘Red’, ‘Blue’] 
l=['red','blue']
print(df.loc[df['color'].isin(l)])
#e
print("Les valeurs de la colonne Price ne sont pas nulles.")
print(df.loc[df['price'].notnull()])
#f
print("affichez seulement les colonnes Color et Shape en résultat")
print(df.loc[df['price'].isnull()],['color','shape'])


