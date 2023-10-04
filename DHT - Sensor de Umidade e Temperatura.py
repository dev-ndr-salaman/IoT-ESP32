import dht
import machine
import time
import utime

# Variavel para acessar DHT
d = dht.DHT11(machine.Pin(13))

#Loop
i = 1

print("# TERMÔMETRO E HIDRÔMETRO DIGITAIS #")
print("# Sensor DHT11 #")
print("# Microcontrolador ESP32 #")
print()



while i<3:
    # Obtém a data e hora atuais em segundos
    tempo_em_segundos = utime.time()

    # Converte o tempo em segundos para uma estrutura de tempo (tupla)
    tempo_formatado = utime.localtime(tempo_em_segundos)

    # Formata a data e hora em uma string manualmente
    formato = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}"  # Define o formato desejado
    data_e_hora_formatadas = formato.format(tempo_formatado[0], tempo_formatado[1], tempo_formatado[2], tempo_formatado[3], tempo_formatado[4], tempo_formatado[5])

    d.measure()
    print()
    print("Data e hora da medição: {}".format(data_e_hora_formatadas))
    print("Temperatura: {}º".format(d.temperature()))
    print("Umididade do ar: {}%".format(d.humidity()))
    time.sleep(50)
    i += 1
    
