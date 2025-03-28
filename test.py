import pandas as pd

csv_file = "tu_archivo.csv"

# Intentar leerlo sin especificar encoding
try:
    df = pd.read_csv(csv_file)
except UnicodeDecodeError:
    # Si falla, probar con utf-16-le
    df = pd.read_csv(csv_file, encoding="utf-16-le")

print(df.head())  # Para verificar que se cargó bien

# Guardar en Excel
df.to_excel("salida.xlsx", index=False)
