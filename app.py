GROUP_TYPE = "coop"
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 六种实验物品
items = ["A4纸", "胶带", "垃圾袋", "纸杯", "笔", "牙刷"]

# 合作组口号
slogans_coop = {
    "A4纸": "携手选绿A4纸，共建绿色办公环境！",
    "胶带": "携手选择环保胶带，共同减少资源浪费！",
    "垃圾袋": "携手更换环保垃圾袋，一起守护城市清洁！",
    "纸杯": "携手使用环保纸杯，共饮绿色生活！",
    "笔": "携手选绿笔，共绘环保图！",
    "牙刷": "携手更换环保牙刷，共护健康与地球！"
}

# 非合作组口号
slogans_control = {
    "A4纸": "选择环保A4纸，顺应绿色办公主流。",
    "胶带": "选择环保胶带，顺应绿色消费主流。",
    "垃圾袋": "选择环保垃圾袋，顺应环保生活趋势。",
    "纸杯": "选择环保纸杯，顺应绿色消费趋势。",
    "笔": "选择环保笔，顺应绿色消费主流。",
    "牙刷": "选择环保牙刷，顺应环保生活趋势。"
}

@app.route("/coop")
def coop():
    return render_template("index.html", group="coop")

@app.route("/control")
def control():
    return render_template("index.html", group="control")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "").strip()
    group = data.get("group")

    if msg not in items:
        return jsonify({"reply": "请输入指定商品名称（A4纸、胶带、垃圾袋、纸杯、笔、牙刷）"})

    eco_item = f"环保{msg}"

    if group == "coop":
        reply = (
            f"感谢您光顾小林超市！"
            f"{slogans_coop[msg]}"
            f"65%的消费者已经开始选择{eco_item}。"
            f"{eco_item}的材质均为可降解材料，不仅性能不逊色于传统{msg}，"
            f"也践行了绿色发展的理念。选择{eco_item}是我们共同的责任，助力环境保护！"
        )
    else:
        reply = (
            f"感谢您光顾小林超市！"
            f"{slogans_control[msg]}"
            f"65%的消费者已经开始选择{eco_item}。"
            f"{eco_item}的材质均为可降解材料，不仅性能不逊色于传统{msg}，"
            f"也践行了绿色发展的理念。为了环保事业，倡导您顺应主流，选择{eco_item}。"
        )

    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
