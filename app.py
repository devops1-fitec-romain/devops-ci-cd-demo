
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<name>')
def hello_root(name):
    r = 'Hello, ' + str(name)
    return r


if __name__ == '__main__':
    app.run()