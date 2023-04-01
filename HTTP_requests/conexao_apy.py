import json #Biblioteca para manipular objetos Json
import requests #Biblioteca para fazer requisições HTTP

moeda = 'USD-BRL'
url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'

cotacao = requests.get(url)
print(cotacao.content)
