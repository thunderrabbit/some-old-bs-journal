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

field = cgi.FieldStorage()
print "Content-Type: text/plain\n\n"
print 'Planning to ask for what we need...\n'

for request in required_config_vars:
   print "<label for='text" + request + "'>" + required_config_vars[request] + " <input id='text" + request + "' type='text' name='" + request + "' value='" + required_config_values[request] + "' /></lable>"
