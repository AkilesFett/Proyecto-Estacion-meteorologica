# Proyecto-Final
Estación meteorológica con una Raspberry Pico W con los datos proporcionados por el sensor BME280, estos datos son impresos en una pantalla OLED 128x64, al mismo tiempo será calculada una probabilidad de lluvia que funciona dentro de la ciudad de México y el Estado de México. Para finalizar mandará los datos con el protocolo MQTT a un canal de ThingSpeak dejando así un ejemplo funcional de la implementación del IoT.  
ATENCIÓN. El archivo de config.py tiene un SSID y contraseña de ejemplo, al igual que la parte de las credenciales de ThingSpeak para evitar poner en riesgo información privada de mi red Wi-fi o de mi cuenta privada. A continuación, pongo los datos a los que me refiero, pero aclaro deben ser cambiados dentro del archivo config.py no en este texto.

# Configuración WiFi
WIFI_SSID = 'Aquí va el nombre de la red Wifi' #Remplazar el texto entre '' con el nombre de una red wifi a la que se tenga alcance 
WIFI_PASSWORD = '*********' #Remplazar la contraseña entre las '' con la contraseña real de la red Wifi a la que se tenga alcance

# Configuración ThingSpeak MQTT
THINGSPEAK_MQTT_CLIENT_ID = b"Aquí va el client id que proporciona thingspeak al agregar un dispositivo al canal" #Remplazar lo que está entre '' con los datos adecuados 
THINGSPEAK_MQTT_USERNAME = b"Aquí va el username que proporciona thingspeak al agregar un dispositivo al canal" #Remplazar lo que está entre '' con los datos adecuados 
THINGSPEAK_MQTT_PASSWORD = b"Aquí va la contraseña que proporciona thingspeak al agregar un dispositivo al canal" #Remplazar lo que está entre '' con los datos adecuados 
THINGSPEAK_CHANNEL_ID = b'Aquí va el ID del canal que se quiere usar' #Remplazar lo que está entre '' con los datos adecuados

Por último, cabe resaltar que los pines de mi config.py están configurados así por el armado físico de mi proyecto, pero de igual forma pueden ser cambiados en la siguiente línea dentro de config.py:

# Pines I2C
I2C_SCL_PIN = 5
I2C_SDA_PIN = 4

Al proporcionar correctamente estos datos el programa funcionará correctamente.
