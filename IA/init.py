from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO,emit
from flask_mail import Mail 
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app) 

app.config['firstConnect'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on('first-connect')
@cross_origin()
def handleMessage(msg):
    if app.config['firstConnect'] == False :
        try:
            emit("Connected")
        except:
            app.config['firstConnect'] = True
