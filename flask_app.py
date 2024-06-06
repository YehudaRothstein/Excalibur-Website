import os
import json
import random
import bcrypt
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

USER_DATA_FILE = '/home/yehudarothstein/mysite/users.json'
MATCH_DATA_FILE = '/home/yehudarothstein/mysite/matches.json'
app.config['UPLOAD_FOLDER'] = '/home/yehudarothstein/mysite/static/profiles'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_users(users):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def generate_unique_id(existing_ids):
    while True:
        new_id = random.randint(100000, 999999)
        if new_id not in existing_ids:
            return new_id

class User(UserMixin):
    def __init__(self, id, username, password, full_name, job_title, profile_picture=None, is_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.job_title = job_title
        self.profile_picture = profile_picture
        self.is_admin = is_admin

@login_manager.user_loader
def load_user(user_id):
    users = load_users()
    for user in users:
        if user['id'] == int(user_id):
            return User(user['id'], user['username'], user['password'], user['full_name'], user['job_title'], user.get('profile_picture'), user.get('is_admin', False))
    return None

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        full_name = request.form['full_name']
        job_title = request.form['job_title']
        users = load_users()

        if any(user['username'] == username for user in users):
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

        if len(password) < 6:
            flash('Password is too weak. Please choose a stronger password.', 'danger')
            return redirect(url_for('register'))

        hashed_password = hash_password(password)
        new_user = {
            'id': generate_unique_id([user['id'] for user in users]),
            'username': username,
            'password': hashed_password,
            'full_name': full_name,
            'job_title': job_title,
            'is_admin': False
        }
        users.append(new_user)
        save_users(users)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route("/upload_profile_picture", methods=['POST'])
@login_required
def upload_profile_picture():
    if 'profile_picture' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('profile'))

    file = request.files['profile_picture']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('profile'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        users = load_users()
        for user in users:
            if user['id'] == current_user.id:
                user['profile_picture'] = filename
                save_users(users)
                current_user.profile_picture = filename
                break
        flash('Profile picture uploaded successfully!', 'success')
        return redirect(url_for('profile'))
    else:
        flash('Allowed file types are png, jpg, jpeg, gif', 'danger')
        return redirect(url_for('profile'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        users = load_users()
        user = next((user for user in users if user['username'] == username), None)

        if user and check_password(user['password'], password):
            user_obj = User(user['id'], user['username'], user['password'], user['full_name'], user['job_title'], user.get('is_admin', False))
            login_user(user_obj)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/Scout", methods=["POST", "GET"])
@login_required
def scout():
    try:
        if request.method == 'POST':
            data = request.get_json()
            json_file_path = "/home/yehudarothstein/mysite/static/Data.JSON"
            comments_file_path = "/home/yehudarothstein/mysite/static/Comments.JSON"
            existing_data = []

            if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
                with open(json_file_path, "r") as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        print("JSONDecodeError: The file is empty or not properly formatted")
            existing_data.append(data)
            try:
                with open(json_file_path, "w") as file:
                    json.dump(existing_data, file, indent=4)
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")

            return "Thanks For Submmiting - Exclaibur Scouting System Dev Team"
            return redirect("https://www.excaliburfrc.com/Scout")
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template("Scout.html")

@app.route("/ReportBugs", methods=["POST", "GET"])
@login_required
def report_bug():
    return render_template("Report.html")

@app.route("/")
@login_required
def test():
    return render_template('HomeDashboard.html', full_name=current_user.full_name, job_title=current_user.job_title)

@app.route("/profile")
@login_required
def profile():
    return render_template('Profile.html', full_name=current_user.full_name, job_title=current_user.job_title)

@app.route("/home")
@login_required
def home():
    return render_template('HomeDashboard.html', full_name=current_user.full_name, job_title=current_user.job_title)
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    if not os.path.exists(USER_DATA_FILE):
        save_users([])
    app.run(debug=True)
