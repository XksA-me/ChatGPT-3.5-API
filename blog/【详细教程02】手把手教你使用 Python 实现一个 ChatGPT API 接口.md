大家好，我是老表。

> 手把手教你使用Python调用 ChatGPT-3.5-API。Hands teach you to use Python to call ChatGPT-3.5-API.
>
>> [https://github.com/XksA-me/ChatGPT-3.5-API](https://github.com/XksA-me/ChatGPT-3.5-API)
>>

这是 `手把手教你使用Python调用 ChatGPT-3.5-API`系列第二篇文章，也是第二个项目：[ChatAPI]([https://github.com/XksA-me/ChatGPT-3.5-API](https://github.com/XksA-me/ChatGPT-3.5-API/ChatAPI)) ，项目功能介绍如下图所示：

![1678504700033](image/【详细教程02】手把手教你使用Python实现一个ChatGPTAPI接口/1678504700033.png)

## 先跑起来，再理解

**首先**你需要有一个 openai 账号，如何注册我就不多说了，网上教程很多，而且很详细，如果有问题可以加我微信：pythonbrief，**添加通过后请直接描述你的问题+问题截图**。

访问下面页面，登录 openai 账号后，创建一个 api keys。

```bash
# api keys 创建页面
https://platform.openai.com/account/api-keys
```

**接下来**很简单了，

**1> 下载项目代码：**

```bash
git clone https://github.com/XksA-me/ChatGPT-3.5-API.git

# 如果慢使用下面指令（加了个国内源）
git clone https://ghproxy.com/https://github.com/XksA-me/ChatGPT-3.5-API.git   
```

目录结构：

```bash
.
├── ChatAPI      # 实现 ChatGPT API 服务，Paas应用
├── ChatCMD      # 实现控制台 ChatGPT 多轮对话应用
├── LICENSE  
├── README.md    # 项目总说明
├── blog         # 各个应用实现、使用教程
├── envs         # 存放 key 和各种配置
└── static       # 存放文档静态数据
```

**2> 修改配置文件：**

配置文件在 envs/configs，文件内容如下：

```bash
{"api": "你的 api key", "jwt_secret_key": "你的 JWT_SECRET_KEY"}
```

- 将 api 设置为你的 openai api key
- jwt_secret_key用于指定签名 JWT（JSON Web Token）的密钥，可以随便设置，复杂点为好（后面涉及相关代码会再介绍）

**3> 进入项目目录，安装依赖：**

```bash
cd ChatGPT-3.5-API/ChatAPI
# ChatAPI 项目目录介绍
'''
.
├── README.md            # 项目说明文件
├── chatapi.py           # web 服务主程序
├── chatapi_test.ipynb   # 测试代码
├── chatgpt.py           # 请求 chatgpt 代码
├── file                 # 项目文件
│   ├── chatgpt.db       # sqlite 数据库
│   └── user.csv         # user 表测试数据
├── processing_data.py   # sqlite 数据库操作代码
├── ../envs             # 上级目录下的 envs 文件夹，存放 key
└── requirements.txt     # 项目依赖
'''
```

安装依赖：

```bash
# 注意现在是在：ChatGPT-3.5-API/ChatAPI 目录下
pip install requirements.txt
```

**4> 运行代码：**

- **初始化数据库和数据** processing_data.py `<br/>`
  processing_data.py  包含了初始化代码，直接运行会自动在当前文件夹中的 file 文件夹下生成一个 chatgpt.db 数据库文件，包含两个表：users 和 tokens，默认初始化数据存在：./file/user.csv，可以根据需要修改～

```bash
# 初始化数据
python processing_data.py
```

- **服务端启动服务** `<br/>`
  如果是本地测试 项目运行后服务访问地址：

```bash
- 生成token : http://127.0.0.1:5000/token
- 调用api : http://127.0.0.1:5000/api
```

如果使用的服务器，将 chatapi.py 代码中 127.0.0.1 改成服务器 IP 地址即可。

```bash
python chatapi.py

'''
* Serving Flask app 'chatapi'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.31.225:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 929-327-786
'''
```

- **客户端调用**
- - 获取 Token 代码

```python
# 如果你在自己服务运行，请将 127.0.0.1 改成你自己服务器地址
import requests

# 1. 获取Token
def get_token(username, password):
    url = 'http://127.0.0.1:5000/token'
    data = {
        'u': username,
        'p': password
    }
    response = requests.post(url, json=data)
    print(response.text)
    if response.status_code in {200, 201}:
        return response.json()['message']['token']
    # 其他情况在 服务 里会处理
    return response.json()
```

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36220cdac3524d509e8b0c8ca59b26f0~tplv-k3u1fbpfcp-watermark.image?)

- - 发送 API 请求代码

```python
# 2. 发送API请求
import requests
def call_api(token, q):
    url = 'http://127.0.0.1:5000/api'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(url, headers=headers, params={"q": q})
    if response.status_code == 200 and response.json()['statu']:
        return response.json()['message']
    else:
        # 其他情况在 服务 里会处理
        return response.json()
```

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8df0a372360d4f6da286b75d4a1bbe31~tplv-k3u1fbpfcp-watermark.image?)

- **服务端日志**

```bash
'''
127.0.0.1 - - [11/Mar/2023 14:42:51] "POST /token HTTP/1.1" 200 -
127.0.0.1 - - [11/Mar/2023 15:06:14] "GET /api?q=你好，python写一个合并多个+excel+xls文件的案例，每个excel表头一样 HTTP/1.1" 200 
'''
```

## 关键代码解析

- 使用 Flask-JWT-Extended 实现token生成和有效期管理

```python
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from datetime import datetime, timedelta
from chatgpt import *
from processing_data import (
    get_user, insert_token, get_token_info, update_token, day_diff, get_config
)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = get_config()['jwt_secret_key']  # JWT_SECRET_KEY 随机只有自己知道就行，可在 ../envs/configs 里修改
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)  # Token有效期为30天
jwt = JWTManager(app)
```

这段代码使用了 Flask 框架和 Flask-JWT-Extended 扩展库，实现了对 RESTful API 访问的身份认证和授权控制。

其中 `JWT_ACCESS_TOKEN_EXPIRES`为生成 token 的有效期，上面设置的是 30 天。

- api 请求接口

```python
# 设置单日用户最大请求次数
Request_Count = 10

# API接口路由
@app.route('/api', methods=['GET'])
@jwt_required()
def api():
    # 获取当前Token对应user
    user = get_jwt_identity()
    q = request.args.get('q')
    # 检查 token 对应 user 是否存在
    token_info = get_token_info(user)
    if not token_info:
        return jsonify({'statu': False, 'message': 'Token does not exist. Please contact the administrator to apply.'}), 401
    # 获取用户访问次数
    count = token_info[2]
  
    # 检查访问次数是否需要重置（每日需要重置下次数）
    # 上次请求日期与当前日期相差大于等于一天，且count > 0
    if day_diff(datetime.now().date(), token_info[4]) and count > 0:
        # 重置访问次数
        count = 0

    # 检查Token访问次数是否达到限制
    if count >= Request_Count:
        return jsonify({'statu': False, 'message': 'Token access limit reached.'}), 429
    try:
        messages = [{"role": "user", "content": q}]
        rsp = ask_gpt(messages)
    except Exception as e:
        return jsonify({'statu': False, 'message': f'An error occurred in the chatgpt request, {e}'}), 500
    # 增加Token访问次数
    count+= 1
    last_use_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_token(username=token_info[0], count=count, last_use_time=last_use_time)
    # 返回API响应
    return jsonify({'statu': True, 'message': rsp}), 200
```

> jwt_required() 装饰器用于保护需要授权才能访问的接口；`<br />`
> get_jwt_identity() 函数用于获取当前 Token 的身份标识； `<br />`
> jsonify() 函数用于将 Python 数据结构转换为 JSON 格式； `<br />`

**基本说明：**`<br />`
方法： GET `<br />`
路由： /api `<br />`
认证： JWT `<br />`
功能： 根据用户提供的问题返回机器人回答 `<br />`
**请求参数：**`<br />`
q: 用户提问内容 `<br />`
**返回结果：**`<br />`
statu: 返回结果状态 `<br />`
message: 返回信息内容 `<br />`
**状态码：**`<br />`
200: 请求成功 `<br />`
401: Token不存在或已失效 `<br />`
429: Token请求次数超出限制 `<br />`
500: 服务器内部错误 `<br />`

**请求流程：**

1. 用户发起 API 请求，包含 Token 和查询参数 q。
2. 服务端获取 Token 对应的用户信息。
3. 如果 Token 不存在，返回错误提示信息，状态码 401。
4. 获取当前用户访问次数 count。
5. 判断访问次数是否需要重置，如果上次请求日期与当前日期相差大于等于一天，且 count > 0，重置访问次数。
6. 判断 Token 访问次数是否达到限制 Request_Count。
7. 如果 Token 访问次数达到限制，返回错误提示信息，状态码 429。
8. 发送用户查询请求给 GPT 模型。
9. 捕获 GPT 模型请求异常，返回错误提示信息，状态码 500。
10. 增加用户访问次数 count，更新 Token 最后使用时间 last_use_time。
11. 返回 API 响应，状态码 200。

- token 请求

```python
# Token生成路由
@app.route('/token', methods=['POST'])
def token():
    # 获取用户名和密码
    username = request.json.get('u', None)
    password = request.json.get('p', None)
    user = get_user(username)
    # 检查用户名和密码是否正确
    if not user or password != user[2]:
        return jsonify({'statu': False, 'message': 'Invalid username or password'}), 401
    try:
        # 每个用户只能有一个token
        token_info = get_token_info(username)
        if token_info:
            return jsonify({'statu': True, 'message': {'username': username, 'token': token_info[1], 'expiration_time': token_info[3]}}), 200
        # 生成Token
        token = create_access_token(identity=username)
        # 记录到数据表
        expiration_time = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
        insert_token(username, token, expiration_time)
    except Exception as e:
        return jsonify({'statu': False, 'message': f'Error in create token, Exception: {e}'}), 500
    # 返回Token
    return jsonify({'statu': True, 'message': {'username': username, 'token': token, 'expiration_time': expiration_time}}), 201
```

> create_access_token() 函数用于生成 Token；

**基本说明：**`<br />`
方法： POST `<br />`
路由： /token `<br />`
功能： 用于生成 Token `<br />`
**请求参数：**`<br />`
`u`（string）：用户名，必填。`<br />`
`p`（string）：密码，必填。`<br />`
**返回结果：**`<br />`
status（bool）：请求状态，成功为 true，失败为 false。`<br />`
message（object）：响应信息，成功时包含以下字段：`<br />`

- - username（string）：用户名。
- - token（string）：生成的 Token。
- - expiration_time（string）：Token 过期时间，格式为 YYYY-MM-DD HH:MM:SS。

**状态码：**`<br />`
200：服务器成功处理了请求，并返回了JSON格式的响应；`<br />`
201：服务器成功创建了新资源，并返回了JSON格式的响应；`<br />`
401：表示请求要求身份验证，客户端需要提供有效的用户名和密码；`<br />`
500：服务器内部错误，无法完成请求的处理。

**请求流程：**

1. 客户端向服务器发送一个POST请求，请求的URL是'/token'；
2. 服务器接收到请求后，获取请求体中的用户名和密码，并调用get_user函数查找数据库中是否存在该用户；
3. 如果用户不存在或密码错误，服务器返回一个包含状态码401和错误信息的JSON响应；
4. 如果用户存在且密码正确，服务器调用get_token_info函数查找该用户是否已经有一个token；
5. 如果已经有一个token，服务器返回一个包含状态码200和该token信息的JSON响应；
6. 如果没有token，服务器调用create_access_token函数生成一个新的token，并调用insert_token函数将该token信息插入到数据库中；
7. 如果生成和插入token过程中发生异常，服务器返回一个包含状态码500和异常信息的JSON响应；
8. 服务器返回一个包含状态码201和新生成token信息的JSON响应。

**注：** 以上两个接口请求流程是 ChatGPT 根据代码描写的。

## 常见 Web 状态码含义

在Web访问中，当客户端向服务器发起请求时，服务器会向客户端返回一个状态码，用于告诉客户端请求的处理情况。以下是一些常见的状态码及其含义：

- 200 OK：请求成功，服务器已成功处理了请求。
- 201 Created：请求成功并且服务器创建了新的资源。
- 204 No Content：请求成功，但是响应中没有实体的主体部分。
- 301 Moved Permanently：请求的资源已经永久移动到新的URL。
- 302 Found：请求的资源临时从不同的URL响应请求，但是请求者应继续使用原始URL访问资源。
- 304 Not Modified：请求的资源未被修改，服务器返回此状态码时，不会返回资源的主体部分。
- 400 Bad Request：请求无效，服务器无法识别请求的格式，常见的原因包括请求中的参数有误或者缺失。
- 401 Unauthorized：请求未被授权，需要客户端进行身份验证。
- 403 Forbidden：服务器已经理解请求，但是拒绝执行它，通常是因为客户端没有足够的权限。
- 404 Not Found：请求的资源不存在，服务器无法找到请求的资源。
- 429 Too Many Requests：这意味着客户端发送的请求过多，超过了服务器可以处理的限制。
- 500 Internal Server Error：服务器遇到了意外的情况，无法完成请求。

## 更多拓展

也许你会有疑问，为什么只有 api 和 token 接口，没有 register 注册接口，每次给新用户还得自己手动操作，太蠢了？

本应用是一个 Paas 层的 API 接口，所以没有提供 register 这种应用层面接口，下一步会出一个 ChatWeb 项目，这个项目会有用户登录、注册界面，这时候和 ChatAPI 结合起来，就是一个较为完整的 Web 应用了。（描述和认知不一定准确，如果你有不同看法，欢迎留言指正、交流）

你还可以上 Github 搜索更多 ChatGPT 相关项目，或者其他有意思的项目学习练手，欢迎学习交流。

我创建了个 ChatGPT 应用交流群，如果你感兴趣可以加我 w&x: pythonbrief（**备注申请原因，由于群维护、邀请需要一定人力成本，目前入群需缴纳3元入群费用**）。

也欢迎大家上[github 提问](https://github.com/XksA-me/ChatGPT-3.5-API/issues)。

<center>
<img src="../static/wx.png" width=40% />
<p>扫码即可加我微信</p>
</center>
