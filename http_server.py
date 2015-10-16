from bottle import route, run, template

class Employee(object):
    def __init__(self, age, company):
        self._age = age
        self._company = company

@route('/hello/<name>', method='GET')
def response(name):
    return template("<b>Hello {{name}}</b>!",name = name)

run(host='localhost', port=4040)