def conecta(ssid, senha):
    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

import urequests
print("Conectando [...]")
station = conecta("IPOJUCA","patinhas123")
if not station.isconnected():
    print("Falha na conexão. Não conectado.")
else:
    print("Conexão realizada. Acessando ")
    "Temperatura: {}º".format(sensor.temperature())
    response = urequests.get("https://api.thingspeak.com/update?api_key=ZZ1HC93DQPEV372K&field1=20")
    print("Página acessada: ")
    print(response.text)
    station.disconnect()

    
    
