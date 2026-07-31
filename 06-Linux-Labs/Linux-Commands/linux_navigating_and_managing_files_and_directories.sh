    1  pwd #get location of present working directory
    2  ls #list files and directories in the current directory
    3  ls /bin #list files in binaries
    4  ls /bin/ls #see that ls is present
    5  ls /bin/b* #list all files starting with b
    6  ls /bin/*r #list all ending in r
    7  ls  -l #longer list with additional info
    8  ls  -a #list all files, including hidden files
    9  ls  -d #list directories only, do not include files
   10  ls -s #	sort by file size, largest first
   11  ls -r #reverse order
   12  ls -t #	sort by last-modified date, newest first
   13  ls -d #list directories only, do not include files
   14  ls -h #	with -l and -s, print sizes like 1K, 234M, 2G
   15  ls -la /etc #all files in /etc including hidden files
   16  mkdir scripts #create new directory named scripts
   17  ls
   18  cd scripts #change pwd to scripts 
   19  pwd
   20  cd #back home
   21  pwd
   22  cd .. #parent directory of current directory, moves directories up one level
   23  touch #create an empty file
   24  touch myfile.txt #creates empty file called myfile.txt
   25  find /etc -name '*.txt' # search for files in a directory
   26  find /etc -name '*.conf'
   27  rm -i myfile.txt # used to delete files, ideally with the -i option, which creates a prompt to ask for confirmation before every deletion
   28  touch users.txt
   29  mv users.txt user-info.txt #move files from one directory to another and/or rename them.
   30  ls
   31  ls -l /tmp
   32  cp /tmp/user-info.txt user-info.txt #copy into current working directory
   33  cp /etc/passwd users.txt # copy the contents of an existing file into a new one
   34  ls
   37  cd ~/IBM-Data-Engineering/06-Linux-Labs/
   38  history 50 > linux_navigating_and_managing_files_and_directories.sh
