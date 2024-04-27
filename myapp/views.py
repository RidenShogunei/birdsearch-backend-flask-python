# views.py
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from . import app, db
from myapp.models import User
import uuid
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # 获取 JSON 数据
    if data and 'username' in data and 'password' in data and 'realname' in data:  # 验证数据完整性
        hashed_password = generate_password_hash(data['password'], method='sha256')  # 密码哈希处理

        new_user = User(
            uid=str(uuid.uuid4()),  # 使用 UUID 生成 uid
            username=data['username'],
            password=hashed_password,
            realname=data['realname'],
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'uid': new_user.uid}), 201  # 返回 uid 和 201 状态码
    else:
        return 'Invalid data!', 400  # 返回错误信息和 400 状态码


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # 获取 JSON 数据
    if data and 'username' in data and 'password' in data:  # 验证数据完整性
        user = User.query.filter_by(username=data['username']).first()  # 查找用户

        if user and check_password_hash(user.password, data['password']):  # 验证密码
            return jsonify({'uid': user.uid}), 200  # 返回 uid 和 200 状态码
        else:
            return 'Invalid credentials!', 401  # 返回错误信息和 401 状态码
    else:
        return 'Invalid data!', 400  # 返回错误信息和 400 状态码# 登录函数...

@app.route('/')
def hello():
    return 'hello'