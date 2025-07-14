# app1/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_app1():
    return "Hello from App 1!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)