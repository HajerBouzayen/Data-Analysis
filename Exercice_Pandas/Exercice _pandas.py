import pandas as pd
import matplotlib.pyplot as plt
# Créez un dataframe à partir du fichier CSV
df=pd.read_csv("DonneesHopitaux.csv",sep=',')
print(df)
df.isna().sum()
print(df)
df=df.dropna()
print(df)
#2. Ajoutez dans le dataframe une colonne nommé "duree" qui calcule la durée du #séjour à l'hôpital pour chaque personne, quelle que soit l'issue
df=df.assign(duree=df['sortie']-df['entree'])
print(df.head())
#3 Définissez la fonction n(t) qui retourne le nombre de personnes entrées
#à l'hôpital et qui y sont encore après t jours,
def n(t):
    return len (df.loc[df['duree']>t])
#4 Définissez la fonction d(t) qui retourne le nombre de personnes qui sont #décédées après t jours après leur arrivée à l'hôpital.
def d(t):
    return len(df.loc[(df['issue']==0) & (df['duree']==t)])
# 5 s(t) retourne le résultst de cet estimateur pour un t donné
def s(t):
    return (n(t)-d(t))/n(t)
#6 calculer s(t)pour t allant de 1 à 100 et enregistrez le resultat dans une #liste
T=range(1,101)
st=[]
for t in T:
    st.append(s(t))
print(st) 
# tracez la courbe s(t)
plt.plot(T,st,marker=None,color='red')
plt.show()

