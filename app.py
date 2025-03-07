# app.py
from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<int:length>')
def generate(length):
    if length < 4 or length > 20:  # Set limits for password length
        return jsonify({'error': 'Password length must be between 4 and 20 characters.'}), 400
    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)