#!/bin/python3
print("content-type:text/plain\n")

import os
import subprocess
import cgi
data_taker=cgi.FieldStorage()
service=data_taker.getvalue("submit")
namenode_ip=data_taker.getvalue("namenode_ip")
namenode_folder=data_taker.getvalue("namenode_folder")
#datanode_folder=data_taker.getvalue("datanode_folder")
file_name=data_taker.getvalue("file_name")
file_content=data_taker.getvalue("file_content")
if service=="namenode_configure":
	output=subprocess.getstatusoutput("echo {} | sudo python3 /hadoop_namenode_configure.py".format(namenode_folder))
	print(output[1])

if service=="datanode_configure":
        output=subprocess.getstatusoutput("echo {} | sudo python3 /hadoop_datanode_configure.py".format(namenode_ip))
        print(output[1])

if service=="report":
        output=subprocess.getstatusoutput("sudo hadoop dfsadmin -report")
        print(output[1])

if service=="client_configure":
        output=subprocess.getstatusoutput("echo {} | sudo python3 /hadoop_client_configure.py".format(namenode_ip))
        print(output[1])	

if service=="file_upload":
	
	
	output=subprocess.getstatusoutput("echo {} | sudo python3 /file.py".format(file_content))
	print(output)
	file_name='first'
	output=subprocess.getstatusoutput("sudo hadoop fs -put /{}.txt /home/ec2-user".format(file_name))
	print(output)
	#if output[0]==0:
	#	print("File uploaded sucesfully!!")

if service=="open_file":
	output=subprocess.getstatusoutput("sudo cat  /{}.txt".format(file_name))
	print(output[1])

if service=="show_files":
	output=subprocess.getstatusoutput("sudo hadoop fs -ls /")
	print(output[1])
