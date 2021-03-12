from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

# print("使用者", __name__)
print(app.config['SECRET_KEY'])

# 因为python存在循环引用问题，所以此导入不能写在前面
from app import routes
