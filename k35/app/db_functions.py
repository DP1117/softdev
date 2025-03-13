import sqlite3
from flask_login import UserMixin

def get_db_connection():
    conn = sqlite3.connect('site.db')
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

def add_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['email'], user['password'])
    return None

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['email'], user['password'])
    return None

def add_story(title, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO story (title, user_id) VALUES (?, ?)', (title, user_id))
    story_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return story_id

def add_contribution(content, user_id, story_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contribution (content, user_id, story_id) VALUES (?, ?, ?)', (content, user_id, story_id))
    conn.commit()
    conn.close()

def get_latest_contribution(story_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contribution WHERE story_id = ? ORDER BY id DESC LIMIT 1', (story_id,))
    contribution = cursor.fetchone()
    conn.close()
    return contribution

def get_user_stories(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM story WHERE user_id = ?', (user_id,))
    stories = cursor.fetchall()
    conn.close()
    return stories

def get_story_by_id(story_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM story WHERE id = ?', (story_id,))
    story = cursor.fetchone()
    conn.close()
    return story
