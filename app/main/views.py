from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required
from ..models import User

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


@main.route('/user/<uname>')
def profile (uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)



    return render_template('profile/profile.html', user = user)

@main.route ('/blog/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_blog(id):
    pass

