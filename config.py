import os

class Config:
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
   pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
