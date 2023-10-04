from wifi_lib import conecta
import urequests
print("Conectando [...]")
station = conecta("NOME_REDE","SENHA_REDE")
if not station.isconnected():
    print("Falha na conexão. Não conectado.")
else:
    print("Conexão realizada. Acessando ")
    response = urequests.get("https://www.ppgia.pucpr.br")
    print("Página acessada: ")
    print(response.text)
    station.disconnect()

    
    