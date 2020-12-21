import os
import subprocess
print("hellllllooooo")
c=input()
print(c)

os.system('touch /first.txt')
fileObject=open("/first.txt", "w")
fileObject.write('{}'.format(c))
fileObject.close()

