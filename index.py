#!/usr/bin/env python
import cgi
import os.path
import pickle
# os.path - The key to File I/O

field = cgi.FieldStorage()
print "Content-Type: text/plain\n\n"
print 'Planning to create a python version of my journal, world!\n'

class init:
  __Template__()
  {
     _page : ""
  }

print Template
US = {"Sammy":0,"summy":0,"spoonman":0}

required_config_vars = {
    "db_name":"enter the name of the database",
    "db_user":"enter your database username",
    "db_pass":"enter your database password"
    }

# these will be read from $_POST, but just putting them here for testing
required_config_values = {
    "db_name":"keep_pushing_the_limits",
    "db_user":"pushy",
    "db_pass":"pass"
    }

print US;

configuration_infile = "/Users/thunderrabbit/php_file_journal/config.sample"
configuration_outfile = "/Users/thunderrabbit/php_file_journal/config"

print os.path.exists(configuration_outfile)
print os.path.isfile(configuration_outfile)
print os.path.isdir(configuration_outfile)
print os.path.isabs(configuration_outfile)

wepickle = pickle.dumps(US)

print(wepickle)

print "Writing to file: %s" % configuration_outfile
file = open(configuration_outfile, 'w')
file.write("This is the new content of %s :-)\n" % configuration_outfile)
file.write("%s is a great file, doncha know.\n" % configuration_outfile)
file.close()

file = open(configuration_infile, 'r')
elbow = file.readlines()
file.close()

for request in required_config_vars:
   print "<label for='text" + request + "'>" + required_config_vars[request] + " <input id='text" + request + "' type='text' name='" + request + "' value='" + required_config_values[request] + "' /></lable>"
   

