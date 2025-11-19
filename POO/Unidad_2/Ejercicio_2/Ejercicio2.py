class Email:
    def enviar(self,mensaje):
        print("Enviando EMAIL: ",mensaje)

class SMS:    
    def enviar(self,mensaje):
        print("Enviando SMS: ",mensaje)

class Whatsapp:
    def enviar(self,mensaje):
        print("Enviando Whatsapp: ",mensaje)

class Notificador:
    
    def __init__(self,canal):
        if not isinstance(canal, Email) and not isinstance(canal, SMS) and not isinstance(canal, Whatsapp):
            raise Exception("El canal de envio no es correcto")
        
        self.canal = canal

    def notoficar_mensaje(self, mensaje:str):
        self.canal.enviar(mensaje)

    def cambiar_canal(self, nuevo_canal):
        if not isinstance(nuevo_canal, Email) and not isinstance(nuevo_canal, SMS) and not isinstance(nuevo_canal, Whatsapp):
            raise Exception("El canal de envio no es correcto")

        self.canal = None
        self.canal = nuevo_canal


if __name__=="__main__":
    try:
        notificador = Notificador(Email())
        notificador.notoficar_mensaje("que pasa")
            
        notificador.cambiar_canal(SMS())
        notificador.notoficar_mensaje("que pasa")

        notificador.cambiar_canal(Whatsapp())
        notificador.notoficar_mensaje("que pasa")
    except Exception as e:
        print