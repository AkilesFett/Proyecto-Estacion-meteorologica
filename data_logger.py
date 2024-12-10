from config import CSV_FILENAME

# Función para inicializar el archivo CSV si no existe
def inicializar_csv():
    """Crea el archivo CSV con encabezados si no existe."""
    try:
        with open(CSV_FILENAME, 'r') as file:
            print(f"Archivo {CSV_FILENAME} ya existe.")
    except OSError:
        with open(CSV_FILENAME, 'w') as file:
            file.write("timestamp,temperatura,presion,humedad\n")  # Encabezados
            print(f"Archivo {CSV_FILENAME} creado.")

# Función para guardar datos en el archivo
def guardar_datos_csv(timestamp, temperatura, presion, humedad):
    """Agrega una fila de datos al archivo CSV."""
    try:
        with open(CSV_FILENAME, 'a') as file:
            file.write(f"{timestamp},{temperatura},{presion},{humedad}\n")
            print(f"Datos guardados: {timestamp}, {temperatura}, {presion}, {humedad}")
    except OSError as e:
        print(f"Error al guardar datos: {e}")
