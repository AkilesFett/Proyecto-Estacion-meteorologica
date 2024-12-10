import network
import time
import sys
from sensor import SensorBME280
from oled import PantallaOLED
from mqtt_client import ClienteMQTT
from utils import calcular_altura, calcular_probabilidad_lluvia
from data_logger import inicializar_csv, guardar_datos_csv
from config import WIFI_SSID, WIFI_PASSWORD

# Función para generar un timestamp manual
def generar_timestamp():
    """Genera un timestamp en formato 'YYYY-MM-DD HH:MM:SS'."""
    t = time.localtime()
    return f"{t[0]:04d}-{t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}"

# Conexión WiFi
def conectar_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    print("Conectando al WiFi...")
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)

    for i in range(20):
        if wifi.isconnected():
            print(f"Conectado al WiFi. Dirección IP: {wifi.ifconfig()}")
            return
        time.sleep(1)
    print("Error: No se pudo conectar al WiFi")
    sys.exit()

# Programa principal
def main():
    conectar_wifi()

    # Inicializar componentes
    sensor = SensorBME280()
    oled = PantallaOLED()
    mqtt = ClienteMQTT()
    mqtt.conectar()

    # Inicializar archivo CSV
    inicializar_csv()

    # Publicar datos periódicamente
    while True:
        try:
            # Leer datos del sensor
            temp, pres, hum = sensor.leer_datos()
            alt = calcular_altura(pres, temp)
            prob_lluvia = calcular_probabilidad_lluvia(hum, pres, temp, presion_base=780)  # Corregido
            timestamp = generar_timestamp()  # Generar timestamp

            # Guardar datos en CSV
            guardar_datos_csv(timestamp, temp, pres, hum)

            # Mostrar en OLED
            oled.mostrar_datos(temp, pres, hum, alt, prob_lluvia)

            # Publicar a MQTT
            mqtt.publicar(temp, pres, hum, alt, prob_lluvia)

            print(f"Temp: {temp}C, Pres: {pres}hPa, Hum: {hum}%, Alt: {alt}m, Prob: {prob_lluvia:.1f}%")
            time.sleep(16)
        except KeyboardInterrupt:
            print("Ctrl-C presionado... saliendo")
            sys.exit()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
