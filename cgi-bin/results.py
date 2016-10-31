#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Import modules for CGI handling 
import sys, json, cgi

#form = cgi.FieldStorage()
#userName = "blank"
#userName = form["userName"].value

result = {'success':'true','message':'The Command Completed Successfully'};
inputedTest = {'Name':'test'}

myjson = json.load(sys.stdin)
# Do something with 'myjson' object

#print 'Content-Type: application/json\n\n'

with open('names.txt', 'w') as outfile:
    json.dump(myjson, outfile)

print "Content-type:application/json\r\n\r\n"
print json.dumps(result)
#print "test"
