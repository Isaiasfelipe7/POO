class Bateria:
    def __init__(self, codigo, capacidade):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = 0
    
    def carregar(self, valor):
        nova_carga = self.__percentual_carga + valor
        if nova_carga > 100:
            nova_carga = 100
        self.__percentual_carga = nova_carga
    
    def descarregar(self, valor):
        nova_carga = self.__percentual_carga - valor
        if nova_carga < 0:
            nova_carga = 0
        self.__percentual_carga = nova_carga
    
    def getcodigo(self):
        return self.__codigo
    
    def getcapacidade(self):
        return self.__capacidade
    
    def getpercentual_carga(self):
        return self.__percentual_carga
    
class Celular:
    def __init__(self, mei):
        self.__mei = mei
        self.__bateria = None
        self.__wifi = False
        self.__ligado = False
    
    def ligardesligar(self):
        if self.__bateria is None or self.__bateria.getpercentual_carga() == 0:
            print('O celular está sem carga')
        self.__ligado = not self.__ligado
        if self.__ligado:
            print(f'Celular ligado. Carga da bateria {self.__bateria.getpercentual_carga()} %')
        else:
            print('Celular desligado.')

    def colocarbateria(self, bateria):
        if self.__bateria is not None:
            print('Celular já possui uma bateria.')
        self.__bateria = bateria

    def retirarbateria(self):
        if self.__bateria is None:
            print('Bateria retirada')
        self.__bateria = None

    def ligar_desligar_wifi(self):
        self.__wifi = not self.__wifi
        if self.__wifi:
            print('Wi-Fi ligado')
        else:
            print('Wi-Fi desligado')
    
    def assistir_video(self, tempo):
        if not self.__wifi:
            print('Não foi possível assistir ao vídeo, Wi-Fi desligado')
        if self.__bateria is None or self.__bateria.getpercentual_carga() < tempo * 5:
            print('Não há carga suficiente na bateria para assistir ao vídeo')
            if self.__bateria is not None and self.__bateria.getpercentual_carga() == 0:
                self.descarregar(self.__bateria.getpercentual_carga())
        self.__bateria.descarregar(tempo * 5)
        print(f'Vídeo assistido por {tempo} minutos Carga da bateria {self.__bateria.getpercentual_carga()} %')

    def carregar(self, valor):
        if self.__bateria is not None:
            self.__bateria.carregar(valor)
        
    def descarregar(self, valor):
        if self.__bateria is not None:
            self.__bateria.descarregar(valor)
