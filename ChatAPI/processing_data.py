import sqlite3
import csv
from datetime import datetime, timedelta
import json


DATABASE_NAME = './file/chatgpt.db'

# 初始化数据库函数，创建两个表：用户表和token表
def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # 创建用户表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL, -- 用户账号
            password TEXT NOT NULL, -- 用户密码
            registration_time DATETIME DEFAULT (datetime('now', 'localtime')), -- 注册时间
            last_login_time DATETIME DEFAULT (datetime('now', 'localtime')) -- 上次登录时间
        )
    ''')

    # 创建token表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL, -- 用户账号
            token_value TEXT UNIQUE NOT NULL, -- token值
            count INTEGER DEFAULT 0, -- 请求次数
            expiration_time DATETIME NOT NULL, -- 到期时间
            last_use_time DATETIME DEFAULT (datetime('now', 'localtime')) -- 上次调用时间
        )
    ''')

    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()

# 添加新用户到用户表
def create_user(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))

    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()

# 通过用户名获取用户信息
def get_user(username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT id, username, password, registration_time, last_login_time
        FROM users
        WHERE username='{username}'
    ''')

    user = cursor.fetchone()
    # 关闭游标和连接
    cursor.close()
    conn.close()

    return user

# 将 token 记录到 token 表中
def insert_token(username, token_value, expiration_time):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO tokens (username, token_value, expiration_time)
        VALUES (?, ?, ?)
    ''', (username, token_value, expiration_time))

    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()

# 更新 token 数据（使用次数+状态）
def update_token(username, count, last_use_time):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tokens
        SET count=?, last_use_time = ?
        WHERE username = ?
    ''', (count, last_use_time, username))

    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()

# 通过 username 值获取 token 信息
def get_token_info(username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT username, token_value, count, expiration_time, last_use_time
        FROM tokens
        WHERE username = ?
    ''', (username,))
    
    token_info = cursor.fetchone()

    # 关闭游标和连接
    cursor.close()
    conn.close()

    return token_info
    
# 批量写入用户数据
def update_data(data_file='./file/user.csv'):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # 打开CSV文件
    with open(data_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # 遍历CSV文件的每一行
        for row in reader:
            # 提取用户名和密码
            username = row['username']
            password = row['password']
            # 插入一行数据
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username,password))

    # 提交事务
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()

def delete_data(username, table):
    # 创建连接
    conn = sqlite3.connect(DATABASE_NAME)
    # 创建游标
    cursor = conn.cursor()
    # 执行删除语句
    cursor.execute(f"DELETE FROM {table} WHERE username = '{username}'")
    # 确认删除操作
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()


# 查看数据表结构和数据
def check_db():
    # 连接到数据库文件
    conn = sqlite3.connect(DATABASE_NAME)
    # 创建一个游标对象
    cursor = conn.cursor()
    # 获取所有表的名称
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    # 对于每个表，获取表结构和数据
    for table_name in tables:
        table_name = table_name[0]
        print(f"Table: {table_name}")
        cursor.execute(f"SELECT * from {table_name}")
        col_names = [description[0] for description in cursor.description]
        print(col_names)
        for row in cursor.fetchall():
            print(row)

    # 关闭游标和连接
    cursor.close()
    conn.close()


# 判断日期差
def day_diff(today, datestr):
    date_time = datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
    # 提取日期（不含时间）
    date_only = date_time.date()
    # 计算日期差异
    diff = today - date_only
    # 检查日期差异是否等于1天
    if diff >= timedelta(days=1):
        return True
    else:
        return False


# 获取 configs 内容
def get_config():
    # 可以自己根据自己实际情况实现
    # 以我为例子，我是存在一个 configs 文件里，json 格式
    '''
    {"api": "你的 api keys"}
    '''
    config_file = '../envs/configs'
    with open(config_file, 'r', encoding='utf-8') as f:
        configs = json.loads(f.read())
    return configs

if __name__=="__main__":
    # 初始化数据库
    init_db()
    # 初始化用户表
    data_file = './file/user.csv'
    update_data(data_file)
    # 检查数据表结构和数据内容
    check_db()
    # 测试通过用户名查找用户信息
    print("chatweb2: ", get_user("chatweb2"))
    