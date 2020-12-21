#!/bin/python3
print("content-type:text/plain\n")

import os
import subprocess
import cgi
data_taker=cgi.FieldStorage()
service=data_taker.getvalue("submit")
v_path=data_taker.getvalue("v_path")
vg_name=data_taker.getvalue("vg_name")
lv_name=data_taker.getvalue("lv_name")
folder=data_taker.getvalue("folder")
lv_size=data_taker.getvalue("lv_size")
display_group=data_taker.getvalue("display_group")
fdisk=data_taker.getvalue("fdisk")
if service=="create_partition":
	output1=subprocess.getstatusoutput("sudo pvcreate {}".format(v_path))
	print(output1[1])
	output2=subprocess.getstatusoutput("sudo vgcreate {} {}".format(vg_name,v_path))
	print(output2[1])
	output3=subprocess.getstatusoutput("sudo lvcreate --size {} --name {} {}".format(lv_size, lv_name,vg_name))
	print(output3[1])
	output4=subprocess.getstatusoutput("sudo mkfs.ext4 /dev/{}/{}".format(vg_name,lv_name))
	print(output4[1])
	subprocess.getstatusoutput("sudo mkdir {}".format(folder))
	output5=subprocess.getstatusoutput("sudo mount {} {}".format(v_path,folder ))
	print(output5[1])
	output=subprocess.getstatusoutput("sudo df -h")
	print(output[1])	
	
if display_group =="vg":
	output=subprocess.getstatusoutput("sudo vgdisplay")
	print(output[1])
elif display_group=="lv":
	output=subprocess.getstatusoutput("sudo lvdisplay")
	print(output[1])

if service=="display_mount":
	output=subprocess.getstatusoutput("sudo df -h")
	print(output[1])
	
if service=="extend_lvm":
	output=subprocess.getstatusoutput("")

if service=="fdisk":
	output=subprocess.getstatusoutput("sudo fdisk -l")
	print(output[1])
