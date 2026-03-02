from flask import Flask, request, jsonify

app = Flask(__name__)

# 首页（必须有）
@app.route("/", methods=["GET"])
def home():
    return "Green Shopping Bot is running on Render."

# 聊天接口
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    reply = (
        "根据调查，65%的消费者在购物时会更倾向选择环保产品。"
        f" 你刚才提到的是：{user_message}"
    )

    return jsonify({"reply": reply})
