from machine import I2C, Pin
from bme280 import BME280
from config import I2C_SCL_PIN, I2C_SDA_PIN

# Inicializa y configura el sensor BME280
class SensorBME280:
    def __init__(self):
        i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
        self.sensor = BME280(i2c=i2c)

    def leer_datos(self):
        """Lee los datos de temperatura, presión y humedad del sensor."""
        temperatura = self.sensor.temperature()
        presion = self.sensor.pressure()
        humedad = self.sensor.humidity()
        return temperatura, presion, humedad
