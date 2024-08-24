import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('dados.csv')

df['Preço original'] = df['Preço original'].str.replace(',','.')
df['Preço original'] = df['Preço original'].str.replace('R$', '').astype(float)


# %% Gerar tabela e exportar
# Agrupando por marca e calcular estatísticas
grouped = df.groupby('Nome do produto')['Preço original']
result = grouped.agg(['mean','median','max','min', lambda x: x.max() - x.min(),'std'])

# Renomeando as colunas
result.columns = ['Média','mediana','máximo','minímo','amplitude','Desvio Padrão']

# %% Gerar gráfico
plt.plot(result, '*')
result.plot.bar(rot=0)
plt.show()