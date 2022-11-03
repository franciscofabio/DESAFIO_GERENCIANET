from flask import Flask, request
import pandas as pd
import joblib as jb
#import json
import os
import setuptools

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
    birth_year = df['birth_year'].values[0]
    age_creation = df['age_creation'].values[0]

    input = pd.DataFrame({'account_number': conta,
                          'occupation': occupation, 'state': state,
                          'city': city, 'paid': paid, 'unpaid': unpaid,
                          'birth_year': birth_year, 'age_creation': age_creation
                          }, index=[0])

    pred = int(mdl.predict(input)[0])

    return f"<h1>Conta: {conta}  Fraude: {pred}</h1>"


app.run(debug=True, port=5000)
"""if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)"""
