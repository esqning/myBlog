from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# print("使用者", __name__)
print(app.config['SECRET_KEY'])

# 因为python存在循环引用问题，所以此导入不能写在前面
from app import routes, model
