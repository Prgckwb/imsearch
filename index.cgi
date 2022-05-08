#! /usr/local/anaconda3/bin/python3

from jinja2 import Environment, FileSystemLoader
import cgi
import cgitb

cgitb.enable(display=0, logdir="./log")


def make_page(html):
    print('Content-Type: text/html\n')
    print(html)


a = "hogehoge"

html_text = f'''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="static/css/styles.css">
    <link rel="script" href="static/javascript/main.js">
    <title>柳井研究室CGI課題</title>
</head>
<body>
<section class="section">
    <div class="container">
        <p class="title is-2 has-text-centered">
            Image Search by RGB Histgram with Histgram Intersection {a}
        </p>
        
        <div class="columns">
            <div class="column">
                
            </div>        
        </div>
    </div>
</section>
</body>
</html>
'''

make_page(html_text)
