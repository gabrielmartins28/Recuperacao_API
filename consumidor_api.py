import requests


def obter_dados_meteorologicos():
    endereco = "http://127.0.0.1:8000/v1/forecast"
    parametros = {
    "latitude": -26.4851,
    "longitude": -49.0713,

    }


    resposta = requests.get(
    endereco,
    params=parametros,
    timeout=15
    )
    
    resposta.raise_for_status()
    dados = resposta.json()
    condicoes_atuais = dados['current']
    temperatura = condicoes_atuais['temperature_2m']
    umidade = condicoes_atuais["relative_humidity_2m"]
    sensacao_termica = condicoes_atuais["apparent_temperature"]
    precipitacao = condicoes_atuais["precipitation"]
    vento = condicoes_atuais["wind_speed_10m"]
    horario = condicoes_atuais["time"]

    return {    "temperatura": temperatura,    "umidade_relativa": umidade,    "sensacao_termica": sensacao_termica,    "precipitacao": precipitacao,    "velocidade_vento": vento,    "horario": horario}






# resposta.raise_for_status()

# if resposta.status_code == 200:
#     print("DEu certo")
#     dados = resposta.json()


#     temperatura = dados["current"]["temperature_2m"]
#     umidade = dados["current"]["relative_humidity_2m"]
#     sensacao_termica = dados["current"]["apparent_temperature"]
#     precipitacao = dados["current"]["precipitation"]
#     vento = dados["current"]["wind_speed_10m"]
#     horario = dados["current"]["time"]

    

    





  
  
  
    