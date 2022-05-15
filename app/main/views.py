from flask import render_template,request,redirect,url_for
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/snippet')
def snippet():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('snippet.html')
