from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)  # Increased length for stronger hashing
    is_admin = db.Column(db.Boolean, default=False)
    has_advanced_access = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    quizzes_taken = db.relationship('QuizResult', backref='user', lazy=True)

    __table_args__ = (
        db.UniqueConstraint('username', name='uq_user_username'),
        db.UniqueConstraint('email', name='uq_user_email'),
    )

    def set_password(self, password):
        """Hash and set the user's password."""
        if not self._is_valid_password(password):
            raise ValueError("Password does not meet security requirements")
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256:600000')

    def check_password(self, password):
        """Check if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)

    def _is_valid_password(self, password):
        """Check if password meets security requirements."""
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):  # At least one uppercase letter
            return False
        if not re.search(r'[a-z]', password):  # At least one lowercase letter
            return False
        if not re.search(r'\d', password):     # At least one digit
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # At least one special character
            return False
        return True

    def get_password_requirements(self):
        """Return password requirements for user feedback."""
        return {
            'min_length': 8,
            'requires_uppercase': True,
            'requires_lowercase': True,
            'requires_digit': True,
            'requires_special': True
        }

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    is_advanced = db.Column(db.Boolean, default=False)  # New field to mark advanced quizzes
    time_limit = db.Column(db.Integer, default=0)  # Time limit in minutes (0 for no limit)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref='quiz', lazy=True)
    results = db.relationship('QuizResult', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    points = db.Column(db.Integer, default=1)

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    user_answers = db.Column(db.Text)  # Store user's answers as JSON
    completed_at = db.Column(db.DateTime, default=datetime.utcnow) 