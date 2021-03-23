import os
import pandas as pd
cwd = os.path.relpath("Bank 2")
files = os.listdir(cwd)  
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel("Bank 2\{0}".format(file)), ignore_index=True) 
df.head() 
df.to_excel('Data.xlsx')