import pandas as pd
import numpy as np
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:,3:] 
df[df['Length of Membership']>3]
#print(df.columns)
df.to_csv(os.path.join('data','customer.csv'))
