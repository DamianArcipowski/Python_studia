import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('lasy17.xlsx')
new_df = df[df.Województwo.isin(['POMORSKIE', 'OPOLSKIE', 'MAŁOPOLSKIE', 'MAZOWIECKIE'])]
df_long = pd.melt(new_df, id_vars=['Województwo'], var_name='Rok', value_name='Wartosc')
chart = sns.scatterplot(data=df_long, x='Rok', y='Wartosc', hue='Województwo', style='Województwo')
plt.savefig('test.jpg')