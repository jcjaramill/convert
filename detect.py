import chardet

with open("CSV ESTU_L6.csv", "rb") as f:
    result = chardet.detect(f.read())

print(result["encoding"])  # Muestra la codificación detectada