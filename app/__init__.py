from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']= '16e454f599fc965323ff03cfa1018b2241401c32232bb79bfa2447b48f8ea181'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cheptoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
from app import routes