import pandas as pd 
from openpyxl import load_workbook
writer=pd.ExcelWriter('mydata1_exp.xlsx',engine='openpyxl')
writer.book=load_workbook('mydata_exp.xlsx')
dataf=pd.read_csv('etudiant.csv',sep=';',header=0,encoding='latin-l')
dataf.to_excel(writer,"Nombres",index=None)
writer.save()
valeurs={'dizaines':[10,20,30,40],'centaines':[100,200,300,400],'milliers':[1000,2000,3000,4000]}
dataf=pd.DataFrame(valeurs)
print(dataf)