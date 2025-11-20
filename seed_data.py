from app import app, db
from models import User, Quiz, Question
from werkzeug.security import generate_password_hash

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create admin user
        admin = User(
            username='admin',
            email='admin@quizora.com',
            password_hash=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        # Retrieve the admin user to ensure their ID is populated
        admin = User.query.filter_by(username='admin').first()

        # Create regular user
        user = User(
            username='user',
            email='user@quizora.com',
            password_hash=generate_password_hash('user123'),
            is_admin=False
        )
        db.session.add(user)
        db.session.commit()

        # Create basic quizzes
        python_quiz = Quiz(
            title='Python Basics',
            description='Test your knowledge of Python programming fundamentals.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(python_quiz)

        web_quiz = Quiz(
            title='Web Development',
            description='Quiz about HTML, CSS, and JavaScript basics.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(web_quiz)

        math_quiz = Quiz(
            title='Mathematics',
            description='Challenge yourself with basic math questions.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(math_quiz)

        gk_quiz = Quiz(
            title='General Knowledge',
            description='Test your general knowledge across a variety of topics.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(gk_quiz)

        social_quiz = Quiz(
            title='Social Studies',
            description='Questions about history, geography, and civics.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(social_quiz)

        psychology_quiz = Quiz(
            title='Psychology',
            description='Explore the basics of psychology and human behavior.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(psychology_quiz)

        science_quiz = Quiz(
            title='Science',
            description='Test your knowledge in physics, chemistry, and biology.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(science_quiz)

        # New Basic Subjects
        sports_basic_quiz = Quiz(
            title='Sports Basics',
            description='Basic questions about various sports and their rules.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(sports_basic_quiz)

        nepali_basic_quiz = Quiz(
            title='Nepali Language Basics',
            description='Basic quiz on Nepali language fundamentals and common phrases.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(nepali_basic_quiz)

        dramas_basic_quiz = Quiz(
            title='Dramas & Theater Basics',
            description='Basic questions about popular dramas and theater terms.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(dramas_basic_quiz)

        entertainment_basic_quiz = Quiz(
            title='Entertainment Basics',
            description='Basic questions on popular movies, music, and TV shows.',
            creator_id=admin.id,
            is_advanced=False
        )
        db.session.add(entertainment_basic_quiz)

        # Create advanced quizzes
        advanced_python_quiz = Quiz(
            title='Advanced Python',
            description='In-depth questions on advanced Python concepts.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_python_quiz)

        advanced_web_quiz = Quiz(
            title='Advanced Web Development',
            description='Advanced concepts in modern web technologies.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_web_quiz)

        advanced_math_quiz = Quiz(
            title='Advanced Mathematics',
            description='Challenging problems in calculus, algebra, and more.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_math_quiz)

        advanced_gk_quiz = Quiz(
            title='Advanced General Knowledge',
            description='Deep dive into diverse and complex general knowledge topics.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_gk_quiz)

        advanced_social_quiz = Quiz(
            title='Advanced Social Studies',
            description='Complex questions on global history, political science, and economics.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_social_quiz)

        advanced_psychology_quiz = Quiz(
            title='Advanced Psychology',
            description='Detailed questions on psychological theories and research methods.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_psychology_quiz)

        advanced_science_quiz = Quiz(
            title='Advanced Science',
            description='Explore complex topics in advanced physics, chemistry, and biology.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(advanced_science_quiz)

        # Advanced versions of newly added subjects
        sports_advanced_quiz = Quiz(
            title='Advanced Sports',
            description='In-depth questions about sports strategies, history, and records.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(sports_advanced_quiz)

        nepali_advanced_quiz = Quiz(
            title='Advanced Nepali Language & Literature',
            description='Complex questions on Nepali grammar, classical literature, and nuanced cultural aspects.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(nepali_advanced_quiz)

        dramas_advanced_quiz = Quiz(
            title='Advanced Dramas & Theater',
            description='Scholarly questions on dramatic theories, playwrights, and theater movements.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(dramas_advanced_quiz)

        entertainment_advanced_quiz = Quiz(
            title='Advanced Entertainment Industry',
            description='Detailed questions on industry trends, iconic figures, and artistic movements.',
            creator_id=admin.id,
            is_advanced=True
        )
        db.session.add(entertainment_advanced_quiz)

        db.session.commit() # Commit quizzes to get their IDs

        # Create questions for Python quiz (Basic)
        python_questions = [
            Question(
                quiz=python_quiz,
                question_text='What is the correct way to create a function in Python?',
                option_a='function myFunc():',
                option_b='def myFunc():',
                option_c='create myFunc():',
                option_d='new myFunc():',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='Which of the following is NOT a Python data type?',
                option_a='List',
                option_b='Dictionary',
                option_c='Array',
                option_d='Tuple',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='What is the output of print(type([]))?',
                option_a='<class "array">',
                option_b='<class "list">',
                option_c='<class "tuple">',
                option_d='<class "set">',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='Which keyword is used to start a loop in Python?',
                option_a='for',
                option_b='loop',
                option_c='iterate',
                option_d='repeat',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='How do you insert COMMENTS in Python code?',
                option_a='// This is a comment',
                option_b='/* This is a comment */',
                option_c='# This is a comment',
                option_d='-- This is a comment',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='Which method can be used to remove whitespace from the beginning and the end of a string?',
                option_a='strip()',
                option_b='trim()',
                option_c='remove()',
                option_d='clean()',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='What is the output of: print(2 ** 3)?',
                option_a='6',
                option_b='8',
                option_c='9',
                option_d='5',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='Which of the following is used to define a block of code in Python?',
                option_a='Curly braces {}',
                option_b='Parentheses ()',
                option_c='Indentation',
                option_d='Quotation marks',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='What is the output of: print("Hello" + str(5))?',
                option_a='Hello5',
                option_b='Hello 5',
                option_c='Error',
                option_d='5Hello',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=python_quiz,
                question_text='Which of the following is a mutable data type in Python?',
                option_a='Tuple',
                option_b='String',
                option_c='List',
                option_d='Integer',
                correct_answer='C',
                points=1
            )
        ]

        # Create questions for Advanced Python quiz
        advanced_python_questions = [
            Question(
                quiz=advanced_python_quiz,
                question_text='What is the time complexity of a binary search algorithm?',
                option_a='O(n)',
                option_b='O(log n)',
                option_c='O(n log n)',
                option_d='O(1)',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_python_quiz,
                question_text='Which of the following is NOT a valid use of Python decorators?',
                option_a='Function memoization',
                option_b='Access control',
                option_c='Variable declaration',
                option_d='Logging',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_python_quiz,
                question_text='What is the output of the following code?\nfrom functools import partial\ndef multiply(x, y):\n    return x * y\ndouble = partial(multiply, 2)\nprint(double(4))',
                option_a='4',
                option_b='8',
                option_c='16',
                option_d='Error',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_python_quiz,
                question_text='Which of the following is true about Python\'s GIL (Global Interpreter Lock)?',
                option_a='It allows multiple threads to execute Python code simultaneously',
                option_b='It prevents multiple threads from executing Python code simultaneously',
                option_c='It only affects multiprocessing, not threading',
                option_d='It can be disabled for better performance',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_python_quiz,
                question_text='What is the purpose of __slots__ in Python classes?',
                option_a='To define class methods',
                option_b='To restrict attribute creation and save memory',
                option_c='To create read-only attributes',
                option_d='To implement multiple inheritance',
                correct_answer='B',
                points=2
            )
        ]

        # Create questions for Web Development quiz (Basic)
        web_questions = [
            Question(
                quiz=web_quiz,
                question_text='What does HTML stand for?',
                option_a='Hyper Text Markup Language',
                option_b='High Tech Modern Language',
                option_c='Hyper Transfer Markup Language',
                option_d='Hyper Text Modern Language',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which CSS property is used to change the text color?',
                option_a='text-color',
                option_b='font-color',
                option_c='color',
                option_d='text-style',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which of the following is NOT a JavaScript framework?',
                option_a='React',
                option_b='Angular',
                option_c='Django',
                option_d='Vue',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which HTML tag is used to create a hyperlink?',
                option_a='<a>',
                option_b='<link>',
                option_c='<href>',
                option_d='<hyperlink>',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which property is used to change the background color in CSS?',
                option_a='color',
                option_b='background-color',
                option_c='bgcolor',
                option_d='background',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which symbol is used for IDs in CSS selectors?',
                option_a='.',
                option_b='#',
                option_c='*',
                option_d='&',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which JavaScript keyword is used to declare a variable?',
                option_a='var',
                option_b='int',
                option_c='let',
                option_d='Both A and C',
                correct_answer='D',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which HTML tag is used to display a picture on a webpage?',
                option_a='<img>',
                option_b='<img>',
                option_c='<pic>',
                option_d='<picture>',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='Which CSS property controls the spacing between lines of text?',
                option_a='line-spacing',
                option_b='letter-spacing',
                option_c='line-height',
                option_d='text-spacing',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=web_quiz,
                question_text='What is the purpose of the `alt` attribute in an `<img>` tag?',
                option_a='To define the image source',
                option_b='To provide alternative text for the image',
                option_c='To set the image alignment',
                option_d='To specify the image dimensions',
                correct_answer='B',
                points=1
            )
        ]

        # Create questions for Advanced Web Development quiz
        advanced_web_questions = [
            Question(
                quiz=advanced_web_quiz,
                question_text='What is the main difference between HTTP/2 and HTTP/1.1?',
                option_a='HTTP/2 uses binary protocol while HTTP/1.1 uses text',
                option_b='HTTP/2 only works with HTTPS',
                option_c='HTTP/2 doesn\'t support cookies',
                option_d='HTTP/2 can\'t handle multiple requests',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_web_quiz,
                question_text='Which of these is NOT a valid use case for Web Workers?',
                option_a='CPU-intensive calculations',
                option_b='Real-time data processing',
                option_c='DOM manipulation',
                option_d='Image processing',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_web_quiz,
                question_text='What is the purpose of the Intersection Observer API?',
                option_a='To detect when elements enter the viewport',
                option_b='To handle mouse intersections',
                option_c='To manage CSS transitions',
                option_d='To create 3D effects',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_web_quiz,
                question_text='Which of these is NOT a valid way to optimize web performance?',
                option_a='Using HTTP/2',
                option_b='Implementing service workers',
                option_c='Loading all scripts synchronously',
                option_d='Using CDN for static assets',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_web_quiz,
                question_text='What is the main advantage of using CSS Grid over Flexbox?',
                option_a='Grid can handle both rows and columns simultaneously',
                option_b='Grid is more performant',
                option_c='Grid has better browser support',
                option_d='Grid is easier to learn',
                correct_answer='A',
                points=2
            )
        ]

        # Create questions for Mathematics quiz (Basic)
        math_questions = [
            Question(
                quiz=math_quiz,
                question_text='What is the value of Pi (π) to two decimal places?',
                option_a='3.14',
                option_b='3.16',
                option_c='3.12',
                option_d='3.18',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is the square root of 144?',
                option_a='10',
                option_b='11',
                option_c='12',
                option_d='13',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What type of triangle has all sides of equal length?',
                option_a='Scalene',
                option_b='Isosceles',
                option_c='Equilateral',
                option_d='Right',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is the sum of angles in a triangle?',
                option_a='90 degrees',
                option_b='180 degrees',
                option_c='270 degrees',
                option_d='360 degrees',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is the formula for the area of a circle?',
                option_a='2πr',
                option_b='πr²',
                option_c='πd',
                option_d='2πd',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is 7 multiplied by 8?',
                option_a='49',
                option_b='56',
                option_c='63',
                option_d='72',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='How many sides does a hexagon have?',
                option_a='5',
                option_b='6',
                option_c='7',
                option_d='8',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is the next number in the sequence: 1, 1, 2, 3, 5, 8, ...?',
                option_a='11',
                option_b='12',
                option_c='13',
                option_d='14',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is the derivative of f(x) = x^2 with respect to x?',
                option_a='x',
                option_b='2x',
                option_c='x^3/3',
                option_d='2',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=math_quiz,
                question_text='What is 25% of 200?',
                option_a='25',
                option_b='50',
                option_c='75',
                option_d='100',
                correct_answer='B',
                points=1
            )
        ]

        # Create questions for Advanced Mathematics quiz
        advanced_math_questions = [
            Question(
                quiz=advanced_math_quiz,
                question_text='What is the value of the Riemann zeta function at s=2?',
                option_a='π²/6',
                option_b='π/4',
                option_c='e²',
                option_d='√2',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_math_quiz,
                question_text='Which of these is NOT a valid proof technique in mathematics?',
                option_a='Proof by contradiction',
                option_b='Proof by induction',
                option_c='Proof by assumption',
                option_d='Proof by construction',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_math_quiz,
                question_text='What is the fundamental theorem of calculus?',
                option_a='It relates derivatives and integrals',
                option_b='It defines the concept of limits',
                option_c='It proves the existence of real numbers',
                option_d='It establishes the rules of differentiation',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_math_quiz,
                question_text='In group theory, what is a normal subgroup?',
                option_a='A subgroup that is closed under conjugation',
                option_b='A subgroup with an even number of elements',
                option_c='A subgroup that contains the identity element',
                option_d='A subgroup that is commutative',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_math_quiz,
                question_text='What is the significance of the Euler-Mascheroni constant?',
                option_a='It appears in the study of harmonic series',
                option_b='It defines the golden ratio',
                option_c='It is the base of natural logarithms',
                option_d='It represents the ratio of a circle\'s circumference to its diameter',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_math_questions)

        # Create questions for General Knowledge quiz (Basic)
        gk_questions = [
            Question(
                quiz=gk_quiz,
                question_text='What is the capital of France?',
                option_a='Berlin',
                option_b='Madrid',
                option_c='Paris',
                option_d='Rome',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='Which planet is known as the "Red Planet"?',
                option_a='Earth',
                option_b='Mars',
                option_c='Jupiter',
                option_d='Venus',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='Who painted the Mona Lisa?',
                option_a='Vincent van Gogh',
                option_b='Leonardo da Vinci',
                option_c='Pablo Picasso',
                option_d='Claude Monet',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='What is the largest ocean on Earth?',
                option_a='Atlantic Ocean',
                option_b='Indian Ocean',
                option_c='Arctic Ocean',
                option_d='Pacific Ocean',
                correct_answer='D',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='How many continents are there?',
                option_a='5',
                option_b='6',
                option_c='7',
                option_d='8',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='What is the chemical symbol for water?',
                option_a='O2',
                option_b='H2O',
                option_c='CO2',
                option_d='NaCl',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='Which country is famous for the Great Wall?',
                option_a='Japan',
                option_b='China',
                option_c='India',
                option_d='Egypt',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='What is the hardest natural substance on Earth?',
                option_a='Gold',
                option_b='Iron',
                option_c='Diamond',
                option_d='Quartz',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='Who wrote "Romeo and Juliet"?',
                option_a='Charles Dickens',
                option_b='William Shakespeare',
                option_c='Jane Austen',
                option_d='Mark Twain',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=gk_quiz,
                question_text='What is the capital of Japan?',
                option_a='Beijing',
                option_b='Seoul',
                option_c='Tokyo',
                option_d='Bangkok',
                correct_answer='C',
                points=1
            )
        ]

        # Create questions for Advanced General Knowledge quiz
        advanced_gk_questions = [
            Question(
                quiz=advanced_gk_quiz,
                question_text='Which ancient civilization developed the concept of zero?',
                option_a='Roman',
                option_b='Greek',
                option_c='Mayan',
                option_d='Babylonian',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='Who formulated the theory of relativity?',
                option_a='Isaac Newton',
                option_b='Galileo Galilei',
                option_c='Albert Einstein',
                option_d='Nikola Tesla',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='What is the largest artificial intelligence model by parameter count?',
                option_a='GPT-3',
                option_b='PaLM 2',
                option_c='LaMDA',
                option_d='DeepMind AlphaFold',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='Which philosopher is credited with the idea of the "categorical imperative"?',
                option_a='John Locke',
                option_b='Immanuel Kant',
                option_c='Friedrich Nietzsche',
                option_d='Plato',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='What is the main function of the World Trade Organization (WTO)?',
                option_a='To provide humanitarian aid globally.',
                option_b='To regulate international trade and resolve trade disputes.',
                option_c='To promote global health initiatives.',
                option_d='To fund developing countries\' infrastructure projects.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='Explain the concept of "Tragedy of the Commons."',
                option_a='A situation where individuals act independently and rationally according to their own self-interest, depleting a shared resource.',
                option_b='A dramatic play that ends in catastrophe.',
                option_c='A type of economic system where resources are communally owned.',
                option_d='A philosophical idea about the nature of human morality.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='Who is credited with inventing the printing press?',
                option_a='Johannes Gutenberg',
                option_b='Leonardo da Vinci',
                option_c='Isaac Newton',
                option_d='Benjamin Franklin',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='What is the significance of the Rosetta Stone?',
                option_a='It is a key that unlocked the understanding of Egyptian hieroglyphs.',
                option_b='It is an ancient map of the world.',
                option_c='It describes the rules of ancient Roman law.',
                option_d='It is a religious artifact from Mesopotamia.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_gk_quiz,
                question_text='Which event is considered the start of the modern scientific revolution?',
                option_a='The fall of the Roman Empire.',
                option_b='The publication of Nicolaus Copernicus\'s "De revolutionibus orbium coelestium"',
                option_c='The invention of the steam engine.',
                option_d='The discovery of America.',
                correct_answer='B',
                points=2
            )
        ]
        db.session.add_all(advanced_gk_questions)

        # Create questions for Social Studies quiz (Basic)
        social_questions = [
            Question(
                quiz=social_quiz,
                question_text='Who was the first President of the United States?',
                option_a='Abraham Lincoln',
                option_b='George Washington',
                option_c='Thomas Jefferson',
                option_d='John Adams',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='What is the longest river in the world?',
                option_a='Amazon River',
                option_b='Nile River',
                option_c='Yangtze River',
                option_d='Mississippi River',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='In which year did World War II end?',
                option_a='1942',
                option_b='1945',
                option_c='1918',
                option_d='1950',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='What is the capital city of Australia?',
                option_a='Sydney',
                option_b='Melbourne',
                option_c='Canberra',
                option_d='Perth',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='What document declared the American colonies independent from Great Britain?',
                option_a='The Constitution',
                option_b='The Bill of Rights',
                option_c='The Declaration of Independence',
                option_d='The Articles of Confederation',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='Which ancient civilization built the pyramids?',
                option_a='Roman',
                option_b='Greek',
                option_c='Egyptian',
                option_d='Inca',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='Who was Martin Luther King Jr.?',
                option_a='A famous musician',
                option_b='A civil rights leader',
                option_c='A renowned scientist',
                option_d='A former president',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='Which country is known as the "Land of the Rising Sun"?',
                option_a='China',
                option_b='South Korea',
                option_c='Japan',
                option_d='Thailand',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='What is the highest mountain in the world?',
                option_a='Mount Everest',
                option_b='K2',
                option_c='Mount Kilimanjaro',
                option_d='Mount Blanc',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=social_quiz,
                question_text='Which of the following is NOT a branch of the U.S. government?',
                option_a='Legislative',
                option_b='Executive',
                option_c='Military',
                option_d='Judicial',
                correct_answer='C',
                points=1
            )
        ]

        # Create questions for Advanced Social Studies quiz
        advanced_social_questions = [
            Question(
                quiz=advanced_social_quiz,
                question_text='What is the significance of the Bretton Woods Conference?',
                option_a='It established the post-World War II international monetary system',
                option_b='It ended the Cold War',
                option_c='It created the United Nations',
                option_d='It established free trade agreements',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_social_quiz,
                question_text='Which of these is NOT a principle of the Washington Consensus?',
                option_a='State ownership of major industries',
                option_b='Fiscal discipline',
                option_c='Trade liberalization',
                option_d='Market-determined interest rates',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_social_quiz,
                question_text='What is the main difference between Keynesian and Monetarist economic theories?',
                option_a='Keynesians emphasize government intervention while Monetarists focus on money supply',
                option_b='Keynesians support free markets while Monetarists prefer government control',
                option_c='Keynesians focus on supply while Monetarists focus on demand',
                option_d='Keynesians are modern while Monetarists are classical',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_social_quiz,
                question_text='What is the significance of the Treaty of Westphalia?',
                option_a='It established the modern concept of state sovereignty',
                option_b='It ended World War I',
                option_c='It created the European Union',
                option_d='It established colonial boundaries',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_social_quiz,
                question_text='Which of these is NOT a characteristic of a failed state?',
                option_a='Strong central government',
                option_b='Loss of control over territory',
                option_c='Inability to provide public services',
                option_d='Legitimacy crisis',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_social_questions)

        # Create questions for Psychology quiz (Basic)
        psychology_questions = [
            Question(
                quiz=psychology_quiz,
                question_text='Who is considered the "father of psychology"?',
                option_a='Sigmund Freud',
                option_b='B.F. Skinner',
                option_c='Wilhelm Wundt',
                option_d='Carl Rogers',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='Which psychological perspective emphasizes the unconscious mind?',
                option_a='Behaviorism',
                option_b='Cognitive Psychology',
                option_c='Psychodynamic Theory',
                option_d='Humanistic Psychology',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='What is the "Id" in Freud\'s theory of personality?',
                option_a='The moral component of personality',
                option_b='The rational, problem-solving component',
                option_c='The primitive, instinctual component',
                option_d='The part that mediates between the Id and Superego',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='Which of the following is a classical conditioning term?',
                option_a='Reinforcement',
                option_b='Punishment',
                option_c='Unconditioned Stimulus',
                option_d='Observational Learning',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='What is cognitive dissonance?',
                option_a='A type of memory disorder',
                option_b='Mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.',
                option_c='The inability to recognize familiar faces',
                option_d='A positive feeling towards a new idea',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='Who proposed the hierarchy of needs?',
                option_a='Carl Jung',
                option_b='Abraham Maslow',
                option_c='Ivan Pavlov',
                option_d='Jean Piaget',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='What is the primary focus of humanistic psychology?',
                option_a='Unconscious conflicts',
                option_b='Observable behaviors',
                option_c='Personal growth and self-actualization',
                option_d='Cognitive processes',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='Which part of the brain is responsible for memory formation?',
                option_a='Cerebellum',
                option_b='Brainstem',
                option_c='Hippocampus',
                option_d='Amygdala',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='What is the placebo effect?',
                option_a='A negative reaction to medication',
                option_b='A therapeutic effect resulting from a patient\'s belief in a treatment rather than from the treatment\'s inherent properties.',
                option_c='The diminishing of a conditioned response',
                option_d='A form of classical conditioning',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=psychology_quiz,
                question_text='Who developed the concept of the "collective unconscious"?',
                option_a='Sigmund Freud',
                option_b='Carl Jung',
                option_c='Alfred Adler',
                option_d='Erik Erikson',
                correct_answer='B',
                points=1
            )
        ]

        # Create questions for Advanced Psychology quiz
        advanced_psychology_questions = [
            Question(
                quiz=advanced_psychology_quiz,
                question_text='What is the main difference between classical and operant conditioning?',
                option_a='Classical conditioning involves involuntary responses while operant involves voluntary behavior',
                option_b='Classical conditioning is modern while operant is outdated',
                option_c='Classical conditioning works on animals while operant works on humans',
                option_d='Classical conditioning is faster than operant conditioning',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_psychology_quiz,
                question_text='Which of these is NOT a defense mechanism according to Freud?',
                option_a='Logical reasoning',
                option_b='Repression',
                option_c='Projection',
                option_d='Displacement',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_psychology_quiz,
                question_text='What is the significance of the Stanford Prison Experiment?',
                option_a='It demonstrated how social roles can influence behavior',
                option_b='It proved that prisons are necessary',
                option_c='It showed that people are naturally good',
                option_d='It demonstrated the effectiveness of rehabilitation',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_psychology_quiz,
                question_text='What is the main difference between Type A and Type B personality?',
                option_a='Type A is competitive and time-conscious while Type B is relaxed and patient',
                option_b='Type A is introverted while Type B is extroverted',
                option_c='Type A is emotional while Type B is rational',
                option_d='Type A is creative while Type B is analytical',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_psychology_quiz,
                question_text='Which of these is NOT a stage in Piaget\'s theory of cognitive development?',
                option_a='Social learning stage',
                option_b='Sensorimotor stage',
                option_c='Concrete operational stage',
                option_d='Formal operational stage',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_psychology_questions)

        # Create questions for Science quiz (Basic)
        science_questions = [
            Question(
                quiz=science_quiz,
                question_text='What is the chemical symbol for gold?',
                option_a='Ag',
                option_b='Au',
                option_c='Fe',
                option_d='Cu',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the process by which a liquid turns into a gas?',
                option_a='Melting',
                option_b='Freezing',
                option_c='Evaporation',
                option_d='Condensation',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='Which force keeps planets in orbit around the sun?',
                option_a='Electromagnetic force',
                option_b='Strong nuclear force',
                option_c='Gravity',
                option_d='Weak nuclear force',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the powerhouse of the cell?',
                option_a='Nucleus',
                option_b='Mitochondria',
                option_c='Ribosome',
                option_d='Endoplasmic Reticulum',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the chemical formula for carbon dioxide?',
                option_a='CO',
                option_b='CO2',
                option_c='C2O',
                option_d='H2CO3',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='Which gas do plants absorb from the atmosphere?',
                option_a='Oxygen',
                option_b='Nitrogen',
                option_c='Carbon Dioxide',
                option_d='Hydrogen',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the process of a solid turning directly into a gas?',
                option_a='Evaporation',
                option_b='Sublimation',
                option_c='Condensation',
                option_d='Melting',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the largest organ in the human body?',
                option_a='Heart',
                option_b='Brain',
                option_c='Skin',
                option_d='Liver',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='What is the pH of a neutral solution?',
                option_a='0',
                option_b='7',
                option_c='14',
                option_d='Depends on temperature',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=science_quiz,
                question_text='Which planet is closest to the Sun?',
                option_a='Venus',
                option_b='Earth',
                option_c='Mercury',
                option_d='Mars',
                correct_answer='C',
                points=1
            )
        ]

        # Create questions for Advanced Science quiz
        advanced_science_questions = [
            Question(
                quiz=advanced_science_quiz,
                question_text='Explain the concept of quantum entanglement and its implications.',
                option_a='A phenomenon where particles are linked and affect each other regardless of distance.',
                option_b='The process of particles merging into a single entity.',
                option_c='The behavior of particles at extremely high temperatures.',
                option_d='A classical physics concept describing wave interference.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='Describe the process of nuclear fission and its applications.',
                option_a='The fusion of two atomic nuclei to form a heavier nucleus, releasing energy.',
                option_b='The splitting of a heavy atomic nucleus into two or more smaller nuclei, releasing a large amount of energy, used in nuclear power and weapons.',
                option_c='A chemical reaction that produces heat and light.',
                option_d='The decay of radioactive isotopes over time.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='What is the role of ATP in biological systems?',
                option_a='It\'s a structural component of cell membranes.',
                option_b='It\'s the primary energy currency of the cell, used to power various cellular processes.',
                option_c='It\'s a genetic material that stores hereditary information.',
                option_d='It\'s a waste product of cellular respiration.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='Differentiate between DNA and RNA.',
                option_a='DNA is single-stranded; RNA is double-stranded.',
                option_b='DNA stores genetic information; RNA is involved in gene expression and protein synthesis.',
                option_c='DNA contains uracil; RNA contains thymine.',
                option_d='DNA is found in the cytoplasm; RNA is found in the nucleus.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='Explain the greenhouse effect and its primary drivers.',
                option_a='The cooling of Earth\'s atmosphere due to reduced solar radiation.',
                option_b='The process by which gases in Earth\'s atmosphere trap heat, warming the planet, primarily driven by CO2, methane, and N2O.',
                option_c='A phenomenon where ozone layer depletion causes increased UV radiation.',
                option_d='The process of converting solar energy into electrical energy.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='What is CRISPR-Cas9?',
                option_a='A type of antibiotic.',
                option_b='A revolutionary gene-editing tool.',
                option_c='A new telescope for space observation.',
                option_d='A method for creating synthetic elements.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='Describe the Big Bang theory.',
                option_a='The theory that the universe began from a very hot, dense state and has been expanding ever since.',
                option_b='A theory about the formation of black holes.',
                option_c='A theory explaining the origin of life on Earth.',
                option_d='The theory that the universe is static and unchanging.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='What is the principle of Occam\'s Razor?',
                option_a='The simplest explanation is usually the correct one.',
                option_b='Complexity is preferred over simplicity.',
                option_c='All theories must be proven empirically.',
                option_d='Knowledge is derived from experience.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=advanced_science_quiz,
                question_text='Explain the concept of natural selection with an example.',
                option_a='The process by which organisms better adapted to their environment tend to survive and produce more offspring. Example: Peppered moths.',
                option_b='The process of organisms intentionally changing their traits.',
                option_c='The deliberate breeding of organisms for desired traits.',
                option_d='The extinction of species due to human activity.',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_science_questions)

        # Create questions for Sports Basic quiz
        sports_basic_questions = [
            Question(
                quiz=sports_basic_quiz,
                question_text='How many players are on a soccer team?',
                option_a='9',
                option_b='10',
                option_c='11',
                option_d='12',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='Which country invented the sport of basketball?',
                option_a='Canada',
                option_b='United States',
                option_c='United Kingdom',
                option_d='China',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='What is the term for a perfect score in bowling?',
                option_a='Strike',
                option_b='Spare',
                option_c='300',
                option_d='Turkey',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='Which stroke is NOT used in competitive swimming?',
                option_a='Freestyle',
                option_b='Backstroke',
                option_c='Doggy Paddle',
                option_d='Butterfly',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='In tennis, what is it called when the score is 40-40?',
                option_a='Advantage',
                option_b='Deuce',
                option_c='Game point',
                option_d='Set point',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='Which martial art originated in Korea?',
                option_a='Karate',
                option_b='Judo',
                option_c='Taekwondo',
                option_d='Kung Fu',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='How many bases are there in a standard baseball game?',
                option_a='3',
                option_b='4',
                option_c='5',
                option_d='6',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='What equipment is essential for playing badminton?',
                option_a='Ball and bat',
                option_b='Shuttlecock and racket',
                option_c='Net and club',
                option_d='Puck and stick',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='Which famous athlete is known as "The Greatest" in boxing?',
                option_a='Mike Tyson',
                option_b='Muhammad Ali',
                option_c='Manny Pacquiao',
                option_d='Floyd Mayweather Jr.',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=sports_basic_quiz,
                question_text='What is the highest score possible in a single frame of ten-pin bowling?',
                option_a='10',
                option_b='20',
                option_c='30',
                option_d='40',
                correct_answer='C',
                points=1
            )
        ]

        # Create questions for Nepali Language Basics quiz
        nepali_basic_questions = [
            Question(
                quiz=nepali_basic_quiz,
                question_text='What does "Namaste" mean in English?',
                option_a='Goodbye',
                option_b='Thank you',
                option_c='Hello',
                option_d='How are you?',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='How do you say "water" in Nepali?',
                option_a='Pani',
                option_b='Khana',
                option_c='Ghar',
                option_d='Kitaab',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='Which is the national animal of Nepal?',
                option_a='Tiger',
                option_b='Cow',
                option_c='Elephant',
                option_d='Panda',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='What is "Dhanyabad" used for?',
                option_a='Asking for directions',
                option_b='Saying goodbye',
                option_c='Saying thank you',
                option_d='Greeting someone',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='Which mountain range is primarily located in Nepal?',
                option_a='Andes',
                option_b='Alps',
                option_c='Himalayas',
                option_d='Rockies',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='What is "Ramro" in English?',
                option_a='Bad',
                option_b='Good',
                option_c='Big',
                option_d='Small',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='Which major river flows through Nepal?',
                option_a='Ganges',
                option_b='Indus',
                option_c='Koshi',
                option_d='Brahmaputra',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='What is a "momo"?',
                option_a='A type of bread',
                option_b='A dumpling',
                option_c='A soup',
                option_d='A dessert',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='Which festival is known as the "Festival of Lights" in Nepal?',
                option_a='Dashain',
                option_b='Tihar',
                option_c='Holi',
                option_d='Maghe Sankranti',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=nepali_basic_quiz,
                question_text='What is the currency of Nepal?',
                option_a='Rupee',
                option_b='Dollar',
                option_c='Yen',
                option_d='Euro',
                correct_answer='A',
                points=1
            )
        ]

        # Create questions for Dramas & Theater Basics quiz
        dramas_basic_questions = [
            Question(
                quiz=dramas_basic_quiz,
                question_text='Which famous playwright wrote "Romeo and Juliet"?',
                option_a='Charles Dickens',
                option_b='William Shakespeare',
                option_c='Jane Austen',
                option_d='Mark Twain',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='What is the main purpose of a play\'s script?',
                option_a='To describe the stage design',
                option_b='To provide lines for actors and stage directions',
                option_c='To outline the director\'s vision',
                option_d='To list the cast and crew',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='Which of these is a type of theatrical genre?',
                option_a='Novel',
                option_b='Poetry',
                option_c='Comedy',
                option_d='Biography',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='What is an "audience" in theater?',
                option_a='The people who perform the play',
                option_b='The people who watch the play',
                option_c='The people who write the play',
                option_d='The people who design the costumes',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='What is a "monologue"?',
                option_a='A conversation between two characters',
                option_b='A long speech by one character',
                option_c='A song in a musical',
                option_d='A scene with no dialogue',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='Which element of drama refers to the events of the story?',
                option_a='Character',
                option_b='Theme',
                option_c='Plot',
                option_d='Spectacle',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='What is a "stage" in a theater?',
                option_a='The seating area for the audience',
                option_b='The area where actors perform',
                option_c='The entrance to the theater',
                option_d='The box office',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='Which of these is a common prop in a play?',
                option_a='Lighting fixture',
                option_b='Microphone',
                option_c='Chair',
                option_d='Curtain',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='What is the role of a "director" in a play?',
                option_a='To write the script',
                option_b='To act in the play',
                option_c='To oversee the artistic and technical aspects of the production',
                option_d='To sell tickets',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=dramas_basic_quiz,
                question_text='Which type of drama typically ends happily?',
                option_a='Tragedy',
                option_b='Comedy',
                option_c='Melodrama',
                option_d='Farce',
                correct_answer='B',
                points=1
            )
        ]

        # Create questions for Entertainment Basics quiz
        entertainment_basic_questions = [
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Which animal is known as the "King of the Jungle"?',
                option_a='Tiger',
                option_b='Lion',
                option_c='Elephant',
                option_d='Bear',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='What is the highest-grossing film of all time?',
                option_a='Avatar',
                option_b='Avengers: Endgame',
                option_c='Titanic',
                option_d='Star Wars: The Force Awakens',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Who is famous for the song "Bohemian Rhapsody"?',
                option_a='The Beatles',
                option_b='Queen',
                option_c='Led Zeppelin',
                option_d='Pink Floyd',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Which TV show features a character named Homer Simpson?',
                option_a='Family Guy',
                option_b='South Park',
                option_c='The Simpsons',
                option_d='Futurama',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Who played the role of Harry Potter in the film series?',
                option_a='Rupert Grint',
                option_b='Daniel Radcliffe',
                option_c='Emma Watson',
                option_d='Tom Felton',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Which pop artist is known as the "King of Pop"?',
                option_a='Elvis Presley',
                option_b='Michael Jackson',
                option_c='Prince',
                option_d='Justin Bieber',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='What is the fictional city where Batman operates?',
                option_a='Metropolis',
                option_b='Gotham City',
                option_c='Star City',
                option_d='Central City',
                correct_answer='B',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Which movie franchise features a character named James Bond?',
                option_a='Mission: Impossible',
                option_b='Bourne',
                option_c='007',
                option_d='Kingsman',
                correct_answer='C',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Who is the lead singer of the band U2?',
                option_a='Bono',
                option_b='The Edge',
                option_c='Adam Clayton',
                option_d='Larry Mullen Jr.',
                correct_answer='A',
                points=1
            ),
            Question(
                quiz=entertainment_basic_quiz,
                question_text='Which TV show is set in the fictional world of Westeros?',
                option_a='The Witcher',
                option_b='Game of Thrones',
                option_c='House of the Dragon',
                option_d='Vikings',
                correct_answer='B',
                points=1
            )
        ]

        # Create questions for Advanced Sports quiz
        sports_questions = [
            Question(
                quiz=sports_advanced_quiz,
                question_text='In which year were the first modern Olympic Games held?',
                option_a='1892',
                option_b='1896',
                option_c='1900',
                option_d='1904',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which country has won the most FIFA World Cups?',
                option_a='Germany',
                option_b='Italy',
                option_c='Brazil',
                option_d='Argentina',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Who holds the record for the most Grand Slam singles titles in men\'s tennis?',
                option_a='Roger Federer',
                option_b='Rafael Nadal',
                option_c='Novak Djokovic',
                option_d='Pete Sampras',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is a "hat-trick" in ice hockey?',
                option_a='Scoring two goals in a game.',
                option_b='Scoring three goals in a single game by one player.',
                option_c='Getting three assists in a game.',
                option_d='Winning three consecutive games.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which sport uses terms like "birdie," "eagle," and "bogey"?',
                option_a='Tennis',
                option_b='Golf',
                option_c='Baseball',
                option_d='Bowling',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which athlete is known as "The Flying Finn" in long-distance running?',
                option_a='Paavo Nurmi',
                option_b='Lasse Virén',
                option_c='Hannes Kolehmainen',
                option_d='Ville Ritola',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is the highest individual score in a single test innings in cricket?',
                option_a='365 not out by Sir Garfield Sobers',
                option_b='375 by Brian Lara',
                option_c='400 not out by Brian Lara',
                option_d='380 by Matthew Hayden',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which country has won the most gold medals in Winter Olympics history?',
                option_a='United States',
                option_b='Norway',
                option_c='Germany',
                option_d='Russia',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Who is the only person to have played in both the FIFA World Cup and the Cricket World Cup?',
                option_a='Viv Richards',
                option_b='Ian Botham',
                option_c='Gary Lineker',
                option_d='Denis Compton',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is the oldest major tennis tournament in the world?',
                option_a='French Open',
                option_b='US Open',
                option_c='Wimbledon',
                option_d='Australian Open',
                correct_answer='C',
                points=2
            )
        ]

        # Create questions for Nepali Language & Culture quiz (Advanced)
        nepali_questions = [
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Who is known as the "Mahakavi" (Great Poet) of Nepali literature?',
                option_a='Laxmi Prasad Devkota',
                option_b='Bhanubhakta Acharya',
                option_c='Gopal Prasad Rimal',
                option_d='Muna Madan',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Which is the national flower of Nepal?',
                option_a='Laligurans (Rhododendron)',
                option_b='Jasmine',
                option_c='Lotus',
                option_d='Rose',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='What is the significance of "Dashain" in Nepali culture?',
                option_a='It marks the end of winter.',
                option_b='It\'s the longest and most auspicious festival, celebrating the victory of good over evil.',
                option_c='It\'s a celebration of harvest.',
                option_d='It commemorates the birth of Buddha.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Which script is primarily used to write the Nepali language?',
                option_a='Roman script',
                option_b='Devanagari script',
                option_c='Nepali script',
                option_d='Brahmi script',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Who was the first king of unified Nepal?',
                option_a='Prithvi Narayan Shah',
                option_b='Janga Bahadur Rana',
                option_c='Mahendra Bir Bikram Shah Dev',
                option_d='Tribhuvan Bir Bikram Shah Dev',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Which ancient kingdom, located in present-day Nepal, was known for its trade routes between India and Tibet?',
                option_a='Lumbini',
                option_b='Mithila',
                option_c='Licchavi',
                option_d='Gorkha',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Explain the significance of "Indra Jatra" festival.',
                option_a='It celebrates the start of spring.',
                option_b='It\'s a celebration honoring the god Indra and Kumari, the Living Goddess, seeking blessings for a good harvest.',
                option_c='It marks the end of the monsoon season.',
                option_d='It commemorates a historical battle.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Who wrote the epic "Muna Madan"?',
                option_a='Bhanubhakta Acharya',
                option_b='Laxmi Prasad Devkota',
                option_c='Balkrishna Sama',
                option_d='Gopal Prasad Rimal',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='What is the traditional Nepali instrument similar to a flute?',
                option_a='Sarangi',
                option_b='Madal',
                option_c='Bansuri',
                option_d='Damaru',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Describe the traditional Newari architecture found in Kathmandu Valley.',
                option_a='Characterized by simple, functional designs.',
                option_b='Known for intricate wood carvings, multi-tiered roofs, and pagoda style.',
                option_c='Primarily uses concrete and steel.',
                option_d='Focuses on minimalist aesthetics.',
                correct_answer='B',
                points=2
            )
        ]

        # Create questions for Dramas & Theater quiz (Advanced)
        dramas_questions = [
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Who wrote the ancient Greek tragedy "Oedipus Rex"?',
                option_a='Aeschylus',
                option_b='Euripides',
                option_c='Sophocles',
                option_d='Aristophanes',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the primary characteristic of Absurdist theatre?',
                option_a='Focus on realistic portrayal of life.',
                option_b='Emphasis on logical plots and clear resolutions.',
                option_c='Exploration of the meaninglessness of human existence, often with illogical dialogue and repetitive actions.',
                option_d='Strict adherence to classical dramatic unities.',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Who is considered the "father of modern drama"?',
                option_a='William Shakespeare',
                option_b='Henrik Ibsen',
                option_c='Anton Chekhov',
                option_d='Bertolt Brecht',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is a soliloquy in drama?',
                option_a='A dialogue between two characters.',
                option_b='A speech delivered by a character alone on stage, revealing their thoughts and feelings.',
                option_c='A song performed by the chorus.',
                option_d='A conversation between the actor and the audience.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Which play by Arthur Miller critiques the American Dream?',
                option_a='The Crucible',
                option_b='All My Sons',
                option_c='Death of a Salesman',
                option_d='A View from the Bridge',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Explain Brecht\'s concept of "Verfremdungseffekt" (alienation effect).',
                option_a='A technique to make the audience empathize more with characters.',
                option_b='A technique to distance the audience from the play to encourage critical reflection rather than emotional immersion.',
                option_c='A method for actors to get into character quickly.',
                option_d='A special lighting effect used in avant-garde theater.',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the significance of the Globe Theatre in Shakespearean drama?',
                option_a='It was the first indoor theatre in England.',
                option_b='It was where Shakespeare performed all his plays personally.',
                option_c='It was a major open-air playhouse in London, famous for hosting many of Shakespeare\'s plays.',
                option_d='It was a private theater for royalty only.',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Who wrote "Waiting for Godot"?',
                option_a='Eugene Ionesco',
                option_b='Samuel Beckett',
                option_c='Harold Pinter',
                option_d='Tom Stoppard',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the function of a dramaturg in a theater production?',
                option_a='To design the costumes.',
                option_b='To research and provide context for the play, assisting the director and actors.',
                option_c='To compose the music.',
                option_d='To manage the theater\'s finances.',
                correct_answer='B',
                points=2
            )
        ]

        # Create questions for Entertainment Industry quiz (Advanced)
        entertainment_questions = [
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which film holds the record for the most Academy Awards won?',
                option_a='Titanic',
                option_b='Ben-Hur',
                option_c='The Lord of the Rings: The Return of the King',
                option_d='All of the above (tied with 11 awards)',
                correct_answer='D',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Who composed the soundtrack for the film "Inception"?',
                option_a='Hans Zimmer',
                option_b='John Williams',
                option_c='Ennio Morricone',
                option_d='Ramin Djawadi',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which TV series is known for popularizing the phrase "Winter is Coming"?',
                option_a='The Witcher',
                option_b='Game of Thrones',
                option_c='House of the Dragon',
                option_d='Vikings',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Who is the highest-grossing film director of all time?',
                option_a='Steven Spielberg',
                option_b='James Cameron',
                option_c='Michael Bay',
                option_d='Christopher Nolan',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which music artist has won the most Grammy Awards?',
                option_a='Beyoncé',
                option_b='Georg Solti',
                option_c='Quincy Jones',
                option_d='Alison Krauss',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='What is the highest-grossing media franchise of all time?',
                option_a='Marvel Cinematic Universe',
                option_b='Star Wars',
                option_c='Pokémon',
                option_d='Hello Kitty',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Explain the concept of "method acting."',
                option_a='A style of acting where actors use their own experiences and emotions to create believable characters.',
                option_b='A highly stylized and artificial form of acting.',
                option_c='A technique focused on physical movements and gestures.',
                option_d='Acting without any prior rehearsal.',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which influential music festival took place in 1969?',
                option_a='Glastonbury',
                option_b='Coachella',
                option_c='Woodstock',
                option_d='Monterey Pop Festival',
                correct_answer='C',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Who wrote the novel that inspired the film "Blade Runner"?',
                option_a='Isaac Asimov',
                option_b='Philip K. Dick',
                option_c='Arthur C. Clarke',
                option_d='Frank Herbert',
                correct_answer='B',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which streaming service famously pioneered the release of entire seasons of TV shows at once?',
                option_a='Hulu',
                option_b='Amazon Prime Video',
                option_c='Netflix',
                option_d='HBO Max',
                correct_answer='C',
                points=2
            )
        ]

        # Create questions for Advanced Sports quiz
        advanced_sports_questions = [
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is the significance of the "Moneyball" approach in baseball?',
                option_a='It revolutionized player evaluation using statistical analysis',
                option_b='It increased player salaries',
                option_c='It changed the rules of the game',
                option_d='It introduced new equipment',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which of these is NOT a valid strategy in modern football tactics?',
                option_a='Playing without a goalkeeper',
                option_b='Tiki-taka',
                option_c='Gegenpressing',
                option_d='Park the bus',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is the significance of the "Fosbury Flop" in high jump?',
                option_a='It revolutionized the technique by jumping backwards',
                option_b='It increased the height of the bar',
                option_c='It changed the landing mat material',
                option_d='It introduced new rules',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='Which of these is NOT a recognized Olympic sport?',
                option_a='Chess',
                option_b='Modern Pentathlon',
                option_c='Rhythmic Gymnastics',
                option_d='Water Polo',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=sports_advanced_quiz,
                question_text='What is the significance of the "Total Football" strategy?',
                option_a='It allows players to switch positions fluidly during play',
                option_b='It focuses on defensive play',
                option_c='It emphasizes individual skills',
                option_d='It prioritizes long passes',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_sports_questions)

        # Create questions for Advanced Nepali Language quiz
        advanced_nepali_questions = [
            Question(
                quiz=nepali_advanced_quiz,
                question_text='What is the significance of "Muna Madan" in Nepali literature?',
                option_a='It is a classic poem about love and sacrifice',
                option_b='It is the first Nepali novel',
                option_c='It is a religious text',
                option_d='It is a historical document',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Which of these is NOT a characteristic of classical Nepali poetry?',
                option_a='Free verse without meter',
                option_b='Use of chhand',
                option_c='Alankar',
                option_d='Rasa',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='What is the significance of the "Aksharanka" in Nepali grammar?',
                option_a='It is a system of vowel markers',
                option_b='It is a type of verb',
                option_c='It is a punctuation mark',
                option_d='It is a number system',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='Which of these is NOT a recognized form of Nepali folk literature?',
                option_a='Modern rap',
                option_b='Dohori',
                option_c='Lok geet',
                option_d='Deusi',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=nepali_advanced_quiz,
                question_text='What is the significance of "Bhanubhakta Acharya" in Nepali literature?',
                option_a='He is considered the first poet to write in Nepali language',
                option_b='He wrote the first Nepali dictionary',
                option_c='He created the Nepali alphabet',
                option_d='He translated the Bible to Nepali',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_nepali_questions)

        # Create questions for Advanced Dramas & Theater quiz
        advanced_dramas_questions = [
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the significance of the "Fourth Wall" in theater?',
                option_a='It is the imaginary barrier between actors and audience',
                option_b='It is a physical wall on stage',
                option_c='It is a lighting technique',
                option_d='It is a sound effect',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Which of these is NOT a recognized theater movement?',
                option_a='Digital theater',
                option_b='Theater of the Absurd',
                option_c='Epic Theater',
                option_d='Naturalism',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the significance of "Stanislavski\'s System" in acting?',
                option_a='It emphasizes psychological realism in acting',
                option_b='It focuses on physical movement',
                option_c='It is a vocal training method',
                option_d='It is a stage design technique',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='Which of these is NOT a traditional form of Asian theater?',
                option_a='Broadway musical',
                option_b='Kabuki',
                option_c='Noh',
                option_d='Kathakali',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=dramas_advanced_quiz,
                question_text='What is the significance of "Brechtian theater"?',
                option_a='It uses alienation effects to make audiences think critically',
                option_b='It focuses on emotional realism',
                option_c='It emphasizes naturalistic acting',
                option_d='It uses only classical music',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_dramas_questions)

        # Create questions for Advanced Entertainment quiz
        advanced_entertainment_questions = [
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='What is the significance of the "French New Wave" in cinema?',
                option_a='It revolutionized filmmaking with new techniques and storytelling',
                option_b='It introduced color to films',
                option_c='It created the first sound films',
                option_d='It established the first film studios',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which of these is NOT a recognized film movement?',
                option_a='Digital Wave',
                option_b='German Expressionism',
                option_c='Italian Neorealism',
                option_d='Soviet Montage',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='What is the significance of "The Beatles\' Sgt. Pepper\'s Lonely Hearts Club Band"?',
                option_a='It revolutionized album production and concept albums',
                option_b='It was the first rock album',
                option_c='It introduced electric guitars',
                option_d='It created the first music video',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='Which of these is NOT a recognized art movement?',
                option_a='Digital Realism',
                option_b='Impressionism',
                option_c='Cubism',
                option_d='Surrealism',
                correct_answer='A',
                points=2
            ),
            Question(
                quiz=entertainment_advanced_quiz,
                question_text='What is the significance of "The Birth of a Nation" in film history?',
                option_a='It pioneered many film techniques but is controversial for its content',
                option_b='It was the first color film',
                option_c='It introduced sound to cinema',
                option_d='It created the first movie theater',
                correct_answer='A',
                points=2
            )
        ]
        db.session.add_all(advanced_entertainment_questions)

        db.session.add_all(python_questions)
        db.session.add_all(advanced_python_questions)
        db.session.add_all(web_questions)
        db.session.add_all(advanced_web_questions)
        db.session.add_all(math_questions)
        db.session.add_all(advanced_math_questions)
        db.session.add_all(gk_questions)
        db.session.add_all(advanced_gk_questions)
        db.session.add_all(social_questions)
        db.session.add_all(advanced_social_questions)
        db.session.add_all(psychology_questions)
        db.session.add_all(advanced_psychology_questions)
        db.session.add_all(science_questions)
        db.session.add_all(advanced_science_questions)
        db.session.add_all(sports_basic_questions)
        db.session.add_all(nepali_basic_questions)
        db.session.add_all(dramas_basic_questions)
        db.session.add_all(entertainment_basic_questions)
        db.session.add_all(sports_questions)
        db.session.add_all(nepali_questions)
        db.session.add_all(dramas_questions)
        db.session.add_all(entertainment_questions)
        db.session.add_all(advanced_sports_questions)
        db.session.add_all(advanced_nepali_questions)
        db.session.add_all(advanced_dramas_questions)
        db.session.add_all(advanced_entertainment_questions)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database() 