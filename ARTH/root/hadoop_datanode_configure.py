import os
print('\n\t\t\t Welcome to hadoop world!!!!')

ip=input()
print("NameNode IP: ",ip)
share_folder="dn"
print("shared folder: ",share_folder)
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



