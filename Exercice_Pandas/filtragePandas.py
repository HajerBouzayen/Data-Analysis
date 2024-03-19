from pandas import DataFrame
import pandas as pd
from numpy import nan
#création du DataFrame
Boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square',
                   'Square','Rectangle'],
         'Price': [10,15,nan,5,10,nan,15,5]
         }

df = DataFrame(Boxes)
print ('Original DataFrame: \n', df)

#Filtrage des colonnes Color et Shape
print('Filtrage des colonnes Color et Shape \n', df.loc[:, ['Color','Shape']])

# Sélection des lignes dont les valeurs de la colonne Color=Green
print ('Lignes dont la colonne Color=Green \n',df.loc[df.Color=='Green', ['Shape', 'Price']])


# Sélection des lignes dont les valeurs de la colonne Price < 15
print ('lignes dont les valeurs de la colonne Price < 15 \n',df.loc[df.Price <15])

# Sélection des lignes dont les valeurs la colonne Color=Green et la colonne Shape=Rectangle
prices= df.loc[(df.Color == 'Green') & (df.Shape == 'Rectangle'), ['Price']]
print ('lignes dont la colonne Color=Green et la colonne Shape=Rectangle \n',prices)


# Sélection des lignes dont les valeurs de la colonne Color existes dans une liste
vals = ['Blue','Red']
select_lines = df.loc[df.Color.isin(vals)]
print ('lignes dont les valeurs de la colonne Color existes dans une liste \n',select_lines)

# Sélection des lignes dont les valeurs de la colonne Price sont Not Nulles
select_lines = df.loc[df.Price.notnull()]
print ('lignes dont les valeurs de la colonne Price Not Nulles\n',select_lines)

# Sélection des lignes dont les valeurs de la colonne Price sont Nulles
select_lines = df.loc[df.Price.isnull(), ['Color', 'Shape']]
print ('lignes dont les valeurs de la colonne Price sont Nulles\n',select_lines)

