from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello flask app'

@app.route('/hello')
def hello():
    return 'This is the hello world page.'