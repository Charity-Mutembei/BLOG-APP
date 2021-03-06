import os

class Config:
    
    UPLOADED_PHOTOS_DEST = '/app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charity:naturelove@localhost/charity'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY= 'charity'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charity:naturelove@localhost/charity'


    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}
