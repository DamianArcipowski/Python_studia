import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.') 

gas = 0
diesel = 0

for i in df['Fuel-type']:
    if i == 'gas':
        gas += 1
    else:
        diesel += 1
        
types = ['gas', 'diesel']
percents = [round(gas / 193, 2), round(diesel / 193, 2)]

fig, ax = plt.subplots()
plt.title('Gas vs Diesel')
ax.pie(percents, labels=types, autopct='%1.1f%%', textprops={'fontsize': 14})
fig.legend()
plt.show()