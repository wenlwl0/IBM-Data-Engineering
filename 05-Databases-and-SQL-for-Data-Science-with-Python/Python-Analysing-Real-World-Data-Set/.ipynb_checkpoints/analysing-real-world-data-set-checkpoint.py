!pip install ipython-sql
!pip install seaborn
import seaborn as sns
%load_ext sql

import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()
!pip install pandas 

%sql sqlite:///socioeconomic.db

import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

# Installs the 'ipython-sql' and 'prettytable' libraries using pip
!pip install ipython-sql prettytable

# Imports the 'prettytable' library, which is used to display data in a formatted table
import prettytable

# Sets the default display format for prettytable to 'DEFAULT' (i.e., a simple table format)
prettytable.DEFAULT = 'DEFAULT'

# Verifies that the table creation was successful
%sql SELECT * FROM chicago_socioeconomic_data limit 5;

# How many rows are in the dataset?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

# How many community areas in Chicago have a hardship index greater than 50.0?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

# What is the maximum value of hardship index in this dataset?
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

# Which community area which has the highest hardship index?
%sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data );

# Which Chicago community areas have per-capita incomes greater than $60,000?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

# Create a scatter plot using the variables `per_capita_income_` and `hardship_index`.
!pip install matplotlib seaborn
income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())