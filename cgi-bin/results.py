#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import cgi, cgitb

form = cgi.FieldStorage()
userName = "blank"
userName = form["userName"].value

print "Content-type:text/html\r\n\r\n"
print userName

