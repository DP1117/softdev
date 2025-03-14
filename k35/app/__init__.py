# Heading: Collaborative Storytelling Game/Website

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS stories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        creator_id INTEGER,
                        FOREIGN KEY(creator_id) REFERENCES users(id)
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS story_updates (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        story_id INTEGER,
                        user_id INTEGER,
                        content TEXT,
                        FOREIGN KEY(story_id) REFERENCES stories(id),
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
            user = c.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))
    
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT s.id, s.title FROM stories s JOIN story_updates su ON s.id = su.story_id WHERE su.user_id = ?', (user_id,))
        stories = c.fetchall()
    return render_template('dashboard.html', stories=stories)

@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO stories (title, creator_id) VALUES (?, ?)', (title, user_id))
            story_id = c.lastrowid
            c.execute('INSERT INTO story_updates (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
            conn.commit()
        return redirect(url_for('dashboard'))
    return render_template('new_story.html')

@app.route('/add_to_story/<int:story_id>', methods=['GET', 'POST'])
def add_to_story(story_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT content FROM story_updates WHERE story_id = ? ORDER BY id DESC LIMIT 1', (story_id,))
        latest_update = c.fetchone()
        if request.method == 'POST':
            content = request.form['content']
            c.execute('INSERT INTO story_updates (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
            conn.commit()
            return redirect(url_for('dashboard'))
    return render_template('add_to_story.html', latest_update=latest_update)

if __name__ == '__main__':
    app.run(debug=True)
