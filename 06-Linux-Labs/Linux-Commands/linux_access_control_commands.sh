    1  cd /home/project
    2  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/usdoi.txt
    3  ls -l usdoi.txt #to see the permissions for the file named usdoi.txt in your current directory
    4  chmod -r usdoi.txt #change mode command lets you change the permissions set for a file. 
    5  ls -l usdoi.txt #verify changed permissions
    6  chmod +r usdoi.txt #grant read access to all users on usdoi.txt
    7  chmod o-r usdoi.txt # remove the read permission only for 'other' category
    8  ls -l usdoi.txt 
    9  cd /home/project
   10  mkdir test
   11  ls -l #Check the default permissions that the system sets for new directory
   12  ls -l
   13  cd test
   14  mkdir test2
   15  cd ../
   16  chmod u-x test # Remove user execute permissions on test
   18  cd test #confirm permission denied
   20  ls -l #still can read it
   21  mkdir test/test3 #throws an error, cannot create a new directory within tests as permission is removed
   22  history 50 > linux_access_control_commands.sh
