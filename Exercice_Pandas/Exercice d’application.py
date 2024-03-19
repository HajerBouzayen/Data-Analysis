import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('NY.txt', sep=',')
print(df.head())
df.columns = ['State', 'Sexe', 'Year', 'Name', 'NbBirths']
print(df.head())
# supprimer la colonne à l'index 0, c'est-à-dir State
df.drop(['State'], axis=1, inplace=True)
# del df['state]
print(df.head())
# ◦ Affichez les 10 premiers enregistrements du dataframe
print(df.head(10))
# Afficher les 10 premiers prénoms les plus utilisés depuis l'année 2010.

def top10():
    df_2010 = df.loc[df['Year'] >= 2010]
    df_top = df_2010.groupby(['Name'])['NbBirths'].sum().reset_index()  # Reset index to include 'Name'
    df_top = df_top.sort_values(by='NbBirths', ascending=False)
    print(df_top.head(10))

    plt.pie(df_top.head(10)['NbBirths'], labels=df_top.head(10)['Name'], autopct='%1.1f%%')
    plt.title('Top 10 Names ')
    plt.axis('equal')
    plt.show()


print(" premiers prénoms les plus utilisés depuis l'année 2010 \n \n",top10())


def PourcentageFG():
    year = int(input('donner une année: '))
    df2 = df.loc[df.Year == year]
    table2 = pd.crosstab(index=df2['Sexe'], columns='Nb',
                         values=df2['NbBirths'], aggfunc='sum')*100/df2['NbBirths'].sum()
    print(table2)


print(" le pourcentage des filles et des garçons nés pendant une année donnée.\n\n ",PourcentageFG())


def NbEnfant():
    prenom = input("donner prenom :")
    df3 = df.loc[(df.Name == prenom) & (df.Year >= 2010)]
    resultat = pd.crosstab(index=df3['Year'], columns='nombre enfant',
                           values=df3['NbBirths'], aggfunc='sum', colnames=['année/ nb enfant'])
    print(resultat)
 

print("le nombre d'enfants  par année portant un prénom donnée \n\n",NbEnfant())


def graphe():
    prenom = input("donner prenom :")

    df_prenom = df.loc[(df['Name'] == prenom) & (
        df['Year'].between(2010, 2018))]
    print(df_prenom)
    resultat = df_prenom.groupby(['Year'])['NbBirths'].sum()
    plt.bar(resultat.index, resultat)
    plt.xlabel("Année")
    plt.ylabel("Nombre d'enfants")
    plt.title("Nombre d'enfants portant le prénom " + prenom)
    plt.show()


print("le nombre d'enfants portant un prénom donnée depuis 2010 jusqu'à 2018. \n \n",graphe())


def intervalle():

    borneInf = int(input('Saisir une année de début : '))
    borneSup = int(input('Saisir une année de fin: '))

    df_interval = df.loc[df['Year'].between(borneInf, borneSup)]

    result = df_interval.groupby('Year')['NbBirths'].idxmax()
    #result=df_interval.pivot_table(index=['Year'],values=['NbBirths'],aggfunc='max')
    nom_plus_utlisé =df_interval.loc[result,['Year', 'Name', 'NbBirths']]
    print(nom_plus_utlisé)


print("quel est le prénom le plus utilisé durant chaque année",intervalle())




def Anne():
    d = int(input('donner une anne :'))
    df_anne = df.loc[df['Year'] == d]

    result = df_anne.groupby(['Sexe'])['NbBirths'].sum().reset_index()
    print(result)

    # Tracer un graphique à barres
    plt.bar(result['Sexe'], result['NbBirths'])
    plt.xlabel('Sexe')
    plt.ylabel('Nombre d\'enfants')
    plt.title(f'Nombre d\'enfants nés en {d} par sexe')
    plt.show()

# Appeler la fonction
print(' le prénom le plus utilisé selon le sexe ',Anne())


