from wifi_lib import conecta
import time
import dht
import machine
import utime
import urequests


# Variavel para acessar DHT e Relé
sensor = dht.DHT11(machine.Pin(13))
rele = machine.Pin(2, machine.Pin.OUT)

# Cabeçalho
print("# TERMÔMETRO E HIDRÔMETRO DIGITAIS #")
print("# Sensor DHT11 #")
print("# Microcontrolador ESP32 #")
print("# Monitoramento pelo IoT Analytics ThingSpeak #")
print()

time.sleep(3)

#Loop principal
while True:
    # Obtém a data e hora atuais em segundos
    tempo_em_segundos = utime.time()

    # Converte o tempo em segundos para uma estrutura de tempo (tupla)
    tempo_formatado = utime.localtime(tempo_em_segundos)

    # Formata a data e hora em uma string manualmente
    formato = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}"  # Define o formato desejado
    data_e_hora_formatadas = formato.format(tempo_formatado[0], tempo_formatado[1], tempo_formatado[2], tempo_formatado[3], tempo_formatado[4], tempo_formatado[5])
    
    #Coleta
    sensor.measure()
    temperatura = sensor.temperature()
    umidade = sensor.humidity()
    
    #Impressão
    print()
    print("Data e hora da medição: {}".format(data_e_hora_formatadas))
    print("Temperatura: {}º".format(temperatura))
    print("Umididade do ar: {}%".format(umidade))
    
    if temperatura > 28 or umidade > 70:
        rele.value(1)
    else:
        rele.value(0)

    print("Conectando [...]")
    station = conecta("NOME_REDE","SENHA_REDE")
    if not station.isconnected():
        print("Falha na conexão. Não conectado.")
    else:
        print("Conexão realizada. Enviando dados para o Thingspeak...")
        url = "https://api.thingspeak.com/update?api_key=ZZ1HC93DQPEV372K&field1={}&field2={}".format(temperatura,umidade)
        response = urequests.get(url)
        print("Dados enviados com sucesso!")
        print(response.text)
        station.disconnect()
    
    time.sleep(50)