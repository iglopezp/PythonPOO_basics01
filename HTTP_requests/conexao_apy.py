import json #Biblioteca para manipular objetos Json
import requests #Biblioteca para fazer requisições HTTP

moeda = 'USD-BRL'
url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'

cotacao = requests.get(url) # Requisição GET sem autenticação
json_cotacao = json.loads(cotacao.content) # Conteudo da resposta como objeto Json 

nome_cotacao = json_cotacao['USDBRL']['name']
maior_valor = json_cotacao['USDBRL']['high']
menor_valor = json_cotacao['USDBRL']['low']
data_cotacao = json_cotacao['USDBRL']['create_date']


print(f'Contação: {nome_cotacao}')
print(f'1 USD custa: R$ {maior_valor} (no maior valor do dia)')
print(f'1 USD custa: R$ {menor_valor} (no menor valor do dia)')
print(f'Data de cotação: {data_cotacao}')

