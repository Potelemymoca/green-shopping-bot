from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# ===== 首页：给被试用的聊天网页 =====
HTML_PAGE = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>小林超市 · 绿色购物助手</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            padding: 30px;
        }
        .chat-box {
            max-width: 600px;
            margin: auto;
            background: white;
            border-radius: 8px;
            padding: 20px;
        }
        h2 {
            text-align: center;
        }
        #messages {
            border: 1px solid #ddd;
            height: 300px;
            overflow-y: auto;
            padding: 10px;
            margin-bottom: 10px;
        }
        .user {
            color: #333;
            margin-bottom: 6px;
        }
        .bot {
            color: green;
            margin-bottom: 10px;
        }
        input {
            width: 80%;
            padding: 8px;
        }
        button {
            padding: 8px 12px;
        }
    </style>
</head>
<body>

<div class="chat-box">
    <h2>感谢您光顾小林超市 🌱</h2>

    <div id="messages"></div>

    <input id="input" placeholder="请输入您的想法..." />
    <button onclick="sendMessage()">发送</button>
</div>

<script>
function addMessage(text, cls) {
    const div = document.createElement("div");
    div.className = cls;
    div.innerText = text;
    document.getElementById("messages").appendChild(div);
}

async function sendMessage() {
    const input = document.getElementById("input");
    const message = input.value.trim();
    if (!message) return;

    addMessage("你：" + message, "user");
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    addMessage("机器人：" + data.reply, "bot");
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE)


# ===== 实验用接口：机器人回复逻辑 =====
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    reply = (
        "携手选绿品，共绘环保图！🌱\n"
        "根据调查，65%的消费者在购物时更倾向选择环保产品。\n"
        f"你刚刚提到的是：{user_message}"
    )

    return jsonify({"reply": reply})


# ===== Render 启动入口 =====
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
