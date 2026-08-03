    1  chmod +x backup.sh
    2  ls -l backup.sh
    3  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip
    4  unzip -DDo important-documents.zip
    5  touch important-documents/*
    6  ./backup.sh important-documents .
    7  sudo cp backup.sh /usr/local/bin/
    8  ls -l /usr/local/bin/backup.sh
   11  sudo service cron start
   12  sudo service cron stop
   14  crontab -l > crontab-schedule
   17  cat crontab-schedule
   19  ls -l backup.sh > backup-file-check
   20  cat backup-file-check
   21  ls -l /usr/local/bin/backup.sh > backup-script-copy
   22  history 50 > linux_final_project_shell.sh
