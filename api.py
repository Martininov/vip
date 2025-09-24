from flask import Flask, jsonify
from main import main

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "message": "Bienvenue sur l'API SofaScore"}

@app.route("/matches")
def matches():
    data = main()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
