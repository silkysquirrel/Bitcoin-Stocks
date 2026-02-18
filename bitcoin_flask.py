from flask import Flask, render_template, request, jsonify
import pandas as pd
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data', methods=['GET'])
def get_data():
    # gets all of the data
    conn = sqlite3.connect('data/mydatabase.db')
    cursor = conn.cursor()
    df = pd.read_sql_query("""
    SELECT 
        Start,
        End,
        Open,
        High,
        Low,
        Close,
        Volume,
        "Market Cap" AS MarketCap
    FROM bitcoin_data
""", conn)
    conn.close()
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
