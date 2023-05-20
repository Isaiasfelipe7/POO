from CelularBateria import Bateria, Celular

# Criar instâncias da classe Bateria
bateria1 = Bateria('001', 1000)
bateria2 = Bateria('002', 1500)
bateria3 = Bateria('003', 2000)

# Testar métodos da classe Bateria
print(bateria1.getcodigo())  # Saída: "001"
print(bateria1.getcapacidade())  # Saída: 1000
print(bateria1.getpercentual_carga())  # Saída: 0

bateria1.carregar(50)
print(bateria1.getpercentual_carga())  # Saída: 50

bateria1.descarregar(30)
print(bateria1.getpercentual_carga())  # Saída: 20

# Criar instâncias da classe Celular
celular1 = Celular('IMEI001')
celular2 = Celular('IMEI002')
celular3 = Celular('IMEI003')

# Testar métodos da classe Celular
celular1.colocarbateria(bateria1)
celular1.ligardesligar()  # Saída: "Celular ligado. Carga da bateria 20 %"
celular1.ligar_desligar_wifi()  # Saída: "Wi-Fi ligado"
celular1.assistir_video(10)  # Saída: "Vídeo assistido por 10 minutos. Carga da bateria 0 %"

celular2.colocarbateria(bateria2)
celular2.carregar(50)
celular2.ligardesligar()  # Saída: "Celular ligado. Carga da bateria 50 %"
celular2.ligar_desligar_wifi()  # Saída: "Wi-Fi desligado"
celular2.assistir_video(5)  # Saída: "Não foi possível assistir ao vídeo. Wi-Fi desligado"

celular3.colocarbateria(bateria3)
celular3.carregar(100)
celular3.ligardesligar()  # Saída: "Celular desligado."
celular3.ligar_desligar_wifi()  # Saída: "Wi-Fi ligado"
celular3.assistir_video(15)  # Saída: "Não há carga suficiente na bateria para assistir ao vídeo"

celular1.colocarbateria(bateria2)
celular1.retirarbateria()
celular1.colocarbateria(bateria2)

celular2.colocarbateria(bateria3)
celular2.retirarbateria()
celular2.colocarbateria(bateria3)

celular3.colocarbateria(bateria1)
celular3.retirarbateria()
celular3.colocarbateria(bateria1)
