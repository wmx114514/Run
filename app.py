from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# 账号配置
USERS = {
    "123": {"pwd": "123", "role": "user"},
    "114514": {"pwd": "123", "role": "admin"}
}

# 根路由：返回登录页
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

# 静态文件路由（css、js、html）
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

# 登录接口
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username]["pwd"] == password:
        return jsonify({
            "code": 0,
            "msg": "登录成功",
            "role": USERS[username]["role"],
            "username": username
        })
    return jsonify({"code": 1, "msg": "账号或密码错误"})

# 跨域
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
