from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {'john': 'secret', 'jane': 'password'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        return redirect(url_for('hello', username=username))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/hello/<username>')
def hello(username):
    return f'Hello, {username}!'

# Nouvelle route pour afficher la sélection de l'équipe
@app.route('/team/<teamname>')
def team(teamname):
    return f'Vous avez sélectionné l\'équipe {teamname}!'

if __name__ == '__main__':
    app.run(debug=True)
