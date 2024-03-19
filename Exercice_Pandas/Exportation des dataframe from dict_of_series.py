import pandas as pd

d={'name':pd.Series(['tom','james','ricky','vin','steve','smith','jack','lee','david','gasper','betina','andres']),
   'age':pd.Series([24,25,34,30,23,34,54,40,51,23,46,51]),
   'rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
   }
df=pd.DataFrame(d)
print(df)

y=pd.read_csv("etudiants.csv",sep=';',header=0,encoding='Latin-1')
y.columns=['prenom','matiere','moyenne']
print(y)
'''z=pd.read_excel('etudiants.csv',sheet_name="Nom",header=0,usecols="A:C")
print(z)'''

