import pandas as pd
archivo_csv = "operaciones_transformadas.csv"
try:
    data = pd.read_csv(archivo_csv)
    archivo_excel = "reporte_logistica.xlsx"
    data.to_excel(archivo_excel, index=False)
    print(f"Reporte generado correctamente: {archivo_excel}")
except Exception as e:
    print(f"Error al exportar los datos: {e}")
