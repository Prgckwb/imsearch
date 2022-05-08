#! /usr/local/anaconda3/bin/python3

from jinja2 import Environment, FileSystemLoader
import cgi
import cgitb

from template.main_page import get_page

cgitb.enable(display=0, logdir="./log")

form = cgi.FieldStorage()

image = ""
feature = "Unko"

if "image" in form:
    image = form["image"].value
if "feature" in form:
    feature = form["feature"].value

print('Content-Type: text/html\n')
print(get_page(image, feature))
