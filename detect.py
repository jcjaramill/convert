import chardet
import pandas as pd

with open("stations.csv", "rb") as f:
    result = chardet.detect(f.read())

print(result["encoding"])  # Muestra la codificación detectada

csv_file = "stations.csv"  # Nombre del archivo CSV
#csv_file = "CSReport.csv"  # Nombre del archivo CSV


# Intentar leerlo sin especificar encoding
try:
    df = pd.read_csv(csv_file)
except UnicodeDecodeError:
    # Si falla, probar con utf-16-le
    df = pd.read_csv(csv_file, encoding="utf-16-le")

print(df.head(5))  # Para verificar que se cargó bien