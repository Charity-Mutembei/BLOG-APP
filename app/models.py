from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path= db.Column(db.String())
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    

    @property
    def password (self):
        raise AttributeError('You cannot read the pass word attribute')


    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure, password)    


    def __repr__(self):
        return f'user{self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    all_blogs = []

    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer)
    blog_title = db.Column(db.String)
    image_path = db.Column(db.String)
    blog_title = db.Column(db.String)
    blogger_name = db.Column (db.String)
    blog_context = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

        Blog.all_blogs.append(self)

    @classmethod
    def get_blogs(cls,id):

        response = []
         
        for blog in cls.all_blogs:
            if blog.user_id == id:
                response.append(blog)


    def __repr__(self):
        return f'Blog{self.blog_title}'


class Quote:

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


  