# installs required packages
!pip install pyspark
!pip install findspark
!pip install pandas

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


# creates a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

spark

# reads the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# previews a few records
mtcars.head()

# uses the `createDataFrame` function to load the data into a spark dataframe
sdf = spark.createDataFrame(mtcars) 

# lets us look at the schema of the loaded spark dataframe
sdf.printSchema()

sdf.show(5)

sdf.select('mpg').show(5)

sdf.filter(sdf['mpg'] < 18).show(5)

sdf.withColumn('wtTon', sdf['wt'] * 0.45).show(5)

sdf_new = sdf.withColumnRenamed("vs", "versus")

sdf.where(sdf['mpg'] < 18).show(3) 


# defines sample DataFrame 1 

data = [("A101", "John"), ("A102", "Peter"), ("A103", "Charlie")] 

columns = ["emp_id", "emp_name"] 

dataframe_1 = spark.createDataFrame(data, columns) 

# defines sample DataFrame 2 

data = [("A101", 1000), ("A102", 2000), ("A103", 3000)]

columns = ["emp_id", "salary"]

dataframe_2 = spark.createDataFrame(data, columns)

# creates a new DataFrame, "combined_df" by performing an inner join

combined_df = dataframe_1.join(dataframe_2, on="emp_id", how="inner")


# defines sample DataFrame 1

data = [("A101", 1000), ("A102", 2000), ("A103",None)]

columns = ["emp_id", "salary"]

dataframe_1 = spark.createDataFrame(data, columns)

# fills missing salary value with a specified value 

filled_df = dataframe_1.fillna({"salary": 3000}) 
filled_df.head(3)

# grouping and Aggregation

sdf.groupby(['cyl'])\
.agg({"wt": "AVG"})\
.show(5)

car_counts = sdf.groupby(['cyl'])\
.agg({"wt": "count"})\
.sort("count(wt)", ascending=False)\
.show(5)
