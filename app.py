from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Aplicação Flask online!"

@app.route("/api/soma", methods=["POST"])
def soma():
    data = request.json or {}
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run()
