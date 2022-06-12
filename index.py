#!python
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print(pageId)
print('''
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>2트랙 - HTML + Python</title>
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
    <li> <a href="index.py?id=HTML">html</a></li>
    <li> <a href="index.py?id=CSS">css</a></li>
    <li> <a href="index.py?id=JavaScript">javascript</a></li>
  </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
</html>
'''.format(title=pageId, desc=description))
