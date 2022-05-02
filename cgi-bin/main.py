# -*- coding: utf-8 -*-
import cgi
import sys
import io

print('Content-Type: text/html; charset=UTF-8\n')
html_body = """
<!DOCTYPE html>
<html>
<head>
<title>Document</title>
<style>
.parent{

}
.contact{
   display: flex;
   flex-direction: column;
}
</style>
</head>
<body>
<div class="parent">
<div class="contact">
<h1>名前：%s</h1>
<h1>カナ：%s</h1>
<h1>メールアドレス：%s</h1>
<h1>きっかけ：%s</h1>
<h1>ご要望：%s</h1>
<h1>詳細：%s</h1>
</div>
</div>
</body>
</html>
"""
form = cgi.FieldStorage()
name = form.getvalue('name', '')
kana = form.getvalue('kananame', '')
mail = form.getvalue('email', '')
kikkake = form.getfirst('kikkake', '')
value = form.getvalue('chkbox', '')
text = form.getvalue('other', '')

if __name__ == '__main__':
    print(html_body % (name, kana, mail, kikkake, value, text))