import pandas as pd

names = pd.read_excel('../datasets/imiona.xlsx')

print(names[names['Liczba'] > 1000]) #pkt 1 
print(names[names['Imie'] == 'DAMIAN']) #pkt 2
print(names.agg({'Liczba': ['sum']})) #pkt 3
print(names.loc[(names.Rok >= 2000) & (names.Rok <= 2005)].agg({'Liczba': ['sum']})) #pkt 4
print(names.groupby('Plec').agg({'Liczba': 'sum'})) #pkt 5
print(names.loc[(names.Plec == 'M')].groupby(['Rok', 'Imie']).agg({'Liczba': 'sum'}).sort_values('Liczba', ascending=False).iloc[0:10]) #pkt 6
print(names.loc[(names.Plec == 'K')].groupby(['Rok', 'Imie']).agg({'Liczba': 'sum'}).sort_values('Liczba', ascending=False).iloc[0:10]) #pkt 6
print(names.loc[(names.Plec == 'M')].groupby(['Imie']).agg({'Liczba': 'sum'}).sort_values('Liczba', ascending=False).iloc[0]) #pkt 7
print(names.loc[(names.Plec == 'K')].groupby(['Imie']).agg({'Liczba': 'sum'}).sort_values('Liczba', ascending=False).iloc[0]) #pkt 7