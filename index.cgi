#! /usr/local/anaconda3/bin/python3

from jinja2 import Environment, FileSystemLoader
import cgi
import cgitb

from template.main_page import get_html_text

cgitb.enable(display=0, logdir="./log")


def make_page(html):
    print('Content-Type: text/html\n')
    print(html)


make_page(get_html_text("Unko"))
