import pandas as pd

orders = pd.read_csv('../datasets/zamowienia.csv', sep=';')

print(orders['Sprzedawca'].unique()) #pkt 1
print(orders.sort_values('Utarg', ascending=False).iloc[0:5]) #pkt 2
print(orders.groupby('Sprzedawca').size()) #pkt 3
print(orders.groupby('Kraj').size()) #pkt 4
print(orders.loc[(orders.Kraj == 'Polska') & (orders['Data zamowienia'] >= '2005-01-01') & (orders['Data zamowienia'] <= '2005-12-31')].count().iloc[0]) #pkt 5
print(orders.loc[(orders['Data zamowienia'] >= '2004-01-01') & (orders['Data zamowienia'] <= '2004-12-31')].agg({'Utarg': ['mean']})) #pkt 6
orders.loc[(orders['Data zamowienia'].str[:4] == '2004')].to_csv('zamowienia_2004.csv', sep=';')
orders.loc[(orders['Data zamowienia'].str[:4] == '2005')].to_csv('zamowienia_2005.csv', sep=';')