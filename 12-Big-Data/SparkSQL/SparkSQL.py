# Installing required packages
!pip install pyspark
!pip install findspark
!pip install pyarrow==0.14.1 
!pip install pandas
!pip install numpy==1.19.5

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creates a spark context class
sc = SparkContext()

# Creates a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Reads the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# Previews a few records
mtcars.head()

mtcars.rename( columns={'Unnamed: 0':'name'}, inplace=True )

# createDataFrame function to load the data into a spark dataframe
sdf = spark.createDataFrame(mtcars) 

# Lets us look at the schema of the loaded spark dataframe
sdf.printSchema()


# The function `withColumnRenamed()` is renames the existing column names

sdf_new = sdf.withColumnRenamed("vs", "versus")


# Views the new dataframe

sdf_new.head(5)


# Creates a Table View

sdf.createTempView("cars")

# Shows the whole table
spark.sql("SELECT * FROM cars").show()

# Shows a specific column
spark.sql("SELECT mpg FROM cars").show(5)

# Basic filtering query to determine cars that have a high mileage and low cylinder count
spark.sql("SELECT * FROM cars where mpg>20 AND cyl < 6").show(5)

# Uses where method to get list of cars that have miles per gallon is less than 18
sdf.where(sdf['mpg'] < 18).show(3) 

# Aggregates data and grouping by cylinders
spark.sql("SELECT count(*), cyl from cars GROUP BY cyl").show()


# Imports the Pandas UDF function 
from pyspark.sql.functions import pandas_udf, PandasUDFType

@pandas_udf("float")
def convert_wt(s: pd.Series) -> pd.Series:
    # The formula for converting from imperial to metric tons
    return s * 0.45

spark.udf.register("convert_weight", convert_wt)

# Applies the UDF to the tableview

spark.sql("SELECT *, wt AS weight_imperial, convert_weight(wt) as weight_metric FROM cars").show()

# Combines DataFrames based on a specific condition. 


# Join operations

# Defines sample DataFrame 1 

data = [("A101", "John"), ("A102", "Peter"), ("A103", "Charlie")] 

columns = ["emp_id", "emp_name"]

dataframe_1 = spark.createDataFrame(data, columns)

# Defines sample DataFrame 2

data = [("A101", 3250), ("A102", 6735), ("A103", 8650)] 

columns = ["emp_id", "salary"] 

dataframe_2 = spark.createDataFrame(data, columns) 

# Creates a new DataFrame, "combined_df" by performing an inner join 

combined_df = dataframe_1.join(dataframe_2, on="emp_id", how="inner") 

# Shows the data in combined_df as a list of Row.

combined_df.collect()

# Fills the missing values 


# Defines sample DataFrame 1 with some missing values

data = [("A101", 1000), ("A102", 2000), ("A103",None)]

columns = ["emp_id", "salary"]

dataframe_1 = spark.createDataFrame(data, columns)


dataframe_1.head(3)

You will see that an error is thrown as the dataframe has null value.


Note that the third record of the DataFrame "dataframe_1", the column “salary”, contains null("na") value. It can be filled with a value by using the function "fillna()". 


# Fills missing salary value with a specified value

filled_df = dataframe_1.fillna({"salary": 3000})

filled_df.head(3)