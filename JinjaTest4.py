from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [{'name': "Ivan", 'age': 23, 'weight': 78},
           {'name': "Sergey", 'age': 14, 'weight': 56},
           {'name': "Oleg", 'age': 23, 'weight': 87},
           {'name': "Misha", 'age': 34, 'weight': 79}
           ]


def loadTpl(path):
    if path == "qwerty":
        return ''' Name {{user.name}}, age {{user.age}}'''
    else:
        return ''' Data: {{user}}'''


# fileloader = FileSystemLoader('templates')
fileloader = FunctionLoader(loadTpl)
env = Environment(loader=fileloader)

tm = env.get_template('qwerty')
msg = tm.render(user=persons[0])

print(msg)
