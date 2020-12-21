import speech_recognition as sr
import os
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

#Function for hadoop
def hadoop():
    while(True):
        os.system('clear')
        print('''\t\t======= Welcome to the Hadoop Menu!! =======

                    1. Configure Namenode
                    2. Configure Datanode
                    5. Configure Client
                    6. Show Report of Cluster
                    7. Show files in Cluster
                    8. Open file stored in Cluster
                    9. Exit
        ''')
        ss1=input("Press Enter to continue...")

        #Function for client
        def client():
            print('''\t\t======= Welcome to Client Menu!! =======

                         a) Create a File
                         b) Upload a File
                         c) Delete a File from Cluster
                         d) Exit
            ''')
            ss6_1=input('Press enter to continue... ')
            chad=None
            while(chad!='exit'):
                with sr.Microphone() as source:
                    print('Tell us your requirement...')
                    audio6_1 =r.listen(source)
                    print('Okay got it!!')
                    chad=r.recognize_google(audio6_1)
                print(chad)
                if 'wait' in had or 'pause' in had:
                    inp=input('Press enter to continue')
                    if inp!='exit':
                        continue
                    else:
                        break
                elif 'create file' in chad or 'create file' in chad:
                    chad1=input('Please enter file name : ')
                    os.system('vi {}'.format(chad1))
                elif 'upload file' in chad or 'upload a file' in chad:
                    chad1=input('\n Please enter file name: ')
                    os.system('hadoop fs -put {} /'.format(chad1))
                elif 'delete file' in chad or 'delete a file' in chad:
                    chad1=input('Please enter file name: ')
                    os.system('hadoop fs -rm /{}'.format(chad1))
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
            os.system('mkdir /{}'.format(folder))
            fileObject = open("/etc/hadoop/hdfs-site.xml", "w")
            fileObject.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            fileObject.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>')
            fileObject.write('\n\n\n<configuration>')
            fileObject.write('\n\n<property>')
            fileObject.write('\n<name>dfs.name.dir</name>')
            fileObject.write('\n<value>/{}</value>'.format(folder))
            fileObject.write('\n</property>\n\n</configuration>')
            fileObject.close()
            #core file
            fileObject = open("/etc/hadoop/core-site.xml", "w")
            fileObject.write('<?xml version="1.0" encoding="UTF-8"?>')
            fileObject.write('\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n\n<property>\n')
            fileObject.write('<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n\n</configuration>')
            fileObject.close()
            os.system('hadoop namenode -y -format')
            os.system('hadoop-daemon.sh start namenode')
            os.system('jps')
            print("\nNamenode has been configured!")
        elif 'datanode' in had:
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
            print("\nDatanode has been configured!")
        elif 'client' in had:
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
            print("Client  has been configured!")
            client()
        elif 'report' in had:
            os.system('hadoop dfsadmin -report')
        elif 'show file' in had or 'show files' in had or 'show the files' in had:
            os.system('hadoop fs -ls /')
        elif 'open' in had:
            os.system('hadoop fs -ls /')
            had1=input('Please enter file name: ')
            os.system('hadoop fs -cat /{}'.format(had1))
        elif 'exit' in had:
            break
        else:
            print('Invalid Option (-_-)')

#Function for AWS Cloud
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
                if inp!='exit':
                    continue
                else:
                    break
            if 'launch instance' in ec or 'launch an instance' in ec:
                ch1=input('Enter the image id: ')
                ch2=input('Enter key name: ')
                ch3=int(input('Enter the no. of instances you wanna launch: '))
                ch4=input('Enter subnet id: ')
                os.system('aws ec2 run-instances --image-id {} --instance-type t2.micro --count {} --subnet-id {} --key-name {}'.format(ch1,ch3,ch4,ch2))
            elif 'details of all instances' in ec or 'details of all instance' in ec:
                os.system('aws ec2 describe-instances')
            elif 'details of one instance' in ec or 'details of any one instance' in ec or 'one instance' in ec:
                ch1=input('Enter instance id: ')
                os.system('aws ec2 describe-instances --instance-id {}'.format(ch1))
            elif 'start instance' in ec:
                ch1=input('Enter instance id: ')
                os.system('aws ec2 start-instances --instance-id {}'.format(ch1))
            elif 'stop instance' in ec or 'stop an instance' in ec:
                ch1=input('Enter instance id: ')
                os.system('aws ec2 stop-instances --instance-id {}'.format(ch1))
            elif 'terminate instance' in ec:
                ch1=input('Enter instance id: ')
                os.system('aws ec2 terminate-instances --instance-id {}'.format(ch1))
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
        inp1=input('Press enter to continue: ')
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
                size=input('Enter the size: ')
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
        inp1=input('Press enter to continue: ')
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
            elif 'details of bucket' in s:
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

def web():
    os.system('clear')
    print('''\t\t======= Welcome to the Web Server Menu!! =======

                1. Configure Web Server
                2. Create file
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
        if 'configure web server' in webs:
            os.system('dnf install httpd')
            os.system('systemctl start httpd')
            os.system('systemctl stop firewalld')
        elif 'create and open file' in webs or 'create file' in webs:
            webs1=input('Enter file name: ')
            os.system('vim /var/www/html/{}'.format(webs1))
        elif 'edit the shared file' in webs or 'edit shared file' in webs or 'edit the share file' in webs or 'edit share file' in webs:
            webs1=input('Enter the file name: ')
            os.system('cd /var/www/html')
            os.system('ls')
            os.system('vim {}'.format(webs1))
        elif 'delete the shared file' in webs or 'delete the share file' in webs or 'delete shared file' in webs or 'delete share file' in webs:
            webs1=input('Enter the file name: ')
            os.system('cd /var/www/html/')
            os.system('ls')
            os.system('rm -rf {}'.format(webs1))
        elif 'stop services' in webs or 'stop web services' in webs or 'stop the web services' in webs:
            os.system('systemctl stop httpd')
            os.system('systemctl start firewalld')
        elif 'exit' in webs:
            break
        else:
            print('Invalid Option (-_-)')
#head()
#sk3=input('Press enter to continue')

#Function for docker
def docker():
    os.system('clear')
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
    while(True):
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
            os.system('dnf install docker-ce --nobest')
            os.system('systemctl stop firewalld')
            os.system('systemctl start docker')
        elif 'pull image' in doc or 'pull an image' in doc:
            doc1=input('Enter OS type: ')
            os.system('docker pull {}'.format(doc1))
        elif 'launch container' in doc or 'launch a container' in doc:
            doc1=input('Enter the name of container: ')
            doc2=input('Enter OS type: ')
            os.system('docker run -it --name {} {}:latest'.format(doc1,doc2))
        elif 'information of all containers' in doc or 'information of containers' in doc:
            os.system('docker ps -a')
        elif 'attach container' in doc or 'attach the container' in doc:
            doc1=input('Enter container name: ')
            os.system('docker attach {}'.format(doc1))
        elif 'start the conatiner' in doc or 'start conatiner' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('docker start {}'.format(doc1))
        elif 'stop the container' in doc or 'stop conatiner' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('docker stop {}'.format(doc1))
        elif 'remove an image' in doc or 'remove the image' in doc or 'remove image' in doc:
            doc1=input('Enter OS type: ')
            os.system('docker rmi -f {}:latest'.format(doc1))
        elif 'delete a container' in doc or 'delete the container' in doc or 'delete container' in doc:
            doc1=input('Enter conatiner name: ')
            os.system('docker rm -f {}'.format(doc1))
        elif 'delete all containers' in doc or 'delete the containers' in doc:
            os.system('docker rm `docker ps -a -q`')
        elif 'information of image' in doc or 'image information' in doc or 'information of images' in doc:
            os.system('docker images')
        elif 'exit' in doc:
            break
        else:
            print('Invalid Option (-_-)')
#head()
#sk4=input('Press enter to continue')

#Function for partition
def partition():

    #Function for LVM Creation
    def crpartition():
        os.system('clear')
        print('''\t\t======= Welcome to Creation of LVM Partition!! =======
                    a) Create Physical Volume (PV)
                    b) Create Volume Group (PV)
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
            if 'create pv' in cpar or 'create a pv' in cpar or 'create physical volume' in cpar:
                cpar1=input('Enter the hard-disk name: ')
                os.system('fdisk -l')
                os.system('pvcreate {}'.format(cpar1))
            elif 'create vg' in cpar or 'create a vg' in cpar or 'create volume group' in cpar:
                cpar1=input('Enter the no. of PVs you want to attach: ')
                os.system('pvdisplay')
                cpars=[]
                i=0
                while(i < int(cpar1)):
                    cpar2=input('Enter PV-{} name: '.format(i+1))
                    cpars.append(cpar2)
                    i+=1
                if int(cpar1)==1:
                    for cparss in cpars:
                        os.system('vgcreate {}'.format(cpars[0]))
                else :
                    for cparss in cpars:
                        os.system('vgcreate {} {}'.format(cpars[0],cpars[1]))
            elif 'extend vg' in cpar:
                os.system('pvdisplay')
                cpar1=input('Enter PV name: ')
                os.system('vgextend {}'.format(cpar1))
            elif 'create lv' in cpar or 'create logical volume' in cpar:
                os.system('vgdisplay')
                cpar1=input('Enter VG name: ')
                cpar2=input('Enter LV name: ')
                cpar3=input('Enter size you want to give to Lv (eg. 1G,M): ')
                os.system('lvcreate --size {} --name {} {}'.format(cpar3,cpar2,cpar1))
            elif 'format' in cpar:
                os.system('lvdisplay')
                cpar1=input('Give LV path: ')
                os.system('mkfs.ext4 {}'.format(cpar1))
            elif 'mount' in cpar:
                cpar1=input('Enter folder name: ')
                os.system('mkdir /{}'.format(cpar1))
                cpar2=input('Give LV path: ')
                os.system('mount {} /{}'.format(cpar2,cpar1))
            elif 'exit' in cpar:
                break
            else:
                print('Invalid Option (-_-)')

    while(True):
        os.system('clear')
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
            os.system('lvdisplay')
            par2=input('Give LV path: ')
            os.system('lvextend --size +{} {}'.format(par1,par2))
            os.system('resize2fs {}'.format(par2))
        elif 'information of hard disk' in par or 'info of hard disk' in par or 'hard disk info' in par or 'hard disk information' in par:
            os.system('fdisk -l')
        elif 'mounted' in par or 'mount' in par:
            os.system('df -h')
        elif 'physical volume' in par or 'pv' in par:
            os.system('pvdisplay')
        elif 'volume group' in par or 'vg' in par:
            os.system('vgdisplay')
        elif 'logical volume' in par or 'lv' in par:
            os.system('lvdisplay')
        elif 'exit' in par:
            break
        else:
            print('Invalid Option (-_-)')

menu=None
while(menu!='exit'):
    with sr.Microphone() as source:
        head()
        skk=input('Press enter to continue')
        print('Tell us your requirement...')
        audio =r.listen(source)
        print('Okay got it!!')
    menu=r.recognize_google(audio)
    print(menu)
    if 'hadoop' in menu or 'Hadoop' in menu:
        hadoop()
    elif 'aws' in menu or 'cloud' in menu:
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