import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

HOUSE_CSV = 'data/house_sales.csv'
df_house = pd.read_csv(HOUSE_CSV, sep='\t')

predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
outcome = 'AdjSalePrice'

print(df_house[predictors].head())
print(df_house[outcome].head())

house_lm = LinearRegression()

house_lm.fit(df_house[predictors], df_house[outcome])

print(f'Intercepto: {house_lm.intercept_:.3f}')
print('Coeficientes')

for name, coef in zip(predictors, house_lm.coef_):
    print(f' {name}: {coef}')

fitted = house_lm.predict(df_house[predictors])

RMSE = np.sqrt(mean_squared_error(df_house[outcome], fitted))
r2 = r2_score(df_house[outcome], fitted)
print(f'RMSE: {RMSE:.0f}')
print(f'rs: {r2:.4f}')

std_dev = np.std(df_house['AdjSalePrice'])
print(f'Desvio padrão de AdjSalePrice: {std_dev:.2f}')