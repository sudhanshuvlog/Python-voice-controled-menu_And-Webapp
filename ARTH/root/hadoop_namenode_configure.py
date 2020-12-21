import os
print('\n\t\t\t Welcome to hadoop world!!!!')

folder=input()
os.system('mkdir /{}'.format(folder))
print(folder)
#folder="nn"
fileObject=open("/etc/hadoop/hdfs-site.xml", "w")
fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>')
fileObject.write('\n\n\n<configuration>')
fileObject.write('\n\n<property>')
fileObject.write('\n<name>dfs.name.dir</name>')
fileObject.write('\n<value>/{}</value>'.format(folder))
fileObject.write('\n</property>\n\n</configuration>')
fileObject.close()
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
print("------------------------------------\n\n")
os.system('jps')
print("\nhurry!! Namenode has been configured")
                
