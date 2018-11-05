from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/hello')
def hello_world2():
    return render_template('hello2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')