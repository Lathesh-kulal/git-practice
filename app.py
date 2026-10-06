from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask!"


@app.route("/api/message")
def message():
    return jsonify({
        "message": "Welcome to my Flask application!"
    })


if __name__ == "__main__":
    app.run(debug=True)