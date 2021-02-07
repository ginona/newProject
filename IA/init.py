from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'alertsauronalert@gmail.com'
app.config['MAIL_PASSWORD'] = 'sauron123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

db.init_app(app)

