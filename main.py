from flask import Flask, render_template, request
import requests
url = 'https://api.exchangerate.host/latest'

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 1234
DEBUG = True


@app.route('/', methods=['POST', "GET"])
def index():
    response = requests.get(url)
    data = response.json()['rates']
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if amount == int(amount):
            amount = int(amount)
        first_wallet = float(request.form['first'])
        second_wallet = float(request.form['second'])
        total_amount = round(float(second_wallet) / float(first_wallet) * amount, 2)
        return render_template('index.html', data=data, total_amount=total_amount, first_wallet=first_wallet, second_wallet=second_wallet, amount=amount)
    else:
        return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
