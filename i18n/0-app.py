#!/usr/bin/env python3
"""creating a simple flask app task 0"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """rendering the index.html template"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
