import numpy as np
import pandas as pd
arr=np.random.randn(7,6)
df=pd.DataFrame(arr,columns=['A','B','C','D','E','F'])
print(df)
del df['C']
print('DF aprés suppression de c avc del :\n',df)
df.drop(['A','E'],axis=1,inplace=True)
