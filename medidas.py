
import pandas as pd

df = pd.read_csv('dados.csv')

df['Preço original'] = df['Preço original'].str.replace(',','.')
df['Preço original'] = df['Preço original'].str.replace('R$', '').astype(float)

# Filtrar os produtos específicos
produtos = ['Óleo de Soja ', 'Óleo de Milho Liza', 'Óleo De Canola']
df_filtrado = df[df['Nome do produto'].isin(produtos)]

# Agrupar por 'Nome do produto' e calcular as estatísticas para 'Preço original'
estatisticas = df_filtrado.groupby('Nome do produto')['Preço original'].agg(
    media='mean',
    mediana='median',
    maximo='max',
    minimo='min',
    amplitude=lambda x: x.max() - x.min()
).round(2)


print(estatisticas)
