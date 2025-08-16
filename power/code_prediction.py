import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Leer el archivo CSV
archivo_csv = "data - hoja.csv"
df = pd.read_csv(archivo_csv, header=None)

# 2. Suponemos que las columnas relevantes son estas
# Renombrar columnas para facilidad
df = df[[1, 2, 3, 4, 5, 7]]
df.columns = ['N1', 'N2', 'N3', 'N4', 'N5', 'PB']

# 3. Crear features X y etiquetas y (usaremos ventana deslizante)
def crear_dataset(df):
    X, y_main, y_pb = [], [], []

    for i in range(len(df) - 1):
        # Usamos la combinación actual para predecir la siguiente
        X.append(df.iloc[i].values)
        y_main.append(df.iloc[i + 1][['N1', 'N2', 'N3', 'N4', 'N5']].values)
        y_pb.append(df.iloc[i + 1]['PB'])

    return np.array(X), np.array(y_main), np.array(y_pb)

X, y_main, y_pb = crear_dataset(df)

# 4. Entrenar un modelo para cada uno de los 5 números principales
modelos_main = []
for i in range(5):
    y_i = y_main[:, i]
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y_i)
    modelos_main.append(modelo)

# 5. Modelo para el número Powerball
modelo_pb = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_pb.fit(X, y_pb)

# 6. Predecir usando el último registro disponible
entrada = df.iloc[-1].values.reshape(1, -1)

predicciones_main = [modelo.predict(entrada)[0] for modelo in modelos_main]
prediccion_pb = modelo_pb.predict(entrada)[0]

# 7. Mostrar resultados
print("🎯 Predicción Powerball:")
print("Números principales:", sorted(predicciones_main))
print("Número Powerball:", prediccion_pb)
print ("fin de programa")