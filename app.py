from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义两个账号：普通用户 + 管理员
USERS = {
    "123": "123",
    "114514": "123"
}

# 登录接口
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        # 判断是否是管理员
        role = "admin" if username == "114514" else "user"
        return jsonify({
            "code": 0,
            "msg": "登录成功",
            "role": role,
            "username": username
        })
    else:
        return jsonify({"code": 1, "msg": "账号或密码错误"})

# 允许跨域
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
