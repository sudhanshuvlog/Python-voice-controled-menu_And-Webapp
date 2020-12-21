#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import os
import time
import subprocess
server_ip="" 


# In[2]:


import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("") 


# In[3]:


print("hello")


# In[4]:


r=sr.Recognizer()
def head():
    os.system('cls')
    print('''\t=========== Welcome to the World of Automation!! ===========
                1. Hadoop
                2. AWS Cloud
                3. Web Server
                4. Docker
                5. Partition
                6. Exit
    ''') 
    speak.Speak('''\tWelcome to the World of Automation!! 
                1. Hadoop
                2. AWS Cloud
                3. Web Server
                4. Docker
                5. Partition
                6. Exit
    ''') 
                


# In[1]:


def hadoop():
    os.system('cls')
    while(True):
        #os.system('cls')
        print('''\t\t Welcome to the Hadoop Menu!! 
                    1. Configure Namenode
                    2. Configure Datanode
                    5. Configure Client
                    6. Show Report of Cluster
                    7. Show files in Cluster
                    8. Open file stored in Cluster
                    9. Exit
        ''')
        
        speak.Speak('''\t\tWelcome to the Hadoop Menu!!
                    1. Configure Namenode
                    2. Configure Datanode
                    5. Configure Client
                    6. Show Report of Cluster
                    7. Show files in Cluster
                    8. Open file stored in Cluster
                    9. Exit
        ''')
        ss1=input("Press Enter to continue...")
        speak.Speak("Please enter to continue")

        #Function for client
        def client():
            print('''\t\t======= Welcome to Client Menu!! =======
                         a) Create a File
                         b) Upload a File
                         c) Delete a File from Cluster
                         d) Exit
            ''')
            speak.Speak('''\t\t welcome to Client Menu!!
                         a) Create a File
                         b) Upload a File
                         c) Delete a File from Cluster
                         d) Exit
            ''')
            speak.Speak("Welcome to client menu")
            speak.Speak("What can i do for you sir")
            ss6_1=input('Press enter to continue... ')
            chad=None
            while(chad!='exit'):
                with sr.Microphone() as source:
                    print('Tell us your requirement...')
                    audio6_1 =r.listen(source)
                    print('Okay got it!!')
                    chad=r.recognize_google(audio6_1)
                print(chad)
                if 'wait' in chad or 'pause' in chad:
                    inp=input('Press enter to continue')
                    if inp!='exit':
                        continue
                    else:
                        break
                elif 'create file' in chad or 'please create file' in chad:
                    chad1=input('Please enter file name : ')
                    os.system('curl http://{}/cgi-bin/cmd.py?cmd=vi+%2F{}'.format(server_ip))
                elif 'upload file' in chad or 'upload a file' in chad:
                    chad1=input('\n Please enter file content: ')
                    os.system('curl http://{}/cgi-bin/cmd.py?cmd=hadoop+fs+-put+{}+%2F'.format(server_ip,chad1))
                elif 'delete file' in chad or 'delete a file' in chad:
                    chad1=input('Please enter file name: ')
                    os.system('curl http://{}/cgi-bin/cmd.py?cmd=hadoop+fs+-rm+%2F{}'.format(server_ip,chad1))
                elif 'exit' in chad:
                    break
                else:
                    print('Invalid Option (-_-)')           
        with sr.Microphone() as source:
            print('Tell us your requirement...')
            audio1 =r.listen(source)
            print('Okay got it!!')
            had=r.recognize_google(audio1)
        print(had)
        if 'wait' in had or 'pause' in had:
            inp=input('Press enter to continue')
            if inp!='exit':
                continue
            else:
                break
        if 'namenode' in had:
            folder=input("which folder would you want to assign your namenode:  ")
            output=subprocess.getstatusoutput('start chrome "http://{}/cgi-bin/hadoop.py?namenode_folder={}&submit=namenode_configure"'.format(server_ip,folder))
            print(output[1])
            if(output[0]==0):
                print("\nNamenode has been configured!")
        elif 'datanode' in had or 'Datanode' in had or 'configure' in had:
            namenode_ip=input("IP of namenode: ")
            #share_folder=input("Which folder storage would you like to share:" )
            output=subprocess.getstatusoutput('start chrome "http://{}/cgi-bin/hadoop.py?namenode_ip={}&datanode_folder=dn&submit=datanode_configure"'.format(server_ip,namenode_ip))
            if output[0]==0:
                print("\n Datanode has been configured!")
            else:
                print("\n some error occured")
        elif 'client' in had:
            ip=input("IP of namenode: ")
             
            print("Client  has been configured!")
            client()
        elif 'report' in had:
            os.system('curl http://{}/cgi-bin/hadoop.py?submit=report'.format(server_ip))
        elif 'show file' in had or 'show files' in had or 'show the files' in had:
            os.system('curl http://{}/cgi-bin/hadoop.py?submit=show_files'.format(server_ip))
        elif 'open' in had:
            os.system('curl http://{}/cgi-bin/hadoop.py?submit=show_files'.format(server_ip))
            had1=input('Please enter file name: ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=hadoop+fs+-cat+%2F{}'.format(server_ip,had1))
        elif 'exit' in had:
            break
        else:
            print('Invalid Option (-_-)')


# unction for AWS Cloud

# In[3]:


def aws():
    

    #Function for EC2
    def ec2():
        os.system('cls')
        print('''\t\t======= Welcome to EC2 Services Menu!! =======
                        a) Launch Instance
                        b) Show details of all instances
                        c) Show details of any one instance
                        d) Start Instance
                        e) Stop Instance
                        f) Terminate Instance
                        g) Exit
            ''')
        
        speak.Speak('''Welcome to EC2 Services Menu!!
                        a) Launch Instance
                        b) Show details of all instances
                        c) Show details of any one instance
                        d) Start Instance
                        e) Stop Instance
                        f) Terminate Instance
                        g) Exit
            ''')
        inp1=input('Press enter to continue: ')
        ec=None
        while(ec!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                audio1 =r.listen(source)
                print('Okay got it!!')
            ec=r.recognize_google(audio1)
            print(ec)
            if 'wait' in ec or 'pause' in ec:
                inp=input('Press enter to continue')
                speak.Speak("What can i do for you sir")
                if inp!='exit':
                    continue
                else:
                    break
            if 'launch instance' in ec or 'launch an instance' in ec:
                ch1=input('Enter the image id: ')
                ch2=input('Enter key name: ')
                ch3=input('Enter security group name: ')
                ch4=input('Enter instance type ')
                
                #cmd='/usr/local/bin/aws ec2 run-instances --image-id {} --instance-type t2.micro --count {} --subnet-id {} --key-name {}'.format(ch1,ch3,ch4,ch2)
                os.system('start chrome "http://{}/cgi-bin/1.py?ami_id={}&instance_type={}&key_name={}&security_group={}&submit=launch"'.format(server_ip,ch1,ch4,ch2,ch3))
            elif 'details of all instances' in ec or 'details of all instance' in ec:
                os.system('curl http://{}/cgi-bin/1.py?submit=describe_instances'.format(server_ip))
            elif 'details of one instance' in ec or 'details of any one instance' in ec or 'one instance' in ec:
                ch1=input('Enter instance id: ')
                cmd='aws+ec2+describe-instances+--instance-id++{}'.format(ch1)
                os.system('curl http://{}/cgi-bin/cmd.py?cmd={}'.format(server_ip,cmd))
            elif 'start instance' in ec or 'start' in ec:
                ch1=input('Enter instance id: ')
                cmd='aws+ec2+start-instances+--instance-id++{}'.format(ch1)
                os.system('curl http://{}/cgi-bin/cmd.py?cmd={}'.format(server_ip,cmd))
            elif 'stop instance' in ec or 'stop an instance' in ec or 'stop' in ec:
                ch1=input('Enter instance id: ')
                cmd='aws+ec2+stop-instances+--instance-id++{}'.format(ch1)
                os.system('curl http://{}/cgi-bin/cmd.py?cmd={}'.format(server_ip,cmd))
            elif 'terminate instance' in ec or 'terminate' in ec:
                ch1=input('Enter instance id: ')
                cmd='aws+ec2+terminate-instances+--instance-id++{}'.format(ch1)
                os.system('curl http://{}/cgi-bin/cmd.py?cmd={}'.format(server_ip,cmd))
            elif 'exit' in ec:
                break
            else:
                print('Invalid Option (-_-)')

    #Function for EBS Volume
    def ebs():
        os.system('cls')
        print('''\t\t======= Welcome to EBS Menu!! =======
                     a) Create Volume
                     b) Attach Volume
                     c) Delete Volume
                     d) Details of all Volumes
                     e) Exit
        ''')
        speak.Speak('''Welcome to EBS Menu!! 
                     a) Create Volume
                     b) Attach Volume
                     c) Delete Volume
                     d) Details of all Volumes
                     e) Exit
        ''')
        inp1=input('Press enter to continue: ')
        speak.Speak("What can i do for you sir")
        ebs=None
        while(ebs!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                audio2 =r.listen(source)
                print('Okay got it!!')
            ebs=r.recognize_google(audio2)
            print(ebs)
            if 'wait' in ebs or 'pause' in ebs:
                inp=input('Press enter to continue')
                if inp!='exit':
                    continue
                else:
                    os.system('exit')
            if 'create volume' in ebs or 'create ebs volume' in ebs or 'create an ebs volume' in ebs:
                zone=input('Enter the Availability Zone: ')
                size=int(input('Enter the size: '))
                os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(zone,size))
            elif 'attach volume' in ebs or 'attach an ebs volume' in ebs or 'attach ebs volume' in ebs:
                ebs1=input('Enter device name where you want to attach the EBS Volume(Eg. /dev/xvda): ')
                ebs2=input('Enter the instance id to which you want to connect the volume: ')
                ebs3=input('Enter the volume id which you want to attach')
                os.system('aws ec2 attach-volume --device {} --instance-id {} --volume-id {}'.format(ebs1,ebs2,ebs3))
            elif 'delete volume' in ebs or 'delete ebs volume' in ebs or 'delete an ebs volume' in ebs:
                ebs1=input('Enter the volume id: ')
                os.system('aws ec2 delete-volume --volume-id {}'.format(ebs1))
            elif 'details of all volumes' in ebs or 'detail of volumes' in ebs or 'detail of all volumes' in ebs:
                os.system('aws ec2 describe-volumes')
            elif 'exit' in ebs:
                break
            else:
                print('Invalid Option (-_-)')

    #Function for Key
    def key():
        os.system('cls')
        print('''\t\t======= Welcome to Key Pair Menu!! =======
                     a) Create key
                     b) Delete key
                     c) Show Details of Key-Pair
                     c) Exit
        ''')
        speak.Speak('''Welcome to Key Pair Menu!! 
                     a) Create key
                     b) Delete key
                     c) Show Details of Key-Pair
                     c) Exit
        ''')
        inp1=input('Press enter to continue: ')
        k=None
        while(k!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                  
                audio3 =r.listen(source)
                print('Okay got it!!')
            k=r.recognize_google(audio3)
            print(k)
            if 'wait' in k or 'pause' in k:
                inp=input('Press enter to continue: ')
                speak.Speak("What can i do for you sir")
                if inp!='exit':
                    continue
                else:
                    os.system('exit')
            if 'create key' in k or 'create a key' in k or 'create a key pair' in k or 'create key pair' in k:
                k1=input('Enter key name: ')
                os.system('aws ec2 create-key-pair --key-name {}'.format(k1))
            elif 'delete key' in k or 'delete a key' in k or 'delete a key pair' in k or 'delete a key pair' in k:
                k1=input('Enter key name: ')
                os.system('aws ec2 delete-key-pair --key-name {}'.format(k1))
            elif 'details of key' in k:
                os.system('aws ec2 describe-key-pairs')
            elif 'exit' in k:
                break
            else:
                print('Invalid Option (-_-)')

    #Function for S3
    def s3():
        os.system('cls')
        print('''\t\t======= Welcome to S3 Menu!! =======
                     a) Create bucket
                     b) Delete empty bucket
                     c) Upload any file in bucket
                     d) Delete bucket
                     e) Show bucket details
                     f) Exit
        ''')
        speak.Speak('''Welcome to S3 Menu!! 
                     a) Create bucket
                     b) Delete empty bucket
                     c) Upload any file in bucket
                     d) Delete bucket
                     e) Show bucket details
                     f) Exit
        ''')
        inp1=input('Press enter to continue: ')
        speak.Speak("what can i do for you sir")
        s=None
        while(s!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                audio4 =r.listen(source)
                print('Okay got it!!')
            s=r.recognize_google(audio4)
            print(s)
            if 'wait' in s or 'pause' in s:
                inp=input('Press enter to continue: ')
                if inp!='exit':
                    continue
                else:
                    os.system('exit')
            if 'create bucket' in s or 'create a bucket' in s:
                s1=input('Enter bucket name: ')
                os.system('aws s3 mb s3://{}'.format(s1))
            elif 'delete an empty bucket' in s or 'delete empty bucket' in s:
                s1=input('Enter bucket name: ')
                os.system('aws s3 rb s3://{}'.format(s1))
            elif 'upload file' in s or 'upload any file' in s or 'upload a file' in s:
                s1=input('Enter path of file: ')
                s2=input('Enter bucket name to which you want to copy: ')
                os.system('aws s3 cp {} s3://{}'.format(s1,s2))
            elif 'delete a bucket' in s or 'delete bucket' in s:
                s1=input('Enter bucket name: ')
                os.system('aws s3 rb s3://{} --force'.format(s1))
            elif 'details of bucket' in s or 'show bucket details' in s:
                os.system('aws s3 ls')
            elif 'exit' in s:
                break
            else:
                print('Invalid Option (-_-)')

    #Function for Snapshot
    def snapshot():
        os.system('cls')
        print('''\t\t======= Welcome to Snapshot Menu!! =======
                     a) Create snapshot
                     b) Delete snapshot
                     c) Show details of snapshot
                     c) Exit
        ''')
        speak.Speak('''Welcome to Snapshot Menu!! 
                     a) Create snapshot
                     b) Delete snapshot
                     c) Show details of snapshot
                     c) Exit
        ''')
        
        inp1=input('Press enter to continue: ')
        snap=None
        while(snap!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                audio5 =r.listen(source)
                print('Okay got it!!')
            snap=r.recognize_google(audio5)
            print(snap)
            if 'wait' in snap or 'pause' in snap:
                inp=input('Press enter to continue: ')
                if inp!='exit':
                    continue
                else:
                    os.system('exit')
            if 'create snapshot' in snap or 'create a snapshot' in snap:
                snap1=input('Enter the volume id for which you want to create snapshot: ')
                os.system('aws ec2 create-snapshot --volume-id {}'.format(snap1))
            elif 'delete snapshot' in snap or 'delete a snapshot' in snap:
                snap1=input('Enter snapshot id: ')
                os.system('aws ec2 delete-snapshot --snapshot-id {}'.format(snap1))
            elif 'show details of snapshot' in snap or 'show detail of snapshots' in snap or 'show the detail of snapshots' in snap or 'show the details of snapshot' in snap:
                os.system('aws ec2 describe-snapshots')
            elif 'exit' in snap:
                break
            else:
                print('Invalid Option (-_-)')
    menu2=None
    os.system('cls')
    os.system('aws configure')
    while(menu!='exit'):
        os.system('cls')
        print('''\n\t\tWelcome to the AWS Menu!!
                    1. EC2 services
                    2. EBS volume
                    3. Key-Pair
                    4. S3
                    5. Snapshot
                    6. Exit
        ''')
        speak.Speak('''Welcome to the AWS Menu!!
                    1. EC2 services
                    2. EBS volume
                    3. Key-Pair
                    4. S3
                    5. Snapshot
                    6. Exit
        ''')
        ssk=input("Press Enter to continue...")
        with sr.Microphone() as source:
            print('Tell us your requirement...')
            audio2 =r.listen(source)
            print('Okay got it!!')
        menu2=r.recognize_google(audio2)
        print(menu2)
        if 'ec2' in menu2:
            ec2()
        elif 'ebs' in menu2 or 'volume' in menu2:
            ebs()
        elif 'key pair' in menu2 or 'key' in menu2:
            key()
        elif 's3' in menu2 or 'S3' in menu2:
            s3()
        elif 'snapshot' in menu2:
            snapshot()
        elif 'exit' in menu2:
            break
        else:
            print('Invalid Option (-_-)')


# In[5]:


def web():
    os.system('cls')
    print('''\t\t======= Welcome to the Web Server Menu!! =======
                1. Configure Web Server
                2. Create file and upload it
                3. Edit the shared file
                4. Delete the shared file
                5. Stop Web Server services
                6. Exit
    ''')
    speak.Speak('''\t\t Welcome to the Web Server Menu!! 
                1. Configure Web Server
                2. Create file and upload it
                3. Edit the shared file
                4. Delete the shared file
                5. Stop Web Server services
                6. Exit
    ''')
    ss1=input("Press Enter to continue...")
    while(True):
        with sr.Microphone() as source:
            print('Tell us your requirement...')
            audio1 =r.listen(source)
            print('Okay got it!!')
            webs=r.recognize_google(audio1)
        print(webs)
        if 'wait' in webs or 'pause' in webs:
                    inp=input('Press enter to continue')
                    if inp!='exit':
                        continue
                    else:
                        break
        if 'configure web server' in webs or 'configure' in webs or 'Configure' in webs :
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=sudo+yum+install+httpd'.format(server_ip))
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=sudo+systemctl+start+httpd'.format(server_ip))
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=sudo+setenforce+0'.format(server_ip))
        elif 'create and open file' in webs or 'create file' in webs or 'upload' in webs or 'launch website' in webs:
            webs1=input('\n Enter file content: ')
            output =subprocess.getstatusoutput('start chrome "http://{}/cgi-bin/web.py?file_content={}&submit=launch_website"'.format(server_ip,webs1))
            print(output[0])
            os.system('start chrome "http://{}/client_webpage.html"'.format(server_ip))
        #elif 'edit the shared file' in webs or 'edit shared file' in webs or 'edit the share file' in webs or 'edit share file' in webs:
        #    webs1=input('Enter the file name: ')
        #    os.system('cd /var/www/html')
        #    os.system('ls')
        #    os.system('vim {}'.format(webs1))
        elif 'delete the shared file' in webs or 'delete the share file' in webs or 'delete shared file' in webs or 'delete share file' in webs:
            #webs1=input('Enter the file name: ')
            print("deleting your file.....")
            #os.system('curl http://{}/cgi-bin/cmd.py?cmd=%2Fvar%2Fwww%2Fhtml+-l'.format(server_ip))
            #os.system('ls')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=rm+-rf+%2Fvar%2Fwww%2Fhtml%2Fclient_webpage.html'.format(server_ip))
        elif 'stop services' in webs or 'stop web services' in webs or 'stop the web services' in webs:
            os.system('systemctl stop httpd')
            os.system('systemctl start firewalld')
        elif 'exit' in webs:
            break
        else:
            print('Invalid Option (-_-)')
#head()
#sk3=input('Press enter to continue')


# unction for docker

# In[8]:


def docker():
    while(True):
        #os.system('cls')
        print('''\n\t\tWelcome to the Docker Menu!!
                    1. Configure Docker
                    2. Pull Image
                    3. Launch Container
                    4. Show Information of all Containers
                    5. Attach Container
                    6. Start Conatiner
                    7. Stop Container
                    8. Remove Image
                    9. Delete Container
                    10.Delete all Containers
                    11.Image Information
                    12.Exit
        ''')
        ss1=input("Press Enter to continue...")
     
        with sr.Microphone() as source:
            print('Tell us your requirement...')
            audio1 =r.listen(source)
            print('Okay got it!!')
            doc=r.recognize_google(audio1)
        print(doc)
        if 'wait' in doc or 'pause' in doc:
                inp=input('Press enter to continue')
                if inp!='exit':
                    continue
                else:
                    break
        if 'configure docker' in doc:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=yum+install+docker+-y'.format(server_ip))
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=stop+firewalld'.format(server_ip))
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=systemctl+start+docker'.format(server_ip))
        elif 'pull image' in doc or 'pull an image' in doc or "full" in doc or "image" in doc or "put" in doc:
            doc1=input('Enter OS type: ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=docker+pull+{}'.format(server_ip,doc1))
        elif 'launch container' in doc or 'launch a container' in doc:
            doc1=input('Enter the name of container: ')
            doc2=input('Enter OS type: ')
            os.system('start chrome "http://{}/cgi-bin/docker.py?image_name={}&os_name={}&submit=start_new_os"'.format(server_ip,doc2,doc1))
        elif 'information of all containers' in doc or 'information of containers' in doc:
            os.system('curl http://{}/cgi-bin/docker.py?submit=display_all_os'.format(server_ip))
        elif 'attach container' in doc or 'attach the container' in doc or 'attach' in doc:
            doc1=input('Enter container name: ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=docker+attach+ {}'.format(server_ip,doc1))
        elif 'start the conatiner' in doc or 'start conatiner' in doc or 'start' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('start chrome "http://{}/cgi-bin/docker.py?start_stop=start&os_name={}&submit=start_stop"'.format(server_ip,doc1))
        elif 'stop the container' in doc or 'stop conatiner' in doc or 'stop' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('curl http://{}/cgi-bin/docker.py?submit=display_all_os'.format(server_ip))
            output=subprocess.getstatusoutput('start chrome "http://{}/cgi-bin/docker.py?start_stop=stop&os_name={}&submit=start_stop"'.format(server_ip,doc1))
            print(output[0])
            if(output[0]!=0):
                print("Wrong container name")
            os.system('curl http://{}/cgi-bin/docker.py?submit=display_all_os'.format(server_ip))
        elif 'remove an image' in doc or 'remove the image' in doc or 'remove image' in doc:
            doc1=input('Enter OS type: ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=docker+rmi+-f+{}:latest'.format(server_ip,doc1))
        elif 'delete a container' in doc or 'delete the container' in doc or 'delete container' in doc or 'delete 1' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=docker+rm+-f+{}'.format(server_ip,doc1))
        elif 'delete all containers' in doc or 'delete the containers' in doc:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=sudo+docker+rm+`docker+ps+-a+-q`'.format(server_ip))
        elif 'information of image' in doc or 'image information' in doc or 'information of images' in doc:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=docker+images'.format(server_ip))
        elif 'exit' in doc:
            break
        else:
            print('Invalid Option (-_-)')
#head()
#sk4=input('Press enter to continue')


# unction for partition

# In[9]:


def partition():
#if(3>1):
    #Function for LVM Creation
    def crpartition():
        os.system('cls')
        print('''\t\t======= Welcome to Creation of LVM Partition!! =======
                    a) Create Physical Volume (PV)
                    b) Create Volume Group (VG)
                    c) Add another PV to Volume Group
                    d) Create Logical Volume (LV)
                    e) Format the Partition
                    f) Mount the Partition
                    g) Exit
                ''')
        ss5_1=input("Press enter to continue...")
        cpar=None
        while(cpar!='exit'):
            with sr.Microphone() as source:
                print('Tell us your requirement...')
                audio5_1 =r.listen(source)
                print('Okay got it!!')
                cpar=r.recognize_google(audio5_1)
            print(cpar)
            if 'wait' in cpar or 'pause' in cpar:
                inp=input('Press enter to continue')
                if inp!='exit':                                                           
                    continue
                else:                                                                
                    break
            if 'create pv' in cpar or 'create PV' in cpar or 'create physical volume' in cpar:
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=fdisk+-l'.format(server_ip))
                cpar1=input('Enter the hard-disk name: ')
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=pvcreate+{}'.format(server_ip,cpar1))
            elif 'create vg' in cpar or 'create a vg' in cpar or 'create volume group' in cpar:
                cpar1=input('Enter the no. of PVs you want to attach: ')
                vgname=input('give your Vg a name')
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=pvdisplay'.format(server_ip))
                cpars=[]
                i=0
                while(i < int(cpar1)):
                    cpar2=input('Enter pv -{} name: '.format(i+1))
                    cpars.append(cpar2)
                    i+=1
                if int(cpar1)==1:
                    for cparss in cpars:
                        os.system('start chrome "http://{}/cgi-bin/cmd.py?cmd=vgcreate+{}+{}"'.format(server_ip,vgname,cpars[0]))
                else :
                    for cparss in cpars:
                        os.system('start chrome "http://{}/cgi-bin/cmd.py?cmd=vgcreate+{}+{}+{}"'.format(server_ip,vgname,cpars[0],cpars[1]))
            elif 'extend vg' in cpar:
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=pvdisplay'.format(server_ip))
                cpar1=input('Enter PV name: ')
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=vgextend+{}'.format(server_ip,cpar1))
            elif 'create lv' in cpar or 'create logical volume' in cpar:
                os.system('vgdisplay')
                cpar1=input('Enter VG name: ')
                cpar2=input('Enter LV name: ')
                cpar3=input('Enter size you want to give to Lv (eg. 1G,M): ')
                os.system('start chrome "http://{}/cgi-bin/cmd.py?cmd=lvcreate+--size+{}+--name+{}+{}"'.format(server_ip,cpar3,cpar2,cpar1))
            elif 'format' in cpar:
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=lvdisplay'.format(server_ip))
                cpar1=input('Give LV path: ')
                os.system('start chrome "http://{}/cgi-bin/cmd.py?cmd=mkfs.ext4+{}"'.format(server_ip,cpar1))
            elif 'mount' in cpar:
                cpar1=input('Enter folder name: ')
                os.system('curl http://{}/cgi-bin/cmd.py?cmd=mkdir+%2F{}'.format(server_ip,cpar1)) #%2F = '/'
                cpar2=input('Give LV path: ')
                os.system('start chrome "http://{}/cgi-bin/cmd.py?cmd=mount+{}+%2F{}"'.format(server_ip,cpar2,cpar1))
            elif 'exit' in cpar:
                break
            else:
                print('Invalid Option (-_-)')
    while(True):
        
        print('''\t\t======= Welcome to the Partition Menu!! =======
                1. Create LVM partition
                2. Resize the LVM Partition
                5. Display Details of the Hard-Disks
                6. Display all the Mounted Partitions
                7. Display Details of Physical Volumes
                8. Dispaly Details of Volume Group
                9. Display Details of Logical Volume
                10.Exit
        ''')
        ss1=input("Press Enter to continue...")
        with sr.Microphone() as source:
            print('Tell us your requirement...')
            audio1 =r.listen(source)
            print('Okay got it!!')
            par=r.recognize_google(audio1)
        print(par)
        if 'wait' in par or 'pause' in par:
            inp=input('Press enter to continue')
            if inp!='exit':
                continue
            else:
                break
        if 'create an lvm partition' in par or 'create lvm partition' in par:
            crpartition()
        elif 'resize the lvm partition' in par or 'resize lvm partition' in par:
            par1=input('Enter how much size you want to increase(eg. 1G,M): ')
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=lvdisplay'.format(server_ip))
            par2=input('Give vg name: ')
            par3=input('give lv name: ')
            os.system('start chrome "http://{}/cgi-bin/part.py?volume_path=%2Fdev%2F{}%2F{}&volume_increase_size={}&submit=extend_lvm"'.format(server_ip,par2,par3,par1))
            
        elif 'information of hard disk' in par or 'info of hard disk' in par or 'hard disk info' in par or 'hard disk information' in par:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=fdisk+-l'.format(server_ip))
        elif 'mounted' in par or 'mount' in par:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=df+-h'.format(server_ip))
        elif 'physical volume' in par or 'pv' in par:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=pvdisplay'.format(server_ip))
        elif 'volume group' in par or 'vg' in par:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=vgdisplay'.format(server_ip))
        elif 'logical volume' in par or 'lv' in par:
            os.system('curl http://{}/cgi-bin/cmd.py?cmd=lvdisplay'.format(server_ip))
        elif 'exit' in par:
            break
        else:
            print('Invalid Option (-_-)')


# In[17]:


menu=None
server_ip=input("enter your server ip: ")
while(menu!='exit'):
    with sr.Microphone() as source:
        head()
        skk=input('Press enter to continue')
        speak.Speak('What would you like to do sir')
        print('Tell us your requirement...')
        audio =r.listen(source)
        print('Okay got it!!')
    menu=r.recognize_google(audio)
    print(menu)
    if 'hadoop' in menu or 'Hadoop' in menu or 'cluster' in menu:
        hadoop()
    elif 'aws' in menu or 'cloud' in menu or 'AWS' in menu:
        aws()
    elif 'web server' in menu:
        web()
    elif 'docker' in menu:
        docker()
    elif 'partition' in menu:
        partition()
    elif 'exit' in menu:
        break
    else:
        print('Invalid Option (-_-)')


# In[ ]:




