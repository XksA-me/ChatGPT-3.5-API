## 目录结构

```bash
.
├── LICENSE
├── README.md      # 项目说明文件
├── demo-cmd.py    # 教程中多轮对话代码案例
├── demo.ipynb     # 教程中所有代码及注释
├── envs           # 存放 key
│   └── openai_key
├── user_messages.json   # 存储用户访问数据文件
└── 【详细教程】手把手教你使用 Python 调用 ChatGPT-3.5-API.md   # 教程内容
```

## 运行说明

- 安装依赖
```bash
pip install openai==0.27.0
```

- 国内访问需要自己配置代理，将代码中以下部分改成你自己代理端口即可:
```python
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
```

- envs/openai_key 文件中的 api 改成你自己的，如何获取 openai api 看教程内介绍。


- 运行代码
```bash
python demo-cmd.py

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
<img src="https://img-blog.csdnimg.cn/8005475710f1431095f60b2e97af42c4.png" width=60% />

扫码即可加我微信
</center>


