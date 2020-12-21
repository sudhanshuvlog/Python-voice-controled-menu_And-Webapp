#!/bin/python3
print("content-type:text/plain\n")

import os
import subprocess as sb 
import cgi
command_taker=cgi.FieldStorage()

command=command_taker.getvalue("command")
output=sb.getstatusoutput("sudo {}".format(command))
print(output[1])

