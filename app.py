from flask import Flask, request
import pandas as pd
import joblib as jb
import json

app = Flask(__name__)

mdl = jb.load("my_rf_pycaret_model.pkl")


@app.route('/', methods=['GET'])
def result():
    account = request.args.get('account_number')

    """with open("data.json") as f:
        data = json.load(f)"""

    df = pd.read_json('data.json')
    df['account_number'] = df['account_number'].astype(str)
    df = df.loc[df.account_number == account]

    # Coleta dos dados para produção
    conta = df['account_number'].values[0]
    occupation = df['occupation'].values[0]
    state = df['state'].values[0]
    city = df['city'].values[0]
    paid = df['paid'].values[0]
    unpaid = df['unpaid'].values[0]

    input = pd.DataFrame({'account_number': conta, 'occupation': occupation,
                         'state': state, 'city': city, 'paid': paid, 'unpaid': unpaid}, index=[0])

    pred = int(mdl.predict(input)[0])

    return f"<h1>Conta: {conta}  Fraude: {pred}</h1>"


app.run(debug=True)
