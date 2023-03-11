## 目录结构

```bash
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
```

## 运行说明

- 安装依赖

```bash
pip install -r requirements.txt
```

- 国内访问需要自己配置代理，将代码中以下部分改成你自己代理端口即可（根据用户反馈：如果使用V2Ray作为代理工具，Python 旧版本设置 HttpProxy 会出错，但是 Python 在 3.9.13 修复了这个问题，只要更新到最新版本就可以解决，具体见：[#issuecomment-1461901950](https://github.com/XksA-me/ChatGPT-3.5-API/issues/2#issuecomment-1461901950)）

```python
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
```

- ../envs/openai_key 文件中的 api 改成你自己的，访问下面地址获取 openai api 。
  ```
  # api keys 创建页面
  https://platform.openai.com/account/api-key
  ```
- 运行代码

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
127.0.0.1 - - [11/Mar/2023 14:42:51] "POST /token HTTP/1.1" 200 -
127.0.0.1 - - [11/Mar/2023 15:06:14] "GET /api?q=你好，python写一个合并多个+excel+xls文件的案例，每个excel表头一样 HTTP/1.1" 200 
127.0.0.1 - - [11/Mar/2023 15:11:38] "GET /api?q=你好，怎么称呼你？ HTTP/1.1" 200 -
'''
```

更多项目代码说明请看：[chatapi_test.ipynb]() 和 [【详细教程02】手把手教你使用 Python 实现一个 ChatGPT API 接口]()

## 更多拓展

**后面将陆续更新到这个 repo。**

- 你可以写个函数，从 json 文件读取历史用户访问记录，然后每次访问可以选用户。
- 你可以写个 web 服务，使用 session 或者数据库支持多用户同时登录，同时访问。
- 你可以基于之前分享的钉钉机器人项目，将 gpt-3.5-turbo 接入钉钉机器人。

你还可以上 Github 搜索更多 ChatGPT 相关项目，或者其他有意思的项目学习练手，欢迎学习交流。

我创建了个 ChatGPT 应用交流群，如果你感兴趣可以扫下方二维码添加我微信申请加入（备注申请原因）。

<center>
<img src="../static/wx.png" width=40% />
<p>扫码即可加我微信</p>
</center>
