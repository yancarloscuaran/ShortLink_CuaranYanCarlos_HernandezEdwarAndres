from flask import render_template, request, redirect, url_for, flash
from src import app
from string import ascii_letters, digits
from random import choice
import src.controllers.session as user
from src.models.acortador import shortLinkModel
import os

@app.context_processor  
def utility_processor(): 
    def example(arr): 
        return len(arr)
    return dict(myexample=example)

@app.route('/', methods=['GET','POST'])
def index():
    linkModel = shortLinkModel()
    if request.method == 'GET':
        linksUser = linkModel.dataUser(user.session)
        return render_template('index.html', linksUser = linksUser, session = user.session )
    flash('Enlace generado correctamente', 'success')
    url = request.form.get('link') 
    shortLink = ''.join([choice(ascii_letters + digits) for i in range(4)])
    if not 'user' in user.session:
        Data = {
        'link': url,
        'shortlink': shortLink,
        'user_id': 1
        }
    else:

        Data = {
            'link': url,
            'shortlink': shortLink,
            'user_id': user.session['user'][0]
        }
    linkModel.saveData(Data)
    linksUser = linkModel.dataUser(user.session)
    shortLink = 'localhost:5000/'+ shortLink
    return render_template('index.html', shortLink = shortLink, session = user.session, linksUser = linksUser)

@app.route('/<link>')
def find(link):
    linkModel = shortLinkModel()
    links = linkModel.findLink(link)
    if (links==None):
        return redirect(url_for('index'))
    return redirect(links[2])

