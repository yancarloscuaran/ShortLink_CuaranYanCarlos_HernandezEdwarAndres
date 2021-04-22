from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__, template_folder='views')
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'carloscuaran018@gmail.com',
    "MAIL_PASSWORD": os.environ['correo']
}

app.config.update(mail_settings)
mail = Mail(app)


from src.controllers import *

def create_app():
    app.run(debug=True)