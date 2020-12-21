ip=input("IP of namenode: ")
print("IP: ",ip)
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


