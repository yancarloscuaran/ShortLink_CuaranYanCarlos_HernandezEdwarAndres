from flask import Flask, render_template
from flask_mail import Mail, Message
from src import app, mail

def sendEmail(email):
    with app.app_context():
        msg = Message(subject="Confirm Registration",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[email])
        msg.html = render_template('email.html')
        mail.send(msg)
    
