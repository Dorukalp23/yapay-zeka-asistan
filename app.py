
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "BURAYA_OPENAI_API_ANAHTARINI_YAZ"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Mesaj boş olamaz"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen yardımsever bir yapay zekâ asistanısın."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

# 💡 index.html dosyasını tarayıcıda göstermek için:
@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
