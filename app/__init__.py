from flask import Flask




app = Flask(__name__)
app.config['SECRET_KEY']= '16e454f599fc965323ff03cfa1018b2241401c32232bb79bfa2447b48f8ea181'




from app import routes