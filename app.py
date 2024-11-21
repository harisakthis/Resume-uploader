
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Simple database (in-memory for now)
access_requests = []
approved_access = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_access', methods=['POST'])
def request_access():
    email = request.form['email']
    access_requests.append(email)
    return redirect(url_for('index'))

@app.route('/admin')
def admin_dashboard():
    return render_template('admin.html', requests=access_requests)

@app.route('/approve/<email>', methods=['POST'])
def approve_access(email):
    if email in access_requests:
        access_requests.remove(email)
        approved_access.append(email)
    return redirect(url_for('admin_dashboard'))

@app.route('/resume/<email>')
def resume(email):
    if email in approved_access:
        return render_template('resume.html', email=email)
    else:
        return "Access Denied", 403

if __name__ == '__main__':
    app.run(debug=True)
