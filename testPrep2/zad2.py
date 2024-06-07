import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
only_audi_dodge = df.loc[(df['Car model'] == 'audi') | (df['Car model'] == 'dodge')]
grouped = only_audi_dodge.groupby('Car model').agg({'Price': ['sum']})

chart = grouped.plot.bar(title='Audi vs Dodge')
chart.set_ylabel('Wartosc')
chart.tick_params('x', rotation=50)
plt.show()