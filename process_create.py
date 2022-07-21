#!/usr/local/bin/python3


import cgi
form = cgi.FieldStorage()
title = form["id"].value
description = form['description'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection
print("Location: index.py?id="+title)
print()
