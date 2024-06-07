import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('konie.xlsx')
lodzkie = df.loc[(df.Nazwa == 'ŁÓDZKIE')]
chart = lodzkie.plot.bar(x='Rok', y='Wartość', color='yellow', width=0.25, title='Łódzkie', rot=0)
chart.legend()
chart.set_ylabel('Ludność')
plt.savefig('test.jpg')