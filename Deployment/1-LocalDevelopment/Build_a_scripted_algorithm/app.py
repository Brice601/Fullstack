import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Charger les données
df = pd.read_csv('california_housing_market.csv')

# Séparer features (X) et target (y)
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

# Split train/test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Évaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"R² Score: {r2:.4f}")
print(f"\nLes 5 premières prédictions:")
print(f"Réel: {y_test.values[:5]}")
print(f"Prédit: {y_pred[:5]}")