from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import openai

app = Flask(__name__, static_folder='public')
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Ana sayfa: index.html dosyasını göster
@app.route("/")
def serve_index():
    return send_from_directory("public", "index.html")

# API endpoint
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    if not user_message:
        return jsonify({"reply": "Mesaj boş olamaz."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "API hatası oluştu."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
