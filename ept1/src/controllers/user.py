from flask import render_template, request, redirect, url_for, flash
from src import app
from src.models.user import userModel
from src.models.acortador import shortLinkModel
from src.config.email import sendEmail
import src.controllers.session as user
import hashlib
import os

SHORTLINKMODEL= shortLinkModel()
USERMODEL = userModel()
dataSignUp = {}
@app.route('/User/logIn', methods=['GET','POST'])
def logIn():
    if request.method == 'GET':
        return render_template('LogIn/logIn.html')
    name = request.form.get('username')
    password = request.form.get('password')
    h = hashlib.new('md5', password.encode('utf8'))
    dataLogIn = {
        'name': name,
        'password': h.hexdigest()
    }
    into = USERMODEL.logIn(dataLogIn)
    if(into==None):
        flash('correo y contrasena no coinsiden', 'error')
        return redirect(url_for('logIn'))
    user.session['user'] = into
    links = SHORTLINKMODEL.dataUser(user.session)
    return redirect(url_for('index'))

@app.route('/User/signUp', methods=['GET','POST'])
def signUp():
    if request.method == 'GET':
        return render_template('LogIn/signUp.html')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    h = hashlib.new('md5', password.encode('utf8'))
    global dataSignUp
    dataSignUp = {
        'name': name,
        'email': email,
        'password': h.hexdigest()
    }
    sendEmail(email)
    try:
        USERMODEL.uniqueEmail(dataSignUp['name'])
    except:
        flash('El correo electronico ya se encuentra registrado', 'error')
        return redirect(url_for('signUp'))
    flash('Asegurese de confirmar el registro en su correo', 'success')
    return redirect(url_for('logIn'))

@app.route('/User/logOut')
def logOut():
    user.session.clear()
    return redirect(url_for('index'))

@app.route('/User/deleteLink/<link>')
def deleteLink(link):
    USERMODEL.deleteLink(link,user.session['user'])
    return redirect(url_for('index'))

@app.route('/User/editLink/<link>', methods=['GET','POST'])
def editLink(link):
    linkFull = SHORTLINKMODEL.findLink(link)
    if request.method == 'GET':
        linksUser = SHORTLINKMODEL.dataUser(user.session)
        return render_template('index.html', linksUser = linksUser, session = user.session, link = linkFull )
    data = {
        'id': linkFull[0],
        'shortlink': request.form.get('shortlink'),
        'link': request.form.get('link')
    }
    USERMODEL.editLink(data)
    linksUser = SHORTLINKMODEL.dataUser(user.session)
    return render_template('index.html', linksUser = linksUser, session = user.session )

@app.route('/User/confirm/registration/<int:ban>', methods=['GET','POST'])
def confirmRegistration(ban):
    if(ban==1): 
        try:
            USERMODEL.signUp(dataSignUp)
        except:
            flash('ocurrio un error en la confirmacion de su registro', 'error')
            return redirect(url_for('signUp'))
        flash('Registro confirmado con exito', 'success')
        return redirect(url_for('logIn'))   
    flash('Registro no confirmado', 'error')
    return redirect(url_for('signUp'))
   