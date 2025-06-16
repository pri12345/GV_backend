class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev-secret-key'  # Change this in production 