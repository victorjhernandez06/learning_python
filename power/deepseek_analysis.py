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
## 1. CONFIGURACIÓN DE RUTAS
## ---------------------------

# Ruta completa al archivo CSV en Linux
RUTA_ARCHIVO = "data - hoja.csv"

# Verificar si el archivo existe
if not os.path.exists(RUTA_ARCHIVO):
    print(f"❌ Error: No se encontró el archivo en la ruta: {RUTA_ARCHIVO}")
    print("Por favor verifica:")
    print("1. Que la ruta es correcta")
    print("2. Que el nombre del archivo es exactamente 'data-hoja.csv'")
    print("3. Que el archivo tiene permisos de lectura")
    exit()

## ---------------------------
## 2. FUNCIÓN PARA CARGAR DATOS
## ---------------------------

def cargar_datos_linux(ruta):
    """Función adaptada para cargar datos en sistemas Linux"""
    try:
        # Leer archivo ignorando la primera columna vacía
        df = pd.read_csv(ruta, header=None, usecols=range(1,12))
        
        # Eliminar columnas completamente vacías
        df = df.dropna(axis=1, how='all')
        
        # Asignar nombres a las columnas
        columnas = ['N1', 'N2', 'N3', 'N4', 'N5', 'Powerball']
        df = df.iloc[:, :len(columnas)]  # Tomar solo las columnas necesarias
        df.columns = columnas
        
        # Eliminar filas con valores faltantes
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
        return df
    
    except Exception as e:
        print(f"❌ Error al procesar el archivo: {str(e)}")
        print("Posibles soluciones:")
        print("1. Verifica que el archivo no esté abierto en otro programa")
        print("2. Comprueba que el archivo no esté corrupto")
        print("3. Revisa que los datos tengan el formato esperado")
        return None

## ---------------------------
## 3. ANÁLISIS DE DATOS (igual que antes)
## ---------------------------

def analizar_frecuencias(df):
    """Analiza y visualiza las frecuencias de los números"""
    plt.figure(figsize=(18, 10))
    
    # Frecuencia números principales
    plt.subplot(2, 1, 1)
    all_numbers = pd.concat([df['N1'], df['N2'], df['N3'], df['N4'], df['N5']])
    freq_main = all_numbers.value_counts().sort_index()
    sns.barplot(x=freq_main.index, y=freq_main.values, palette='viridis')
    plt.title('Frecuencia de Números Principales (1-69)')
    plt.xlabel('Número')
    plt.ylabel('Frecuencia')
    
    # Frecuencia Powerball
    plt.subplot(2, 1, 2)
    freq_pb = df['Powerball'].value_counts().sort_index()
    sns.barplot(x=freq_pb.index, y=freq_pb.values, palette='magma')
    plt.title('Frecuencia de Números Powerball (1-26)')
    plt.xlabel('Powerball')
    plt.ylabel('Frecuencia')
    
    plt.tight_layout()
    
    # Guardar el gráfico en la misma ubicación que los datos
    ruta_grafico = os.path.join(os.path.dirname(RUTA_ARCHIVO), 'frecuencias.png')
    plt.savefig(ruta_grafico)
    print(f"📈 Gráfico de frecuencias guardado en: {ruta_grafico}")
    
    plt.show()
    
    return freq_main, freq_pb

## ---------------------------
## 4. MODELADO Y PREDICCIÓN (igual que antes)
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
    
    return df

def entrenar_modelos(df):
    """Entrena modelos separados para cada número"""
    modelos = {}
    caracteristicas = df.drop(['N1', 'N2', 'N3', 'N4', 'N5', 'Powerball'], axis=1)
    
    print("\n🔧 Entrenando modelos...")
    
    # Entrenar modelos para números principales
    for i in range(1, 6):
        X_train, X_test, y_train, y_test = train_test_split(
            caracteristicas, df[f'N{i}'], test_size=0.2, random_state=42)
        
        modelo = RandomForestRegressor(n_estimators=150, random_state=42)
        modelo.fit(X_train, y_train)
        
        score = modelo.score(X_test, y_test)
        print(f"Modelo N{i} - R²: {score:.4f}")
        modelos[f'N{i}'] = modelo
    
    # Entrenar modelo para Powerball
    X_train_pb, X_test_pb, y_train_pb, y_test_pb = train_test_split(
        caracteristicas, df['Powerball'], test_size=0.2, random_state=42)
    
    modelo_pb = RandomForestRegressor(n_estimators=150, random_state=42)
    modelo_pb.fit(X_train_pb, y_train_pb)
    
    pb_score = modelo_pb.score(X_test_pb, y_test_pb)
    print(f"Modelo Powerball - R²: {pb_score:.4f}")
    modelos['Powerball'] = modelo_pb
    
    return modelos

def hacer_prediccion(modelos, df):
    """Genera una predicción para el próximo sorteo"""
    ultimo_sorteo = df.drop(['N1', 'N2', 'N3', 'N4', 'N5', 'Powerball'], axis=1).iloc[-1:]
    
    pred_numeros = []
    for i in range(1, 6):
        pred = modelos[f'N{i}'].predict(ultimo_sorteo)[0]
        pred_numeros.append(max(1, min(69, round(pred))))  # Asegurar rango 1-69
    
    pred_pb = modelos['Powerball'].predict(ultimo_sorteo)[0]
    pred_pb = max(1, min(26, round(pred_pb)))  # Asegurar rango 1-26
    
    return sorted(pred_numeros), pred_pb

## ---------------------------
## 5. FUNCIÓN PRINCIPAL
## ---------------------------

def main():
    print("\n🎰 POWERBALL PREDICTOR (Linux Edition) 🎰")
    print(f"📂 Ruta del archivo: {RUTA_ARCHIVO}")
    
    # 1. Cargar datos
    datos = cargar_datos_linux(RUTA_ARCHIVO)
    if datos is None:
        return
    
    # 2. Análisis inicial
    print("\n🔍 Análisis Inicial:")
    print(datos.describe())
    
    # 3. Análisis de frecuencias
    frecuencias, frecuencias_pb = analizar_frecuencias(datos)
    
    print("\n🔥 Números principales más frecuentes:")
    print(frecuencias.sort_values(ascending=False).head(10))
    
    print("\n🔥 Powerballs más frecuentes:")
    print(frecuencias_pb.sort_values(ascending=False).head(5))
    
    # 4. Preparar datos para modelo
    datos_preparados = preparar_datos(datos)
    
    # 5. Entrenar modelos
    modelos_entrenados = entrenar_modelos(datos_preparados)
    
    # 6. Hacer predicción
    numeros_pred, pb_pred = hacer_prediccion(modelos_entrenados, datos_preparados)
    
    print("\n🎯 PREDICCIÓN PARA EL PRÓXIMO SORTEO:")
    print(f"🏆 Números principales: {numeros_pred}")
    print(f"✨ Powerball: {pb_pred}")
    
    # 7. Recomendación combinada
    print("\n💡 RECOMENDACIÓN COMBINADA (Predicción + Frecuencias):")
    nums_recomendados = list(set(numeros_pred + frecuencias.sort_values(ascending=False).head(15).index.tolist()))
    pb_recomendados = list(set([pb_pred] + frecuencias_pb.sort_values(ascending=False).head(5).index.tolist()))
    
    print(f"🔢 Números principales a considerar (Top 12): {sorted(nums_recomendados)[:12]}")
    print(f"🌟 Powerballs a considerar: {sorted(pb_recomendados)}")
    
    # Guardar resultados
    ruta_resultados = os.path.join(os.path.dirname(RUTA_ARCHIVO), 'resultados.txt')
    with open(ruta_resultados, 'w') as f:
        f.write(f"Predicción Powerball - {pd.Timestamp.now()}\n\n")
        f.write(f"Números principales: {numeros_pred}\n")
        f.write(f"Powerball: {pb_pred}\n\n")
        f.write("Recomendaciones:\n")
        f.write(f"Números: {sorted(nums_recomendados)[:12]}\n")
        f.write(f"Powerballs: {sorted(pb_recomendados)}\n")
    
    print(f"\n📝 Resultados guardados en: {ruta_resultados}")

if __name__ == "__main__":
    main()