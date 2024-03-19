from pandas import DataFrame
data={'color':['Green','Green','Blue','Blue','Red','Green','Red','Blue'],
       'shape':['rectangle','rectangle','square','rectangle','square','square','square','rectangle']}
df=DataFrame(data,columns=['color','shape'])
print('DtaFrame d\'origine:n',df)
#supprimer les doublons
df2=DataFrame.drop_duplicates(df)
print('Dataframe aprés suppression des doublons des lignes:\n',df2)
df3=df.drop_duplicates(subset='color',keep='last')
print('Dataframe aprés suppression des doublons de la colonne color:\n',df3)
