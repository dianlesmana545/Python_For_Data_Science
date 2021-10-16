from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
app = flask.Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return(flask.render_template('main.html'))


if __name__ == '__main__':
    app.run()


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
