# Este código te ayuda a analizar la frecuencia de los números de la lotería Powerball
# Basado en un archivo CSV con resultados históricos.

# Importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# --- Configuración y Carga de Datos ---
# Asegúrate de que tu archivo CSV se llama 'data - hoja.csv' y está en el mismo directorio
# El archivo debe tener columnas para los 5 números principales y una para la Powerball.
# Basándonos en tu error, las columnas parecen tener nombres numéricos y 'Unnamed'.

def cargar_datos(nombre_archivo):
    """
    Carga los datos del archivo CSV, lo convierte en un DataFrame de pandas
    y muestra las primeras filas.
    """
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
        # Creamos un DataFrame de ejemplo para que el código no falle si el archivo no existe
        print("Creando datos de ejemplo para demostración.")
        data_ejemplo = {
            'draw_date': pd.to_datetime(['2024-01-01', '2024-01-04', '2024-01-08']),
            '1': [10, 15, 20],
            '6': [25, 30, 35],
            '7': [40, 45, 50],
            'Unnamed: 8': [55, 60, 65],
            'Unnamed: 9': [70, 75, 80],
            'Unnamed: 10': [1, 5, 10]
        }
        df = pd.DataFrame(data_ejemplo)
        return df

    try:
        df = pd.read_csv(nombre_archivo)
        print("Datos cargados correctamente. Mostrando las primeras filas:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
        return None


# --- Análisis de Frecuencia ---
def analizar_frecuencia(df):
    """
    Calcula la frecuencia de aparición de cada número y de la powerball.
    """
    if df is None:
        return None, None

    # Las columnas se han ajustado según el error que has compartido.
    # Por favor, verifica que estos nombres de columna sean correctos y ajusta si es necesario.
    columnas_numeros = ['1', '6', '7', 'Unnamed: 8', 'Unnamed: 9']
    powerball_column = 'Unnamed: 10'

    # Concatenamos todas las columnas de números en una sola Serie
    # `pd.concat` es útil para unir datos de varias columnas en una
    numeros = pd.concat([df[columna] for columna in columnas_numeros])

    # `value_counts()` cuenta cuántas veces aparece cada valor único
    frecuencia_numeros = numeros.value_counts().reset_index()
    frecuencia_numeros.columns = ['numero', 'frecuencia']

    # Hacemos lo mismo para la Powerball
    frecuencia_powerball = df[powerball_column].value_counts().reset_index()
    frecuencia_powerball.columns = ['numero', 'frecuencia']

    # Ordenamos de mayor a menor frecuencia
    frecuencia_numeros = frecuencia_numeros.sort_values(by='frecuencia', ascending=False)
    frecuencia_powerball = frecuencia_powerball.sort_values(by='frecuencia', ascending=False)

    print("\n--- Números más frecuentes (principales) ---")
    print(frecuencia_numeros.head(10))

    print("\n--- Powerballs más frecuentes ---")
    print(frecuencia_powerball.head(10))

    return frecuencia_numeros, frecuencia_powerball


# --- Visualización de Datos ---
def visualizar_frecuencia(frecuencia_numeros, frecuencia_powerball):
    """
    Crea gráficos de barras para visualizar las frecuencias.
    """
    if frecuencia_numeros is None or frecuencia_powerball is None:
        return

    # Gráfico de barras para los números principales
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(15, 6))
    sns.barplot(x='numero', y='frecuencia', data=frecuencia_numeros.head(20), palette='viridis')
    plt.title('Top 20 de los números de Powerball más frecuentes', fontsize=16)
    plt.xlabel('Número', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()  # Asegura que las etiquetas no se corten
    plt.show()

    # Gráfico de barras para la Powerball
    plt.figure(figsize=(10, 5))
    sns.barplot(x='numero', y='frecuencia', data=frecuencia_powerball, palette='mako')
    plt.title('Frecuencia de la Powerball', fontsize=16)
    plt.xlabel('Número', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.tight_layout()
    plt.show()


# --- Ejecución Principal ---
def main():
    """
    Función principal que orquesta el flujo de trabajo.
    """
    nombre_archivo_csv = 'data - hoja.csv'
    df = cargar_datos(nombre_archivo_csv)
    if df is not None:
        frecuencia_nums, frecuencia_pb = analizar_frecuencia(df)
        visualizar_frecuencia(frecuencia_nums, frecuencia_pb)


if __name__ == '__main__':
    main()
