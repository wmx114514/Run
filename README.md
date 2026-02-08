# 登录系统（含管理员面板）
- 普通用户：账号 123，密码 123
- 管理员：账号 114514，密码 123

## 运行
1. pip install -r requirements.txt
2. python app.py
3. 打开 static/index.html

## 功能
- 双角色登录
- 登录成功自动跳转
- 普通用户首页
- 管理员面板
- 退出登录

## 手机Termux运行
1.pkg update && pkg upgrade -y更新
2.pkg install python -y安装pip
3.pip install flask安装flask(核心)
4.下载到手机
5.进入Termus
6.cd (你下载此项目的目录)
7.如果是压缩包就解压
8.python app.py
9.成功后会提示 :
* Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://xxx.xxx.xxx.xxx:5000
10.浏览器进入http://127.0.0.1:5000
