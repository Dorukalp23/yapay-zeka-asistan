
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Mesaj boş olamaz"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen kibar ve yardımsever bir yapay zekâ asistanısın."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
