import time
from simple import MQTTClient as SimpleMQTTClient

class MQTTClient(SimpleMQTTClient):
    DELAY = 2  # Tiempo de espera entre reconexiones
    DEBUG = False  # Activar mensajes de depuración

    def delay(self, i):
        time.sleep(self.DELAY)

    def log(self, in_reconnect, e):
        if self.DEBUG:
            if in_reconnect:
                print("mqtt reconnect: %r" % e)
            else:
                print("mqtt: %r" % e)

    def reconnect(self):
        i = 0
        while True:
            try:
                super().connect(False)  # Llama al método connect de la clase base
                return  # Salir del bucle al reconectar
            except OSError as e:
                self.log(True, e)
                i += 1
                self.delay(i)

    def publish(self, topic, msg, retain=False, qos=0):
        while True:
            try:
                super().publish(topic, msg, retain, qos)  # Publica el mensaje
                return  # Salir del bucle si se publica con éxito
            except OSError as e:
                self.log(False, e)
                self.reconnect()  # Intentar reconectar antes de reintentar publicar

    def wait_msg(self):
        while True:
            try:
                return super().wait_msg()  # Espera un mensaje
            except OSError as e:
                self.log(False, e)
                self.reconnect()  # Intentar reconectar

    def check_msg(self, attempts=2):
        while attempts:
            self.sock.setblocking(False)  # Configura el socket como no bloqueante
            try:
                return super().wait_msg()  # Intenta recibir mensajes
            except OSError as e:
                self.log(False, e)
                self.reconnect()  # Intentar reconectar
            attempts -= 1
