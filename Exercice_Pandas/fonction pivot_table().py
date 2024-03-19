import pandas as pd
tips=pd.read_csv('tips.csv',sep=',')
print(tips.head())
tabel=pd.pivot_table(tips,index="sex",values=['tip','total_bill','size'])
print('\n Afficher les valeurs moyennes des colonnes quantitatives  (size, tip et total_bill total_bill) regroupées  par sex(male et female\n\n',tabel)
tabel2=pd.pivot_table(tips,columns="sex",values=['tip','total_bill','size'])
print('\n afficher les valeurs moyenne de la colonne « total_bill » regroupées par sexe \n',tabel2)
print('\n \n compter  le nombre de  personnes fumeur par sexe (en ligne) et selon le temps [time, day] en colonne \n \n ')
table3=pd.pivot_table(tips.loc[tips.smoker=="Yes"],index=['sex'],values=['smoker'],columns=['time','day'],aggfunc='count')
print('******** \n',table3)
print(' On y ajoute les totaux:\n')
table4=pd.pivot_table(tips.loc[tips.smoker=="Yes"],index=['sex'],values=['smoker'],columns=['time','day'],aggfunc='count',margins=True,margins_name='Total')
print('*******\n',table4)
print('\n Afficher la pourcentage des personnes  fumeurs et non fumeurs fumeurs par sexe. \n')
def pourcentage(x):
    values=round(100*x.count()/len(tips),2)
    return str(values)+'%'
table5=pd.pivot_table(tips.loc[tips.smoker=="Yes"],index=['smoker'],values=['tip'],columns=['time','day'],aggfunc= pourcentage)
print(table5,'\n \n')
table6=pd.pivot_table(tips.loc[tips.smoker=="Yes"],index=['smoker'],values=['tip'],columns=['time','day'],aggfunc= ['count',pourcentage],margins=True,margins_name='Total')
print(table6,'\n\n')