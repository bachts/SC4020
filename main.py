import numpy as np 
import pandas as pd 
import time
from mlxtend.frequent_patterns import apriori, association_rules 

path = 'online+retail/Online Retail.xlsx'
start = time.time()
df = pd.read_excel(path)

df.to_pickle()
print(time.time()-start)
print(df.head())