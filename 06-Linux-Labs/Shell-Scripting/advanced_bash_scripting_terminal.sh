    1  echo '#!/bin/bash' > conditional_script.sh #redirect shebang to new bash script
    2  chmod u+x conditional_script.sh
    3  echo 'Do you drive?' #ask user a binary yes/no question
    4  echo -n "Enter \"y\" for yes, \"n\" for no."
    5  y
    6  read response
    7  echo '#!/bin/bash' > calculations_and_numerical_logical_comparisons.sh
    8  chmod u+x calculations_and_numerical_logical_comparisons.sh
    9  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv
   10  csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"
   11  wget $csv_file
   12  cat arrays_table.csv #download file to current working directory then display the csv file 
   13  echo '#!/bin/bash' > parse_table_columns_into_arrays.sh
   14  chmod u+x parse_table_columns_into_arrays.sh
   15  cd IBM-Data-Engineering
   16  cd 06-Linux-Labs
   17  cd ~/IBM-Data-Engineering/06-Linux-Labs/ 
   18  cd IBM-Data-Engineering/06-Linux-Labs/ 
   19  git clone https://github.com/wenlwl0/IBM-Data-Engineering.git 
   20  cd IBM-Data-Engineering 
   21  cd 06-Linux-Labs
   22  history 50 > advanced_bash_scripting
