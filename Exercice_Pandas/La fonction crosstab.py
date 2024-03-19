import pandas as pd
import matplotlib.pyplot as plt
tips=pd.read_csv('tips.csv',sep=',')
print(tips.head())
print('\n \n***** La fonction crosstab()******* \n \n')
tabel1=pd.crosstab(tips['sex'],tips['time'])
print(tabel1)
print('\n \n afficher la pourcentage de clients masculins et féminins pour le déjeuner et le dîner\n \n')
tbabl2=pd.crosstab(tips['sex'],tips['time'],margins=True,margins_name="Total clients")
print(tbabl2,'\n')
print('on normalize les lignes et les colonnes\n\n')
tbabl3=pd.crosstab(tips['sex'],tips['time'],margins=True,margins_name="Total clients",normalize=True)
print(tbabl3,'\n')
print('')
tbabl4=round(pd.crosstab(tips['sex'],tips['time'],margins=True,margins_name="Total clients",normalize=True)*100,2)
print(tbabl4,'\n')
tbabl5=pd.crosstab(index=tips['sex'],columns=tips['time'],values=tips['tip'],aggfunc='mean',rownames=['Gender'],colnames=['Time'])
print(tbabl5,'\n')
tbabl6=pd.crosstab(index=tips['sex'],columns=['count'],colnames=['EEffectif'])
print(tbabl6,'\n')

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center', va='center_baseline', color='red', alpha=0.9)

plt.bar(tbabl6.index, tbabl6['count'], color='blue')    
plt.xlabel('nombre d observations')
plt.title("diagramme en baton ")

addlabels(tbabl6.index, tbabl6['count'])
plt.show()
table7=pd.crosstab(tips['day'],tips['sex'])
print(" diagramme en bâton selon deux variables")
table7.plot.bar(width=0.75)
def addMultilabels(x,y,color,ha,va):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],ha=ha,va=va,bbox=dict(facecolor=color,alpha=0.9))
addMultilabels(table7.index, table7['Female'],'blue','right','top')
addMultilabels(table7.index, table7['Male'],'red','left','bottom')
plt.show()
    