from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Render 健康检查 & 首页
@app.route("/", methods=["GET"])
def home():
    return "Green Shopping Bot is running on Render."

# 实验用对话接口
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    reply = (
        "根据调查，65%的消费者在购物时会更倾向选择环保产品。"
        f"你刚才提到的是：{user_message}"
    )

    return jsonify({"reply": reply}), 200


if __name__ == "__main__":
    # 关键点：必须使用 Render 提供的 PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
