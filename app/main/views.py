from email import message
from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import Blog, User
from .forms import UpdateProfile, BlogForm
from .. import db, photos
from ..requests import quotes
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    displays = quotes()


    return render_template('index.html', displays = displays )


@main.route('/user/<uname>')
def profile (uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)



    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





@main.route ('/blog/new', methods = ['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit ():
        blogger_name = form.name.data
        blog_context = form.message.data

        #update review instance
        new_blog = Blog(blogger_name = blogger_name, blog_context= blog_context)


        #save review methods
        new_blog.save_blog()
        return redirect (url_for('main.blog'))

    else: all_blogs = Blog.query.order_by(Blog.posted).all


    return render_template('new_blog.html',blog_form = form, blogs = all_blogs)  

@main.route('/blog', methods= ['GET','POST'])
@login_required
def blog ():
    '''
    displays the written stories of all, after the click 'ReadMore' on the snippet tab.
    '''
    blogs = Blog.query.all()

    return render_template ('blog.html', blogs = blogs)  
        

