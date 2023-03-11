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
    # # @jwt_required() 只有token有效期内才能访问，所以无需再次判断
    # # 检查 Token 是否过期
    # if datetime.now() > token_info[3] :
    #     # 过期的 Token 状态设置为过期
    #     update_token(username=token_info[0], count=count, last_use_time=token_info[4])
    #     return jsonify({'statu': False, 'message': 'Token expired'}), 401
    
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



if __name__ == '__main__':
    # 默认开启 debug 模式，生产环境请设置成 False
    app.run(host="0.0.0.0", port=5000, debug=True)
