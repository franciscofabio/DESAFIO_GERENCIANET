from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def result():
    id = request.args.get('id')
    
    with open("example.json")
    return f"<h1>Conta: {id}</h1>"

app.run(debug=True)