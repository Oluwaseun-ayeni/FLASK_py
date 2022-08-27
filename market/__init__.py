import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1!@localhost:5432/market'
app.config['SECRET_KEY'] = '1437138c9564e90c70431aa1'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_PROTOCOL'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME']= 'Oayeni139@gmail.com'
app.config['MAIL_PASSWORD']= 'emtopmmmaialjwxi'
app.config['MAIL_DEFAULT_SENDER'] = 'Oayeni139@gmail.com'
app.config['MAIL_MAX_EMAILS'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = True
# app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

# app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin Oayeni139@gmail.com'
# app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
db =SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)



login_manager = LoginManager()


# os.environ.get('MAIL_USERNAME')
# os.environ.get('MAIL_PASSWORD')





from market import route



