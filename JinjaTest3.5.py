from jinja2 import Template


persons = [{'name': "Ivan", 'age': 23, 'weight': 78},
           {'name': "Sergey", 'age': 14, 'weight': 56},
           {'name': "Oleg", 'age': 23, 'weight': 87},
           {'name': "Misha", 'age': 34, 'weight': 79}
           ]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{ u.name }} {{ caller(u) }}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{ user.age }}
    <li>weight: {{ user.weight }}
    </ul>
{% endcall -%}

'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)