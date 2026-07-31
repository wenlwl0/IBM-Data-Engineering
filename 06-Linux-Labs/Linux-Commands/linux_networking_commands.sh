    1  hostname #name that is assigned to a computer or device on a network, and it is used to identify and communicate with that device
    2  hostname -i #-i option to view the IP address of the host
    3  sudo apt update #install the iproute2 package part 1
    4  sudo apt install iproute2 #install iproute2 package part 2
    5  ip a #ip command is used to configure or display network interface parameters for a network. a to display configuration of all network interfaces of system
    6  ip addr show eth0 #configuration of a particular device, such as the ethernet adapter eth0
    7  ping www.google.com #ping command to check if www.google.com is reachable. The command keeps pinging data packets to server at www.google.com and prints the response it gets back
    8  ping -c 5 www.google.com #ping only a limited number of times
    9  curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
   10  #curl to access file at the URL and display file's contents
   11  curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
   12  #-0 to save to current working directory
   13  rm usdoi.txt
   14  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
   15  #wget command is similar to curl, however its primary use is for file downloading. One unique feature of wget is that it can recursively download files at a URL
   16  history 50 > linux_networking_commands
   17  cd ~/IBM-Data-Engineering 
   18  cd 06-linux-labs
   19  git clone https://github.com/wenlwl0/IBM-Data-Engineering.git 
   20  cd IBM-Data-Engineering
   21  cd ~/IBM-Data-Engineering/06-Linux-Labs/ 
   22  cd 06-Linux-Labs
   23  history 50 > linux_networking_commands
