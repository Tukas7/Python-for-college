from jinja2 import Template

persons = [
    { 'name':'Maxim', 'age':25, 'weight': 75},
    { 'name':'Sofia', 'age':22, 'weight': 55},
    { 'name':'Lera', 'age':21, 'weight': 65}
]
html= '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{ u.name }} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li> age:{{user.age}}
    <li> weight:{{user.weight}}
    </ul>
{% endcall -%}
'''


tm = Template(html)
msg = tm.render(users=persons)


print(msg)
