
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    technical_skills = db.Column(db.String(255))
    project_interests = db.Column(db.String(255))

# Create the database tables
db.create_all()

# Define the home route
@app.route('/')
def home():
    # Get all the users from the database
    users = User.query.all()

    # Render the home page
    return render_template('home.html', users=users)

# Define the register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the request is a POST request, check if the user already exists
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        technical_skills = request.form['technical_skills']
        project_interests = request.form['project_interests']

        user = User.query.filter_by(username=username).first()

        # If the user does not exist, create a new user
        if not user:
            new_user = User(username=username, password=password, technical_skills=technical_skills, project_interests=project_interests)
            db.session.add(new_user)
            db.session.commit()

            # Flash a success message
            flash('You have successfully registered!')

            # Redirect to the home page
            return redirect(url_for('home'))

        # If the user already exists, flash an error message
        else:
            flash('This username is already taken!')

            # Redirect to the register page
            return redirect(url_for('register'))

    # If the request is a GET request, render the register page
    else:
        return render_template('register.html')

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request is a POST request, check if the user's credentials are valid
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        # If the user exists and the password is correct, log the user in
        if user and user.password == password:
            # Flash a success message
            flash('You have successfully logged in!')

            # Redirect to the home page
            return redirect(url_for('home'))

        # If the user does not exist or the password is incorrect, flash an error message
        else:
            flash('Invalid credentials!')

            # Redirect to the login page
            return redirect(url_for('login'))

    # If the request is a GET request, render the login page
    else:
        return render_template('login.html')

# Define the profile route
@app.route('/profile/<username>')
def profile(username):
    # Get the user from the database
    user = User.query.filter_by(username=username).first()

    # Render the profile page
    return render_template('profile.html', user=user)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
