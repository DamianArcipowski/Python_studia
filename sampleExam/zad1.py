import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Rok': [2017, 2018, 2019, 2020],
    'Mężczyźni': [18.5, 18.5, 18.5, 18.3],
    'Kobiety': [19.8, 19.8, 19.8, 19.6]
}

df = pd.DataFrame(data)

chart = df.plot(x='Rok', title='Liczba ludności w Polsce według płci')
chart.set_xticks(df.Rok)
chart.set_yticks([18, 19, 20])
chart.set_yticklabels(['18 mln', '19 mln', '20 mln'])
chart.set_xlabel(None)
chart.legend(loc='right')
plt.savefig('test.pdf')