from flask import Flask, render_template, request
import requests

app = Flask(__name__)

link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
moedas = requests.get(link).json()
data_atualizacao_dolar = moedas['USDBRL']['create_date']
data_atualizacao_euro = moedas['EURBRL']['create_date']
data_atualizacao_bitcoin = moedas['BTCBRL']['create_date']
cotacao_dolar = moedas['USDBRL']['bid']
cotacao_euro = moedas['EURBRL']['bid']
cotacao_bitcoin = moedas['BTCBRL']['bid']

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/brltousd', methods=['POST'])
def get_brl_usd():
    return render_template('index_dolar.html')


@app.route('/converterbrlusd', methods=['POST'])
def converter_brl_usd():
    valor = float(request.form.get('valor_usuario_real'))
    valorDolar = float(cotacao_dolar)
    valor_convertido_dolar = valor * valorDolar
    valor = f'{valor:,.1f}'
    
    valor_convertido_dolar = f'{valor_convertido_dolar:,.2f}'
    return render_template('index_dolar.html', valor=valor, valor_convertido_dolar=valor_convertido_dolar, data_atualizacao_dolar=data_atualizacao_dolar)


@app.route('/brltoeur', methods=['POST'])
def get_brl_eur():
    return render_template('index_euro.html')


@app.route('/converterbrleur', methods=['POST'])
def converter_brl_eur():
    valor = float(request.form.get('valor_usuario_real'))
    valor_euro = float(cotacao_euro)
    valor_convertido_euro = valor * valor_euro
    valor = f'{valor:,.1f}'
    
    valor_convertido_euro = f'{valor_convertido_euro:,.2f}'
    
    return render_template('index_euro.html', valor=valor, valor_convertido_euro=valor_convertido_euro, data_atualizacao_euro=data_atualizacao_euro)


@app.route('/btctobrl', methods=['POST'])
def get_btc_brl():
    return render_template('index_bitcoin.html')


@app.route('/converterbrlbtc', methods=['POST'])
def converter_brl_btc():
    valor = float(request.form.get('valor_usuario_real'))
    valor_convertido_bitcoin = float(cotacao_bitcoin)
    valor_convertido_bitcoin = valor * valor_convertido_bitcoin
    valor = f'{valor:,.1f}'
    
    valor_convertido_bitcoin = f'{valor_convertido_bitcoin:,.2f}'
    
    return render_template('index_bitcoin.html', valor=valor, valor_convertido_bitcoin=valor_convertido_bitcoin, data_atualizacao_bitcoin=data_atualizacao_bitcoin)


if __name__ == '__main__':
    app.run(debug=True)
