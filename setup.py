#!/usr/bin/env python
import sys
import cgi
import os.path  # os.path - The key to File I/O
import pickle

// the classes below are written for python_file_journal
sys.path.append("classes")
import template
import db
import config

field = cgi.FieldStorage()
print "Content-Type: text/plain\n\n"
print 'Planning to create a python version of my journal, world!\n'

for request in required_config_vars:
   print "<label for='text" + request + "'>" + required_config_vars[request] + " <input id='text" + request + "' type='text' name='" + request + "' value='" + required_config_values[request] + "' /></lable>"
   

