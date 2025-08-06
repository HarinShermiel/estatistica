import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = 'data\sp500_data.csv.gz'
df = pd.read_csv(data)

#remover colunas especificas
df = df.drop(columns=['ADS'])

# Renomear coluna especifica
df = df.rename(columns={'Unnamed: 0': 'Data'})

# Transformar o campo data para datatime e settar ele como indice
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index('Data')

# Encontrar a maior e menor data
data_inicio = df.index.min()
data_fim = df.index.max()

print(f"Quantidade de variações coletadas: {len(df)}")
print (f"Período de coleta: {data_inicio.strftime("%d/%m/%Y")} à {data_fim.strftime("%d/%m/%Y")}")
print("-" *30)
# Guardar o ativo sendo usado 
ativo = 'IBM'

# Encontrar o valor máximo do ativo
maior_valor = df[ativo].max()

# Encontrar a data correspondente ao valor máximo
data_maior = df[df[ativo] == maior_valor].index[0]

print(f'valor: {maior_valor} - data: {data_maior}')
print("-" *30)

print(f"Maior variação diaria: {maior_valor:.4f}")
print(f"Ocorreu no dia: {data_maior.strftime('%d/%m/%Y')}")
print("-" *30)
# Medidas de tendencia central
media = df[ativo].mean()
mediana = df[ativo].median()
moda = df[ativo].mode()

print(f"Medidas de tendencia central para {ativo}:")
print(f"Media: {media:.4f}")
print(f"Mediana: {mediana:.4f}")

if (len(moda) > 0):
    print(f"Modas: {moda}")
else:
    print(f"O ativo {ativo} é amodal")