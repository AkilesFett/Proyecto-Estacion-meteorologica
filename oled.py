from ssd1306 import SSD1306_I2C
from machine import I2C, Pin
from config import I2C_SCL_PIN, I2C_SDA_PIN

class PantallaOLED:
    def __init__(self):
        i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
        self.oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

    def mostrar_datos(self, temp, pres, hum, alt, prob_lluvia):
        """Muestra los datos en la pantalla OLED."""
        self.oled.fill(0)
        self.oled.text(f"Temp: {temp:.2f}C", 0, 0)
        self.oled.text(f"Pres: {pres:.2f}hPa", 0, 14)
        self.oled.text(f"Hum: {hum:.2f}%", 0, 28)
        self.oled.text(f"Alt: {alt:.2f}m", 0, 42)
        self.oled.text(f"Prob_lluv: {prob_lluvia:.1f}%", 0, 56)
        self.oled.show()

