import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#print(ts)
#ts.plot()
#plt.show()


#data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#        'Populacja': [11190846, 1303171035, 207847528, 38010100]}
#df = pd.DataFrame(data)
#print(df)
#group = df.groupby(['Kontynent']).agg({'Populacja': 'sum'})
#print(group)
#group.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=False,
#           title='Populacja z podziałem na kontynenty')
#chart = group.plot.bar()
#chart.set_ylabel('Mld')
#chart.set_xlabel('Kontynent')
#chart.tick_params(axis='x', labelrotation=0)
#chart.legend()
#chart.set_title('Populacja z podziałem na kontynenty')
#plt.xticks(rotation=0)
#plt.savefig('wykres.png')
#plt.show()

#df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
#print(df)
#group = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
#group.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6),
#           colors=['red', 'green'])
#chart = group.plot.pie(subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6))
#plt.legend(loc='lower right')
#plt.title('Suma zamówienia dla sprzedawcy')
#plt.show()

#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#df = pd.DataFrame(ts, columns=['wartości'])
#print(df)
#df['Średnia krocząca'] = df.rolling(window=50).mean()
#df.plot()
#plt.legend()
#plt.show()