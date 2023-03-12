## 目录结构

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

完整文件导航：

```
.
├── ChatAPI
│   ├── README.md
│   ├── chatapi.py
│   ├── chatapi_test.ipynb
│   ├── chatgpt.py
│   ├── file
│   ├── processing_data.py
│   └── requirements.txt
├── ChatCMD
│   ├── README.md
│   ├── chat-cmd.ipynb
│   ├── chat-cmd.py
│   ├── requirements.txt
│   └── user_messages.json
├── LICENSE
├── README.md
├── blog
│   ├── image
│   ├── 【详细教程01】手把手教你使用 Python 调用 ChatGPT-3.5-API.md
│   └── 【详细教程02】手把手教你使用 Python 实现一个 ChatGPT API 接口.md
├── envs
│   └── configs
└── static
    └── wx.png

7 directories, 17 files
```

## 运行说明

[ChatAPI 运行说明](https://github.com/XksA-me/ChatGPT-3.5-API/blob/master/ChatAPI/README.md)

[ChatCMD 运行说明](https://github.com/XksA-me/ChatGPT-3.5-API/blob/master/ChatCMD/README.md)

## 更多拓展

你还可以上 Github 搜索更多 ChatGPT 相关项目，或者其他有意思的项目学习练手，欢迎学习交流。

我创建了个 ChatGPT 应用交流群，如果你感兴趣可以扫下方二维码添加我微信申请加入（备注申请原因）。

<center>
<img src="./static/wx.png" width=40% />
<p>扫码即可加我微信</p>
</center>

## 项目更新计划

### 2023.3.3

[ChatCMD](https://github.com/XksA-me/ChatGPT-3.5-API/tree/master/ChatCMD)

- 基于最新模型 gpt-3.5-turbo
- 支持多轮对话
- 仅实现 Python 控制台应用
  程序代码文件：[chat-cmd.py](https://github.com/XksA-me/ChatGPT-3.5-API/blob/master/ChatCMD/chat-cmd.py)

### 2023.3.12

[ChatAPI](https://github.com/XksA-me/ChatGPT-3.5-API/tree/master/ChatAPI)

**开发ing:**（预计本周上线）

- 基于flask，构建 chatgpt api
- 支持根据用户账号密码自动生成 token
- 支持限制单用户每日访问次数
- 支持设置token有效期

**下一步开发计划:**(预计下周上线)

ChatWEB

- 基于 pywebio/streamlit 的web 页面应用

**再下一步:**

- 基于flask的web页面应用
- 支持登录注册
- 限制单用户单日访问次数

**再再下一步:**

ChatBOT

- 钉钉机器人，可以参考项目[DingdingBot](https://github.com/XksA-me/DingdingBot)
- 飞书机器人，如果有人有需要的话

[更多需求可以点击这里交流](https://github.com/XksA-me/ChatGPT-3.5-API/issues/2)

## 支持作者

点个 start ，参与项目贡献（issue: 提出运行问题、fork: 基于项目实现其他应用）。
