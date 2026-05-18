from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")          # ← 2 blank lines before this
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/")                # ← 2 blank lines before this
def home():
    return jsonify({"message": "Hello from my app!"})


if __name__ == "__main__":     # ← 2 blank lines before this
    app.run(host="0.0.0.0", port=5000)
    # ← newline at end (invisible but required!)