#!/usr/bin/python

# command_line_arguments.py

import sys

print "script name : ", sys.argv[0]
print "argument : ",

for arg in sys.argv[1:]:
	print arg,

print "\n"
