#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import sys, json, cgi

form = cgi.FieldStorage()
userName = "blank"
userName = form["userName"].value

result = {'success':'true','message':'The Command Completed Successfully'};
inputedTest = {'Name':'test'}

myjson = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
# Do something with 'myjson' object

#print 'Content-Type: application/json\n\n'


print "Content-type:text/html\r\n\r\n"
print json.dumps(result)
#print "test"
