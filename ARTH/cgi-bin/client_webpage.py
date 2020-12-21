import os
import subprocess
print("Setting your webpage")
print("\n\n")
c=input()
print("your Web page content: ",c)

os.system('touch /var/www/html/client_webpage.html')
fileObject=open("/var/www/html/client_webpage.html", "w")
fileObject.write('{}'.format(c))
fileObject.close()

print("\n See your website- http://13.235.103.58/client_webpage.html")

print("\n Congratulations Your Website is Online")
