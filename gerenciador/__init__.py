from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ti102.db'
app.config['SECRET_KEY'] = '86d669633821c3fd298601018490b6b6f9416ccb8ee7873729b963615c3d9676'

database = SQLAlchemy(app)
brypt= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from gerenciador import routes, models
