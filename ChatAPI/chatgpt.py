import openai
import json
import os
from processing_data import get_config

os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
openai.api_key = get_config()['api']


# 发送请求给 chatgpt
def ask_gpt(messages):
    # q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return rsp.get("choices")[0]["message"]["content"]