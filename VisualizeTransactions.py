import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv ('statement.csv')
df = pd.DataFrame(data, columns=["Amount"]) #Can be changed to work with your bank statements

amounts =[]
transnum = []



for i, j in df.iterrows(): 
    amounts.append(j['Amount'])
    transnum.append(i)
    
plt.plot(transnum,amounts)
plt.xlabel("Transaction Number")
plt.ylabel("Dollar Amount Credited Or Debited For A Given Transaction")

plt.show()
