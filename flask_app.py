from flask import Flask, render_template, request, redirect, flash, url_for, send_file, session
from flask_login import  login_required, logout_user
from googleapiclient.discovery import build
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

API_KEY = '###################################'
SPREADSHEET_ID = '13eRjZCFyYWVbKQdgj5Yj3uMatjf23at0Fdkd5B-VHXQ'
RANGE_NAME = 'WeeklyTop!A2:B'

def get_top_three():
    service = build('sheets', 'v4', developerKey=API_KEY)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        return []

    sorted_values = sorted([x for x in values if len(x) > 1], key=lambda x: math.ceil(float(x[1])), reverse=True)
    top_three = sorted_values[:3]
    return top_three
def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

app.jinja_env.filters['ordinal'] = ordinal

@app.route("/")
def test():
    return render_template('HomeDashboard.html')

@app.route("/home")
@login_required
def home():
    return render_template('HomeDashboard.html')

@app.route("/base")
def base():
    return render_template('base.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/our_team')
def our_team():
    return render_template('team_members.html')

@app.route('/data.json')
def serve_data_file():
    return send_file('temp.json', mimetype='application/json')

@app.route('/leaderboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        password = request.form['password']
        if password == '12346738':
            session['authenticated'] = True
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect password. Please try again.', 'danger')
            return redirect(url_for('dashboard'))

    if session.get('authenticated'):
        top_three = get_top_three()
        return render_template('dashboard.html', top_three=top_three)
    return render_template('password_protect.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('authenticated', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
