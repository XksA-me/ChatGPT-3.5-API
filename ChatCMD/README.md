## 目录结构

```bash
.
├── README.md          # 项目运行说明文件
├── chat-cmd.ipynb     # 运行测试和说明代码
├── chat-cmd.py        # 教程中所有代码及注
├── requirements.txt    # 项目依赖
├── ../envs             # 上级目录下的 envs 文件夹，存放 key
└── user_messages.json  # 存储用户访问数据文件
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

- ../envs/configs 文件中的 api 改成你自己的，访问下面地址获取 openai api 。
  ```
  # api keys 创建页面
  https://platform.openai.com/account/api-key
  ```
- 运行代码

```bash
python chat-cmd.py

'''
请输入用户名称: 简说Python
【简说Python】你好，用 画龙点睛 造句
【ChatGPT】在这篇论文中，作者使用了一种简单而精妙的方法来解决这个难题，正是这种方法起到了画龙点睛的作用，使得整个研究更加完美。
【简说Python】0
*********退出程序**********
'''
```

## 更多拓展

** 后面将陆续更新到这个 repo。**

- 你可以写个函数，从 json 文件读取历史用户访问记录，然后每次访问可以选用户。
- 你可以写个 web 服务，使用 session 或者数据库支持多用户同时登录，同时访问。
- 你可以基于之前分享的钉钉机器人项目，将 gpt-3.5-turbo 接入钉钉机器人。

你还可以上 Github 搜索更多 ChatGPT 相关项目，或者其他有意思的项目学习练手，欢迎学习交流。

我创建了个 ChatGPT 应用交流群，如果你感兴趣可以扫下方二维码添加我微信申请加入（备注申请原因）。

<center>
<img src="../static/wx.png" width=40% />
<p>扫码即可加我微信</p>
</center>
