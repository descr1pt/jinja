from jinja2 import Template
from markupsafe import escape


data = ''' {% raw %} Информация здесь не преобразовывается {{name}} {% endraw %}'''

tm = Template(data)
msg = tm.render(name='Федор')

print(msg)

link = ''' Ссылка должна быть в виде ссылки:
 <a href="#">Ссылка</a>'''
msg2 = escape(link)
# tm2 = Template('{{ link | e}}')
# msg2 = tm2.render(link=link)

print(msg2)

cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 2, 'city': 'Tver'},
          {'id': 3, 'city': 'Peter'},
          {'id': 4, 'city': 'Novgorod'}]
link2 = '''<select name="cities">
  {% for c in cities -%}
  {% if c.id > 2 -%}
        <option value="{{c['id']}}">"{{c['city']}}"</option>
  {% else -%}
        {{c['city']}}
  {% endif -%}
  {% endfor -%}
  </select>'''

tm2 = Template(link2)
msg3 = tm2.render(cities=cities)

print(msg3)


