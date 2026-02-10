# Clases contenidas
class Email:
    def enviar(self, mensaje):
        print(f"Enviando EMAIL: {mensaje}")


class Sms:
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")


class Whatsapp:
    def enviar(self, mensaje):
        print(f"Enviando Whatsapp: {mensaje}")


# Clase contenedora
class Notificador:
    def __init__(self, canal):
        if not isinstance(canal, Email) and not isinstance(canal, Sms) and not isinstance(canal, Whatsapp):
            raise Exception("El canal de envío no es correcto")

        self.canal = canal

    def notificar(self, mensaje: str):
        self.canal.enviar(mensaje)

    def cambiar_canal(self, nuevo_canal):
        if not isinstance(nuevo_canal, Email) and not isinstance(nuevo_canal, Sms) and not isinstance(nuevo_canal, Whatsapp):
            raise Exception("El canal de envío no es correcto")
        self.canal = nuevo_canal
