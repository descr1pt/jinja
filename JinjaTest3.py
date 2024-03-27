from jinja2 import Template


cars = [{'model': "Audi", 'price': 23000},
        {'model': "BMW", 'price': 30000},
        {'model': "Scoda", 'price': 12222},
        {'model': "ZHIGUL", 'price': 333333}]

tpl = 'Суммарная цена автомобилей {{ cs | sum(attribute= "price" ) }}'
tm = Template(tpl)
msg = tm.render(cs=cars)

tpl2 = '''
{%- for u in users -%}
{% filter lower %}{{ u.model }}{% endfilter %}
{% endfor -%}
'''
tm2 = Template(tpl2)
msg2 = tm2.render(users=cars)


print(msg, msg2)

