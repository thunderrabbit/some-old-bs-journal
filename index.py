#!/usr/bin/env python
import sys
import cgi
import os.path  # os.path - The key to File I/O
import pickle

# the classes below are written for python_file_journal
sys.path.append("classes")
import template
import db

field = cgi.FieldStorage()
print "Content-Type: text/plain\n\n"
print 'Planning to create a python version of my journal, world!\n'
