from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1!@localhost:5432/market'
app.config['SECRET_KEY'] = '1437138c9564e90c70431aa1'
db =SQLAlchemy(app)

from market import route



