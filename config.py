import os
from datetime import timedelta

class Config:
    # Basic Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    
    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session config
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # Upload config
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size 