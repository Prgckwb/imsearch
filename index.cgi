#! /usr/local/anaconda3/bin/python3

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./', encoding='utf-8'))
tpl = env.get_template('template/index.html')

html = tpl.render()

print('Content-Type: text/html\n')
print(html)
