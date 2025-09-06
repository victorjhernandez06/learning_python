import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurar estilo de visualización
plt.style.use('ggplot')
pd.set_option('display.max_columns', None)

## ---------------------------
## 1. CONFIGURACIÓN DE RUTAS.
## ---------------------------

# Ruta completa al archivo CSV
RUTA_ARCHIVO = "F:/Python25/LearningPython/power/data - hoja.csv"

# Verificar si el archivo existe
if not os.path.exists(RUTA_ARCHIVO):
    print(f"❌ Error: No se encontró el archivo en la ruta: {RUTA_ARCHIVO}")
    print("Por favor verifica:")
    print("1. Que la ruta es correcta")
    print("2. Que el nombre del archivo es exactamente 'data - hoja.csv'")
    print("3. Que el archivo tiene permisos de lectura")
    exit()


## ---------------------------
## 2. FUNCIÓN PARA CARGAR DATOS
## ---------------------------

def cargar_datos(ruta):
    """Función para cargar y procesar los datos del Powerball"""
    try:
        # Leer el archivo CSV
        df = pd.read_csv(ruta, header=None)

        # Mostrar información inicial para debugging
        print(f"Forma original del DataFrame: {df.shape}")
        print(f"Columnas originales: {df.columns.tolist()}")
        print("\nPrimeras 5 filas del archivo original:")
        print(df.head())

        # Eliminar la primera columna vacía (índice 0) y la última columna vacía
        # Tu archivo tiene 8 columnas: [0,1,2,3,4,5,6,7]
        # Las columnas 1-5 son los números, columna 6 está vacía, columna 7 es el Powerball
        df = df.iloc[:, [1, 2, 3, 4, 5, 7]]  # Seleccionar solo las columnas relevantes

        # Renombrar las columnas
        df.columns = ['N1', 'N2', 'N3', 'N4', 'N5', 'Powerball']

        # Eliminar filas con valores NaN
        df = df.dropna()

        # Convertir a enteros
        df = df.astype(int)

        # Filtrar valores dentro de los rangos correctos
        df = df[(df['Powerball'] >= 1) & (df['Powerball'] <= 26)]
        for i in range(1, 6):
            df = df[(df[f'N{i}'] >= 1) & (df[f'N{i}'] <= 69)]

        # Eliminar duplicados
        df = df.drop_duplicates()

        print(f"✅ Datos cargados correctamente desde: {ruta}")
        print(f"📊 Total de sorteos analizados: {len(df)}")
        print(f"📋 Columnas finales: {df.columns.tolist()}")
        print("\nPrimeras 5 filas procesadas:")
        print(df.head())

        return df

    except Exception as e:
        print(f"❌ Error al procesar el archivo: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


## ---------------------------
## 3. ANÁLISIS DE FRECUENCIAS
## ---------------------------

def analizar_frecuencias(df):
    """Analiza y visualiza las frecuencias de los números"""
    plt.figure(figsize=(18, 10))

    # Frecuencia números principales
    plt.subplot(2, 1, 1)
    all_numbers = pd.concat([df['N1'], df['N2'], df['N3'], df['N4'], df['N5']])
    freq_main = all_numbers.value_counts().sort_index()

    # Crear gráfico de barras con menos barras para mejor visualización
    plt.bar(freq_main.index, freq_main.values, color='skyblue', alpha=0.7)
    plt.title('Frecuencia de Números Principales (1-69)')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)

    # Frecuencia Powerball
    plt.subplot(2, 1, 2)
    freq_pb = df['Powerball'].value_counts().sort_index()
    plt.bar(freq_pb.index, freq_pb.values, color='lightcoral', alpha=0.7)
    plt.title('Frecuencia de Números Powerball (1-26)')
    plt.xlabel('Powerball')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    # Guardar el gráfico
    ruta_grafico = os.path.join(os.path.dirname(RUTA_ARCHIVO), 'frecuencias_powerball.png')
    plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
    print(f"📈 Gráfico de frecuencias guardado en: {ruta_grafico}")

    plt.show()

    return freq_main, freq_pb


## ---------------------------
## 4. PREPARACIÓN DE DATOS PARA ML
## ---------------------------

def preparar_datos(df):
    """Prepara los datos para el modelo de machine learning"""
    # Calcular frecuencias
    all_numbers = pd.concat([df['N1'], df['N2'], df['N3'], df['N4'], df['N5']])
    number_freq = all_numbers.value_counts().to_dict()
    pb_freq = df['Powerball'].value_counts().to_dict()

    # Crear características adicionales
    for i in range(1, 6):
        df[f'N{i}_freq'] = df[f'N{i}'].map(number_freq)

    df['PB_freq'] = df['Powerball'].map(pb_freq)
    df['Suma_Numeros'] = df[['N1', 'N2', 'N3', 'N4', 'N5']].sum(axis=1)
    df['Promedio_Numeros'] = df[['N1', 'N2', 'N3', 'N4', 'N5']].mean(axis=1)

    # Características de tendencia (últimos 10 sorteos)
    for i in range(1, 6):
        df[f'N{i}_rolling_mean'] = df[f'N{i}'].rolling(window=10, min_periods=1).mean()
        df[f'N{i}_rolling_std'] = df[f'N{i}'].rolling(window=10, min_periods=1).std()

    df['PB_rolling_mean'] = df['Powerball'].rolling(window=10, min_periods=1).mean()

    # Eliminar filas con NaN de las características de rolling
    df = df.dropna()

    print(f"📊 Datos preparados. Forma: {df.shape}")
    return df


## ---------------------------
## 5. ENTRENAMIENTO DE MODELOS
## ---------------------------

def entrenar_modelos(df):
    """Entrena modelos separados para cada número"""
    modelos = {}

    # Seleccionar características (excluir las columnas originales)
    caracteristicas = [col for col in df.columns if col not in ['N1', 'N2', 'N3', 'N4', 'N5', 'Powerball']]
    X = df[caracteristicas]

    print(f"\n🔧 Entrenando modelos con {len(caracteristicas)} características...")

    # Entrenar modelos para números principales
    for i in range(1, 6):
        y = df[f'N{i}']

        # Dividir datos (80% entrenamiento, 20% prueba)
        split_index = int(len(X) * 0.8)
        X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
        y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

        modelo = RandomForestRegressor(n_estimators=50, random_state=42)
        modelo.fit(X_train, y_train)

        score = modelo.score(X_test, y_test)
        print(f"Modelo N{i} - R²: {score:.4f}")
        modelos[f'N{i}'] = modelo

    # Entrenar modelo para Powerball
    y_pb = df['Powerball']
    split_index_pb = int(len(X) * 0.8)
    X_train_pb, X_test_pb = X.iloc[:split_index_pb], X.iloc[split_index_pb:]
    y_train_pb, y_test_pb = y_pb.iloc[:split_index_pb], y_pb.iloc[split_index_pb:]

    modelo_pb = RandomForestRegressor(n_estimators=50, random_state=42)
    modelo_pb.fit(X_train_pb, y_train_pb)

    pb_score = modelo_pb.score(X_test_pb, y_test_pb)
    print(f"Modelo Powerball - R²: {pb_score:.4f}")
    modelos['Powerball'] = modelo_pb

    return modelos, caracteristicas


## ---------------------------
## 6. PREDICCIÓN
## ---------------------------

def hacer_prediccion(modelos, df, caracteristicas):
    """Genera una predicción para el próximo sorteo"""
    # Usar el último sorteo para la predicción
    ultimo_sorteo = df[caracteristicas].iloc[-1:]

    pred_numeros = []
    for i in range(1, 6):
        pred = modelos[f'N{i}'].predict(ultimo_sorteo)[0]
        # Redondear y asegurar que esté en el rango correcto
        pred_rounded = max(1, min(69, round(pred)))
        pred_numeros.append(pred_rounded)

    pred_pb = modelos['Powerball'].predict(ultimo_sorteo)[0]
    pred_pb = max(1, min(26, round(pred_pb)))

    return sorted(pred_numeros), pred_pb


## ---------------------------
## 7. FUNCIÓN PRINCIPAL
## ---------------------------

def main():
    print("\n🎰 POWERBALL PREDICTOR 🎰")
    print(f"📂 Ruta del archivo: {RUTA_ARCHIVO}")

    # 1. Cargar datos
    datos = cargar_datos(RUTA_ARCHIVO)
    if datos is None:
        return

    # 2. Análisis inicial
    print("\n🔍 Análisis Inicial:")
    print(datos.describe())

    # 3. Análisis de frecuencias
    print("\n📊 Analizando frecuencias...")
    frecuencias, frecuencias_pb = analizar_frecuencias(datos)

    print("\n🔥 Números principales más frecuentes:")
    print(frecuencias.sort_values(ascending=False).head(10))

    print("\n🔥 Powerballs más frecuentes:")
    print(frecuencias_pb.sort_values(ascending=False).head(5))

    # 4. Preparar datos para modelo
    datos_preparados = preparar_datos(datos)

    # 5. Entrenar modelos
    modelos_entrenados, features = entrenar_modelos(datos_preparados)

    # 6. Hacer predicción
    numeros_pred, pb_pred = hacer_prediccion(modelos_entrenados, datos_preparados, features)

    print("\n" + "=" * 50)
    print("🎯 PREDICCIÓN PARA EL PRÓXIMO SORTEO:")
    print("=" * 50)
    print(f"🏆 Números principales: {numeros_pred}")
    print(f"✨ Powerball: {pb_pred}")
    print("=" * 50)

    # 7. Recomendación basada en frecuencias
    print("\n💡 RECOMENDACIÓN BASADA EN FRECUENCIAS:")
    nums_frecuentes = frecuencias.sort_values(ascending=False).head(15).index.tolist()
    pb_frecuentes = frecuencias_pb.sort_values(ascending=False).head(5).index.tolist()

    print(f"🔢 Números principales frecuentes: {sorted(nums_frecuentes)}")
    print(f"🌟 Powerballs frecuentes: {sorted(pb_frecuentes)}")

    # 8. Combinación de predicción y frecuencias
    print("\n💡 RECOMENDACIÓN COMBINADA:")
    nums_combinados = list(set(numeros_pred + nums_frecuentes[:8]))
    pb_combinados = list(set([pb_pred] + pb_frecuentes[:3]))

    print(f"🔢 Números a considerar: {sorted(nums_combinados)}")
    print(f"🌟 Powerballs a considerar: {sorted(pb_combinados)}")

    # Guardar resultados
    ruta_resultados = os.path.join(os.path.dirname(RUTA_ARCHIVO), 'prediccion_powerball.txt')
    with open(ruta_resultados, 'w', encoding='utf-8') as f:
        f.write(f"PREDICCIÓN POWERBALL - {pd.Timestamp.now()}\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"🗓️  Total de sorteos analizados: {len(datos)}\n\n")

        f.write("🎯 PREDICCIÓN DEL MODELO:\n")
        f.write(f"Números principales: {numeros_pred}\n")
        f.write(f"Powerball: {pb_pred}\n\n")

        f.write("📊 ANÁLISIS DE FRECUENCIAS:\n")
        f.write(f"Números más frecuentes: {sorted(nums_frecuentes)}\n")
        f.write(f"Powerballs más frecuentes: {sorted(pb_frecuentes)}\n\n")

        f.write("💡 RECOMENDACIONES FINALES:\n")
        f.write(f"Números a jugar: {sorted(nums_combinados)}\n")
        f.write(f"Powerballs a jugar: {sorted(pb_combinados)}\n\n")

        f.write("⚠️  NOTA: Esto es solo una predicción estadística.\n")
        f.write("Los juegos de azar deben jugarse con responsabilidad.\n")

    print(f"\n📝 Resultados guardados en: {ruta_resultados}")
    print("\n¡Buena suerte! 🍀")


if __name__ == "__main__":
    main()