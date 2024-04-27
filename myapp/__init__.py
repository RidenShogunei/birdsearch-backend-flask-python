# __init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://blog:chen2003@47.96.160.149/birdsearch'
db = SQLAlchemy(app)

# 注意在这里导入 views 模块，而不是在 main.py 里。这是因为此时已经初始化了 app 和 db，
# 所以在接下来的 views.py 或其他文件中可以直接导入它们来使用
from myapp import views