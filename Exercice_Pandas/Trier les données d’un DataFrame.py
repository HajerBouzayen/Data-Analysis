from pandas import DataFrame
voitures={'marque':['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
          'annee':[2015,2013,2018,2018],
          'prix':[22000,25000,27000,35000]}
df=DataFrame(voitures)
print('table non triee:\n',df)
df2=df.sort_values(by=['marque'])
print('trie croissante selon la marque:\n',df2)
df2=df.sort_values(by=['marque'],ascending=False)
print('trie décroissante selon la marque:\n',df2)
df2=df.sort_values(by=['annee','prix'])
print('trie croissante selon l\'annee et le prix:\n',df2)

