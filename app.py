from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from models import db, User, Quiz, Question, QuizResult
from forms import LoginForm, RegistrationForm, QuizForm, QuestionForm
from config import Config
import os
import json

app = Flask(__name__)
app.config.from_object(Config)

# Recommendations for advanced subjects
RECOMMENDATIONS = {
    'Mathematics': [
        {'title': 'Khan Academy - Basic Math', 'url': 'https://www.khanacademy.org/math/arithmetic'},
        {'title': 'SplashLearn - Math Games', 'url': 'https://www.splashlearn.com/math-games'}
    ],
    'Advanced Mathematics': [
        {'title': 'Khan Academy - Advanced Math', 'url': 'https://www.khanacademy.org/math/advanced-math'},
        {'title': 'MIT OpenCourseWare - Calculus', 'url': 'https://ocw.mit.edu/courses/mathematics/'}
    ],
    'Science': [
        {'title': 'National Geographic Kids Science', 'url': 'https://kids.nationalgeographic.com/science'},
        {'title': 'Science Kids - Experiments', 'url': 'https://www.sciencekids.co.nz/experiments.html'}
    ],
    'Advanced Science': [
        {'title': 'Coursera - Science Courses', 'url': 'https://www.coursera.org/courses?query=science'},
        {'title': 'edX - Biology & Chemistry', 'url': 'https://www.edx.org/learn/biology'}
    ],
    'Python Basics': [
        {'title': 'Python.org Documentation', 'url': 'https://docs.python.org/3/'},
        {'title': 'Codecademy - Learn Python', 'url': 'https://www.codecademy.com/learn/learn-python-3'}
    ],
    'Advanced Python': [
        {'title': 'Real Python', 'url': 'https://realpython.com/'},
        {'title': 'PyLadies Tutorials', 'url': 'https://pyladies.com/tutorials/'}
    ],
    'Web Development': [
        {'title': 'MDN Web Docs', 'url': 'https://developer.mozilla.org/en-US/docs/Web'},
        {'title': 'freeCodeCamp', 'url': 'https://www.freecodecamp.org/'}
    ],
    'Advanced Web Development': [
        {'title': 'Smashing Magazine', 'url': 'https://www.smashingmagazine.com/'},
        {'title': 'CSS-Tricks', 'url': 'https://css-tricks.com/'}
    ],
    'General Knowledge': [
        {'title': 'National Geographic Quizzes', 'url': 'https://www.nationalgeographic.com/pages/topic/quizzes'},
        {'title': 'Encyclopedia Britannica Kids', 'url': 'https://kids.britannica.com/'}
    ],
    'Advanced General Knowledge': [
        {'title': 'TED Talks - Global Issues', 'url': 'https://www.ted.com/topics/global-issues'},
        {'title': 'The Economist', 'url': 'https://www.economist.com/'}
    ],
    'Social Studies': [
        {'title': 'History.com', 'url': 'https://www.history.com/'},
        {'title': 'National Geographic Education', 'url': 'https://www.nationalgeographic.org/education/'}
    ],
    'Advanced Social Studies': [
        {'title': 'Council on Foreign Relations', 'url': 'https://www.cfr.org/'},
        {'title': 'JSTOR Daily - Social Sciences', 'url': 'https://daily.jstor.org/category/social-sciences/'}
    ],
    'Psychology': [
        {'title': 'Simply Psychology', 'url': 'https://www.simplypsychology.org/'},
        {'title': 'American Psychological Association', 'url': 'https://www.apa.org/help/understanding-psychology'}
    ],
    'Advanced Psychology': [
        {'title': 'Psychology Today', 'url': 'https://www.psychologytoday.com/us'},
        {'title': 'Annual Review of Psychology', 'url': 'https://www.annualreviews.org/journal/psych'}
    ],
    'Sports Basics': [
        {'title': 'ESPN Sports', 'url': 'https://www.espn.com/'},
        {'title': 'BBC Sport', 'url': 'https://www.bbc.com/sport'}
    ],
    'Advanced Sports': [
        {'title': 'Sports Illustrated', 'url': 'https://www.si.com/'},
        {'title': 'The Athletic', 'url': 'https://theathletic.com/'}
    ],
    'Nepali Language Basics': [
        {'title': 'Nepali Language Learning Apps', 'url': 'https://play.google.com/store/search?q=learn%20nepali&c=apps&hl=en_US'},
        {'title': 'Online Nepali Dictionary', 'url': 'https://www.lexilogos.com/english/nepali_dictionary.htm'}
    ],
    'Advanced Nepali Language & Literature': [
        {'title': 'Madan Puraskar Pustakalaya (Nepali Literature Archive)', 'url': 'http://madanpuraskar.org/'},
        {'title': 'Nepali Sahitya (Nepali Literature)', 'url': 'https://nepalisahitya.com/'}
    ],
    'Dramas & Theater Basics': [
        {'title': 'Broadway.com', 'url': 'https://www.broadway.com/'},
        {'title': 'The National Theatre (UK)', 'url': 'https://www.nationaltheatre.org.uk/'}
    ],
    'Advanced Dramas & Theater': [
        {'title': 'American Theatre Magazine', 'url': 'https://www.americantheatre.org/'},
        {'title': 'Drama Online', 'url': 'https://www.dramaonlinelibrary.com/'}
    ],
    'Entertainment Basics': [
        {'title': 'IMDb - Movies, TV & Celebrities', 'url': 'https://www.imdb.com/'},
        {'title': 'Rotten Tomatoes - Movie & TV Reviews', 'url': 'https://www.rottentomatoes.com/'}
    ],
    'Advanced Entertainment Industry': [
        {'title': 'Variety - Entertainment News', 'url': 'https://variety.com/'},
        {'title': 'The Hollywood Reporter', 'url': 'https://www.hollywoodreporter.com/'}
    ]
}

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    logout_user()
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            if 'uq_user_username' in str(e):
                flash('Username already taken. Please choose a different one.', 'danger')
            elif 'uq_user_email' in str(e):
                flash('Email already registered. Please use a different one.', 'danger')
            else:
                flash('An error occurred during registration. Please try again.', 'danger')
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    show_advanced_only = request.args.get('show_advanced', 'False') == 'True'

    if show_advanced_only:
        quizzes = Quiz.query.filter_by(is_advanced=True).all()
    else:
        quizzes = Quiz.query.filter_by(is_advanced=False).all()

    recent_results = sorted(current_user.quizzes_taken, key=lambda r: r.completed_at, reverse=True)[:5]
    return render_template('dashboard.html', quizzes=quizzes, recent_results=recent_results)

@app.route('/quiz/<int:quiz_id>/start')
@login_required
def start_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>')
@login_required
def quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz.html', quiz=quiz)

@app.route('/submit_quiz/<int:quiz_id>', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    score = 0
    total_questions = len(quiz.questions)
    user_answers_dict = {}

    for question in quiz.questions:
        answer = request.form.get(f'question_{question.id}')
        user_answers_dict[str(question.id)] = answer  # Store user's answer
        if answer == question.correct_answer:
            score += question.points
    
    result = QuizResult(
        user_id=current_user.id,
        quiz_id=quiz_id,
        score=score,
        total_questions=total_questions,
        user_answers=json.dumps(user_answers_dict) # Store answers as JSON string
    )
    db.session.add(result)
    db.session.commit()

    score_percentage = (score / total_questions) * 100 if total_questions > 0 else 0

    unlocked_advanced_this_time = False
    # Check if user passed a regular quiz to unlock advanced access
    if not quiz.is_advanced and score_percentage >= 50:
        if not current_user.has_advanced_access:
            current_user.has_advanced_access = True
            db.session.commit()
            flash('Congratulations! You\'ve unlocked advanced quizzes!', 'info')
            unlocked_advanced_this_time = True

    # Check for recommendations if it's an advanced quiz and user passed
    recommendations = []
    if quiz.title in RECOMMENDATIONS:
        recommendations = RECOMMENDATIONS[quiz.title]

    return redirect(url_for('result', result_id=result.id, unlocked_advanced=unlocked_advanced_this_time))

@app.route('/result/<int:result_id>')
@login_required
def result(result_id):
    result = QuizResult.query.get_or_404(result_id)
    quiz = Quiz.query.get_or_404(result.quiz_id)
    user_answers = json.loads(result.user_answers) if result.user_answers else {}
    unlocked_advanced = request.args.get('unlocked_advanced', 'False') == 'True'

    # Calculate score_percentage for display on the result page
    score_percentage = (result.score / result.total_questions) * 100 if result.total_questions > 0 else 0

    # Check for recommendations
    recommendations = []
    # Provide recommendations if the quiz title (or its base subject) matches a key in RECOMMENDATIONS
    # This logic now applies to both basic and advanced quizzes.
    if quiz.title in RECOMMENDATIONS:
        recommendations = RECOMMENDATIONS[quiz.title]
    else:
        # Try to find a base subject if it's an advanced quiz, e.g., "Advanced Science" -> "Science"
        # Or if it's a basic quiz with a specific suffix, e.g., "Python Basics" -> "Python"
        base_quiz_title = quiz.title
        if base_quiz_title.startswith("Advanced "):
            base_quiz_title = base_quiz_title.replace("Advanced ", "")
        elif base_quiz_title.endswith(" Basics"):
            base_quiz_title = base_quiz_title.replace(" Basics", "")

        if base_quiz_title in RECOMMENDATIONS:
            recommendations = RECOMMENDATIONS[base_quiz_title]
    
    # Fetch all quizzes to enable linking to advanced quizzes
    quizzes = Quiz.query.all()

    print(f"DEBUG: score_percentage={score_percentage}, user_has_advanced_access={current_user.has_advanced_access}, unlocked_advanced={unlocked_advanced}")
    return render_template('result.html',
                           result=result,
                           quiz=quiz,
                           user_answers=user_answers,
                           recommendations=recommendations,
                           unlocked_advanced=unlocked_advanced,
                           user_has_advanced_access=current_user.has_advanced_access,
                           score_percentage=score_percentage,
                           quizzes=quizzes) # Pass quizzes to the template

# Admin routes
@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    users = User.query.all()
    quizzes = Quiz.query.all()
    questions = Question.query.all()
    return render_template('admin/admin_dashboard.html', users=users, quizzes=quizzes, questions=questions)

@app.route('/admin/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    form = QuestionForm()
    quizzes = Quiz.query.all()
    form.quiz_id.choices = [(quiz.id, quiz.title) for quiz in quizzes]
    if form.validate_on_submit():
        question = Question(
            quiz_id=form.quiz_id.data,
            question_text=form.question_text.data,
            option_a=form.option_a.data,
            option_b=form.option_b.data,
            option_c=form.option_c.data,
            option_d=form.option_d.data,
            correct_answer=form.correct_answer.data,
            points=form.points.data
        )
        db.session.add(question)
        db.session.commit()
        flash('Question added successfully!')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/add_question.html', form=form)

@app.route('/admin/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))
    form = QuizForm()
    if form.validate_on_submit():
        new_quiz = Quiz(
            title=form.title.data,
            description=form.description.data,
            creator_id=current_user.id,
            time_limit=form.time_limit.data,
            is_advanced=form.is_advanced.data
        )
        db.session.add(new_quiz)
        db.session.commit()
        flash('Quiz created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/create_quiz.html', form=form)

@app.route('/search')
def search():
    query = request.args.get('query')
    quizzes = []
    questions = []
    search_performed = False

    if query:
        search_performed = True
        # Search quizzes by title or description
        quizzes = Quiz.query.filter(
            (Quiz.title.ilike(f'%{query}%')) | 
            (Quiz.description.ilike(f'%{query}%'))
        ).all()

        # Search questions by question text
        questions = Question.query.filter(
            Question.question_text.ilike(f'%{query}%')
        ).all()

    return render_template('search.html', 
                           quizzes=quizzes, 
                           questions=questions, 
                           search_performed=search_performed)

if __name__ == '__main__':
    app.run(debug=True) 