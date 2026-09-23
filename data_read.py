import pandas as pd
archivo_entrada = "operaciones_logistica.csv"
try:
    data = pd.read_csv(archivo_entrada)
    data.to_csv("operaciones.csv", index=False, encoding="utf-8-sig")
    print(f"Datos leídos correctamente: {len(data)} registros")
except Exception as e:
    print(f"Error al leer los datos: {e}")
