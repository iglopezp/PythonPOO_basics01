from tkinter import *
import requests

def Show_cotation():
    url = r'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

    api_response = requests.get(url)

    api_response_json = api_response.json()

    cot_dolar = api_response_json['USDBRL']['high']
    cot_euro = api_response_json['EURBRL']['high']
    cot_btcoin = api_response_json['BTCBRL']['high']

    cotacao = f'''
    Dolar: R$ {cot_dolar} 
    Euro: R$ {cot_euro}
    BitCoin: R$ {cot_btcoin}'''

    #text_cot['text'] = cotacao
    print(cotacao)

Show_cotation()   


################################################################################################
'''
winPage = Tk()

winPage.title('First window using tkinter')

texto_central = Label( winPage, text='Cotação de Moedas USD/EUR/BTC')
texto_central.grid(column=0, row=0)

btn_cot = Button(winPage, text='Cotações Disppnoveis', command=Show_cotation)
btn_cot.grid(column=0, row=1)

text_cot = Label( winPage, text='')
text_cot.grid(column=0, row=2)



winPage.mainloop()
'''