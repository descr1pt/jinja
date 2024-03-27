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


fileloader = FileSystemLoader('templates')
env = Environment(loader=fileloader)

tm = env.get_template('page.html')
msg = tm.render(domain='http://proproprogs.ru', title='About Jinja')

print(msg)
