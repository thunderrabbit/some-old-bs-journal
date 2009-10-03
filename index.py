#!/usr/bin/env python
import cgi

field = cgi.FieldStorage()
print "Content-Type: text/plain\n\n"
print 'Planning to create a python version of my journal, world!\n'

with open('/home/thunderrabbit/robnugen.com/j/TODO', 'r') as todo_file:
    read_data = todo_file.read()
todo_file.closed
    
print read_data
