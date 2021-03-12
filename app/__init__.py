from flask import Flask

app = Flask(__name__)

print("使用者", __name__)

# 因为python存在循环引用问题，所以此导入不能写在前面
from app import routes
