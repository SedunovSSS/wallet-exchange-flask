from flask import Flask, render_template, request
import requests
url = 'https://api.exchangerate.host/latest'

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 4321
DEBUG = True


@app.route('/', methods=['POST', "GET"])
def index():
    response = requests.get(url)
    data = response.json()['rates']
    if request.method == 'POST':
        first_wallet = request.form['first']
        second_wallet = request.form['second']
        try:
            amount = float(request.form['amount'])
            if amount == int(amount):
                amount = int(amount)
            total_amount = round(float(data[second_wallet]) / float(data[first_wallet]) * amount, 2)
            if total_amount == int(total_amount):
                total_amount = int(total_amount)
            return render_template('index.html', data=data, total_amount=total_amount,
                                   first_wallet=first_wallet, second_wallet=second_wallet, amount=amount)
        except Exception as ex:
            print(ex)
            return render_template('index.html', data=data, first_wallet=first_wallet,
                                   second_wallet=second_wallet)
    else:
        return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
