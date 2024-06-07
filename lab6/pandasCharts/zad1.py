import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../datasets/imiona.xlsx')
years = df['Rok'].unique()
amount = df.groupby('Rok').agg({'Liczba': ['sum']})
chart = amount.plot()
