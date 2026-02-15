#Flask app will go here

from flask import Flask, request, jsonify, render_template # Add render_template
from flask_cors import CORS
import sqlite3

# Tell Flask the templates and static files are in the frontend folder
app = Flask(__name__, 
            template_folder="../frontend/templates", 
            static_folder="../frontend/static")
CORS(app)

def get_db_connection():
    # Make sure this path points to where init_db.py creates the file
    conn = sqlite3.connect('../database/reminders.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- ROUTES FOR PAGES ---

@app.route('/')
def index():
    return render_template('index.html') # This serves the dashboard

@app.route('/login')
def login_page():
    return render_template('login.html') # This serves the login page

# --- API ROUTES ---

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.json
    # Here you will eventually check the database for the user
    return jsonify({"message": "Login successful"}), 200


@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.json
    full_name = data.get('fullName')
    email = data.get('email')
    password = data.get('password') # In Week 2, we will add hashing!

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (full_name, email, password_hash) VALUES (?, ?, ?)',
                     (full_name, email, password))
        conn.commit()
        return jsonify({"message": "User created"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already registered"}), 400
    finally:
        conn.close()

# Keep your existing /register route here...

if __name__ == '__main__':
    app.run(debug=True, port=5000)