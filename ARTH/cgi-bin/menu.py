#! /bin/python3
print("content-type: text/plain\n")

import os
import subprocess
import cgi
data=cgi.FieldStorage()
choice=data.getvalue("namenode")
folder=data.getvalue("folder")
os.system('clear')
print('\n\t\t\t Welcome to hadoop world!!!!')
if 4>2:
	if 4>3:
		print("---------------------------")
		x=subprocess.getstatusoutput('sudo mkdir /{}'.format(folder))
		print(x)
		print("let's move forward")	
		subprocess.getstatusoutput('sudo python3')
		print("khtm")	
		
		fileObject = open("/etc/hadoop/hdfs-site.xml", "w")
		fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>')
		fileObject.write('\n\n\n<configuration>')
		fileObject.write('\n\n<property>')
		fileObject.write('\n<name>dfs.name.dir</name>')
		fileObject.write('\n<value>/{}</value>'.format(folder))
		fileObject.write('\n</property>\n\n</configuration>')
		fileObject.close()
		print("hdfs-core done")
		#os.system('ls')
		#os.system('cat /etc/hadoop/hdfs-site.xml')
		
		#core file
		fileObject = open("/etc/hadoop/core-site.xml", "w")
		fileObject.write('<?xml version="1.0" encoding="UTF-8"?>')
		fileObject.write('\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n\n<property>\n')
		fileObject.write('<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n\n</configuration>')
		fileObject.close()
		os.system('hadoop namenode -y -format')
		os.system('hadoop-daemon.sh start namenode')
		os.system('jps')
		print("\nhurry!! Namenode has been configured")
		#print("\n\n Press 1: To see report \n Press 2: Exit \n " )
		#c=input("enter your choice: ")
		#if c == "1" :
		#	os.system('hadoop dfsadmin -report')
		#if c == "2" :
		#	os.system('exit')
		
		
	if choice == '2':
		ip=input("IP of namenode: " )
		
		share_folder=input("Which folder storage would you like to share:" )
		os.system('mkdir /{}'.format(share_folder))
		fileObject = open("/etc/hadoop/hdfs-site.xml", "w")
		fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n\n<property>\n')    
		fileObject.write('<name>fs.data.dir</name>\n<value>/{}</value>\n</property>\n</configuration>'.format(share_folder))

		#core file
		fileObject = open("/etc/hadoop/core-site.xml", "w")
		fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n\n<property>\n')
		fileObject.write('<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>'.format(ip))
		fileObject.close()
		os.system('hadoop-daemon.sh start datanode')
		os.system('jps')
		print("\nhurry!! Datanode has been configured")
		print("\n\n Press 1: To see cluster report \n Press 2: Exit \n " )
		c=input("enter your choice: ")
		if c == "1" :
			os.system('hadoop dfsadmin -report')
		if c =="2" :
			os.system('exit')


	if choice =='3':
		ip=input("IP of namenode: ")
		fileObject = open("/etc/hadoop/hdfs-site.xml", "w")
		fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>')
		fileObject.write('\n\n\n<configuration>')
		fileObject.write('\n\n</configuration>')
		fileObject.close()				
		#core file
		fileObject = open("/etc/hadoop/core-site.xml", "w")
		fileObject.write('<?xml version="1.0"?>')
		fileObject.write('\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n\n<property>\n')
		fileObject.write('<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>'.format(ip))	
		fileObject.close()
		print("\nhurry!! Client  has been configured")
		print("\n\n Press 1: To see report \n Press 2: To upload a file \n Press 3: Create a file \n Press 4: Exit \n " )
		c=input("enter your choice: ")
		if c == "1" :
			os.system('hadoop dfsadmin -report')
		if c =="2" :
			file_name=input('\n Please enter file path: ')
			os.system('hadoop fs -put {} `pwd`'.format(file_name))
		if c =="3" :
			file_name=input('Please create a file name with extension : ')
			os.system('vi `pwd`/{}'.format(file_name))
		if c =="4" :
			os.system('exit')
			
			
		
	if choice =='4':
		print("\n\tWelcome to partition world \n Press 1: For creating physical volume \n Press 2: If physical volume is already created ")
		c=input("\n enter your choice : " )
	
		def pvcreator() :
			H_name=input("\n Enter the volume location in which you want to create partition  ")
			os.system("pvcreate {}".format(H_name))
			print("\n \t Physical volume created!!!!!!!")
			return H_name
		if c =="1" :
			H_name=pvcreator()

		print("\n Please give a name for your volume group ")
		vgname=input("name: ")
		os.system("vgcreate {} {}".format(vgname,H_name))
		os.system("vgdisplay {}".format(vgname))
		print("\n want to add one more physical volume?? ")
		yon=input("yes or no : ")
		if yon == "yes" or yon=="y" :
			pvcreator()
		lvname=input("\n please give a name to your logical volume: " )
		lvsize=input("\n Give size for your partition(lv) : ")
		os.system("lvcreate --size {} --name {} {}".format(lvsize,lvname,vgname))
		
		os.system("lvdisplay {}/{}".format(vgname,lvname))
		print("\n\n formating your partition.........")
		os.system("mkfs.ext4 /dev/{}/{}".format(vgname,lvname))
		print("\n mount your partition!!!!!!!!!!")
		print("\n Give folder location where you want to mount ")
		folder=input("\nenter location: ")
		os.system("mount /dev/{}/{} {}".format(vgname,lvname,folder))
		print("\n folder mounted!!!!!!!!!!!!!!!!")
		os.system("df -h")


	if choice == "5" :
		size=input("\n How much amount you want to increase in your lv : ")		
		vgname=input("\n enter vg name: ")
		lvname=input("\n enter vg name: ")
		os.system("lvextend --size +{} /dev/{}/{}".format(size,vgname,lvname))
		print("Now formating the new added volume in lv!!!!!!")
		os.system("resize2fs /dev/{}/{}".format(vgname,lvname))
		print("completed!!!!")
