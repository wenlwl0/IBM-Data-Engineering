    2  cat entrypoint.sh #displays contents of file and exits back to command prompt
    3  more entrypoint.sh #cat alternative, see only as many lines as will fit on terminal window 
    4  less entrypoint.sh #move up and down through file
    5  cd /home/project
    6  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
    7  head usdoi.txt #prints first 10 lines of file
    8  head -3 usdoi.txt #print only first 3 lines of text from file
    9  tail usdoi.txt #prints last 10 lines
   10  tail -2 usdoi.txt #prints last 2 lines of file
   11  wc usdoi.txt #find the number of lines, words, and characters in a file
   12  wc -l usdoi.txt #just count lines
   13  wc -w usdoi.txt #just count words
   14  wc -c usdoi.txt #no. of bytes
   15  wc -m usdoi.txt #no. of characters
   16  sort usdoi.txt #display lines of file sorted alphanumerically
   17  sort -r usdoi.txt #reverse order
   18  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo.txt
   19  cat zoo.txt
   20  uniq zoo.txt #view contents of file with identical, consecutive lines 
   21  grep people usdoi.txt #prints all lines in the file containing word 'people'
   22  grep -v login /etc/passwd
   23  #Print all lines which do not contain 'login'
   24  cut -c -2 zoo.txt
   25  cut -c 2- zoo.txt #The cut command allows you to view only specific fields from each line of text in a file. -c option to view only the first two characters of each line. 2- to view each line starting from second character
   26  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/v4_new_content/labs/names_and_numbers.csv
   27  cat names_and_numbers.csv
   28  cut -d "," -f2 names_and_numbers.csv #extract just the phone numbers for each person listed in the file using the -d (delimiter) and f (field) options
   29  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo_ages.txt
   30  paste zoo.txt zoo_ages.txt
   31  #paste command to view the two files merged together, line-by-line, as columns delimited by a Tab character
   32  paste -d "," zoo.txt zoo_ages.txt #specify a comma instead of default tab delimiter
   33  history 50 > linux_wrangling_text_files.sh
   34  cd ~/IBM-Data-Engineering/06-Linux-Labs/ 
   35  cd ~/IBM-Data-Engineering 
   36  git remote add origin https://github.com/wenlwl0/IBM-Data-Engineering.git 
   37  git clone https://github.com/wenlwl0/IBM-Data-Engineering.git 
   38  git init
   39  git status
   40  git branch
   41  git config --global user.email "leewenli@gmail.com"
   42  git config --global user.name "wenlwl0"  
   43  git status
   44  cd ~/IBM-Data-Engineering/06-Linux-Labs/ 
   45  cd IBM-Data-Engineering
   46  git remote add origin https://github.com/wenlwl0/IBM-Data-Engineering.git 
   47  git clone https://github.com/wenlwl0/IBM-Data-Engineering.git 
   48  cd IBM-Data-Engineering
   49  cd ~/IBM-Data-Engineering/06-Linux-Labs/ 
   50  cd 06-Linux-Labs
   51  history 50 > linux_wrangling_text_files.sh
