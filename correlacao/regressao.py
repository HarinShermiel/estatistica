import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# pip install scikit-learn
from sklearn.linear_model import LinearRegression

EXPOSICAO_ALGODAO = 'data/LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
plt.show()


prefictors = ['Exposure']
outcome = 'PEFR'

model = LinearRegression()

model.fit(dataframe[prefictors], dataframe[outcome])

print(f'Intercept: {model.intercept_:.3f}')

print(f'Coeficiente Angular: {model.coef_[0]}')

fig, (reg) = plt.subplots(1, 1, figsize=(4, 4))

reg = sns.regplot(x = 'Exposure', y = 'PEFR', data = dataframe, ax = reg)
plt.tight_layout()
plt.show()