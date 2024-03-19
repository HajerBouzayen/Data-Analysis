import pandas as pd

df=pd.read_csv("salaries.csv",sep=';',header=0)

print(df)
group_by_sum= df.groupby(['Country'])['Salary'].sum()
print('somme  de salaiers par payes :\n',group_by_sum)

group_by_count= df.groupby(['Country'])['Salary'].count()

print('nombre  de salaiers par payes :\n',group_by_count )
#les resultat indexéé par country
groupby_count1= df.groupby(['Country','Age'])['Salary'].mean().round(decimals=2)
print('la moyen des salaries par payes et par age:\n',groupby_count1)
groupby_count2 = df.groupby(['Country'])['Salary'].aggregate({'Moyenne':'mean','Ecart-type':'std'})
print('la moyenne et la variance des salaries par payes \n',groupby_count2)
stat=df['Salary'].describe()
print('statistique descriptive:\n',stat)
median=df['Salary'].median()
df.loc[df['Salary'].isnull(),'Salary']=median
print(df)

print(df['Salary'].fillna(median))
print(df)
print('****************************************')
print(df.groupby(['Country'])['Salary'].count().max())
print('****************************************')
print(df.groupby(['Country'])['Salary'].count().idxmax())
print(df.groupby(['Age','Country'])['Salary'].max())
print(df.describe(),'\n')
