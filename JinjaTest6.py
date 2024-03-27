from jinja2 import Environment, FileSystemLoader, FunctionLoader

subs = ['Math', 'English', 'PE', 'Chemistry']

fileloader = FileSystemLoader('templates')
env = Environment(loader=fileloader)

tm = env.get_template('about.html')
msg = tm.render(list_table = subs)

print(msg)
