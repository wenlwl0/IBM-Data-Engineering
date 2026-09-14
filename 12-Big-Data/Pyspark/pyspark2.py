# Installing required packages
!pip install pyspark
!pip install findspark

import findspark
findspark.init()

# PySpark is the Spark API for Python. In this lab, we use PySpark to initialize the spark context. 
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

if 'spark' in locals() and isinstance(spark, SparkSession):
    print("SparkSession is active and ready to use.")
else:
    print("SparkSession is not active. Please create a SparkSession.")
    
data = range(1,30)
# print first element of iterator
print(data[0])
len(data)
xrangeRDD = sc.parallelize(data, 4)

# this will let us know that we created an RDD
xrangeRDD

subRDD = xrangeRDD.map(lambda x: x-1)
filteredRDD = subRDD.filter(lambda x : x<10)

print(filteredRDD.collect())
filteredRDD.count()

import time 

test = sc.parallelize(range(1,50000),4)
test.cache()

t1 = time.time()
# first count will trigger evaluation of count *and* cache
count1 = test.count()
dt1 = time.time() - t1
print("dt1: ", dt1)


t2 = time.time()
# second count operates on cached data only
count2 = test.count()
dt2 = time.time() - t2
print("dt2: ", dt2)

#test.count()

spark

# Download the data first into a local `people.json` file
!curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/people.json >> people.json

# Read the dataset into a spark dataframe using the `read.json()` function
df = spark.read.json("people.json").cache()

# Print the dataframe as well as the data schema
df.show()
df.printSchema()

# Register the DataFrame as a SQL temporary view
df.createTempView("people")

# Select and show basic data columns

df.select("name").show()
df.select(df["name"]).show()
spark.sql("SELECT name FROM people").show()

# Perform basic filtering

df.filter(df["age"] > 21).show()
spark.sql("SELECT age, name FROM people WHERE age > 21").show()

# Perfom basic aggregation of data

df.groupBy("age").count().show()
spark.sql("SELECT age, COUNT(age) as count FROM people GROUP BY age").show()

