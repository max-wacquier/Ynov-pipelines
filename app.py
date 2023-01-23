from bottle import route, run, template
from tools import addCalc


@route('/')
def home():
    return '<b>Homepage</b>!'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/add/<a>/<b>')
def add(a, b):
    result = addCalc(a, b)
    return {
        "result": result
    }


run(host='localhost', port=8080, reloader=True)
