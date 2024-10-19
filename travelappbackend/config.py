import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://gideon:gidygiddy@localhost:5432/traveljournal')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://gideon:zilla@localhost:5432/traveljournal')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
