from robust import MQTTClient
from config import (
    THINGSPEAK_MQTT_CLIENT_ID, THINGSPEAK_MQTT_USERNAME, 
    THINGSPEAK_MQTT_PASSWORD, THINGSPEAK_CHANNEL_ID
)

class ClienteMQTT:
    def __init__(self):
        self.client = MQTTClient(
            server=b"mqtt3.thingspeak.com",
            client_id=THINGSPEAK_MQTT_CLIENT_ID,
            user=THINGSPEAK_MQTT_USERNAME,
            password=THINGSPEAK_MQTT_PASSWORD,
            ssl=False,
        )

    def conectar(self):
        """Conecta al broker MQTT."""
        self.client.connect()

    def publicar(self, temp, pres, hum, alt, prob_lluvia=None):
        """Publica los datos al canal de ThingSpeak."""
        topic = f"channels/{THINGSPEAK_CHANNEL_ID.decode()}/publish"
        mensaje = f"field1={temp}&field2={pres}&field3={hum}&field4={alt}"
        if prob_lluvia is not None:
            mensaje += f"&field5={prob_lluvia}"
        mensaje += "\n"
        self.client.publish(topic.encode(), mensaje.encode())


