from flask import Flask, render_template, request, jsonify
import pandas as pd
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("portfolio.html")


@app.route('/data', methods=['GET'])
def get_data():
    # gets all of the data
    conn = sqlite3.connect('data/mydatabase.db')
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM bitcoin_data", conn)
    conn.close()
    return jsonify(df.to_dict(orient="records"))


app.run(host="127.0.0.1", port=5000)
