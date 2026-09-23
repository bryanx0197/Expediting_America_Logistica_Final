import pandas as pd
archivo_csv = "operaciones.csv"
try:
    data = pd.read_csv(archivo_csv)
    data["Fecha_Programada"] = pd.to_datetime(data["Fecha_Programada"], dayfirst=True)
    data["Fecha_Llegada"] = pd.to_datetime(data["Fecha_Llegada"], dayfirst=True)
    data["Dias_Retraso"] = (data["Fecha_Llegada"] - data["Fecha_Programada"]).dt.days.clip(lower=0)
    data["Estado"] = data["Dias_Retraso"].apply(lambda x: "A tiempo" if x == 0 else "Retrasado")
    data = data.sort_values(by=["Estado", "Proveedor", "Fecha_Programada"])
    data["Fecha_Programada"] = data["Fecha_Programada"].dt.strftime("%d/%m/%Y")
    data["Fecha_Llegada"] = data["Fecha_Llegada"].dt.strftime("%d/%m/%Y")
    data.to_csv("operaciones_transformadas.csv", index=False, encoding="utf-8-sig")
    print("Transformación completada correctamente.")
    print(f"Registros procesados: {len(data)}")
    print(f"Operaciones retrasadas: {(data['Dias_Retraso'] > 0).sum()}")
    print(f"Operaciones a tiempo: {(data['Dias_Retraso'] == 0).sum()}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")
