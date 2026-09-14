!pip install pyspark
!pip install findspark
!pip install pandas

import findspark  # Find and use Apache Spark
findspark.init()  # Initializes findspark to locate Spark
from pyspark.sql import SparkSession  
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType, DateType
import pandas as pd  
# Initializes a Spark Session
spark = SparkSession \
    .builder \
    .appName("COVID-19 Data Analysis") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

# Checks if the Spark Session is active
if 'spark' in locals() and isinstance(spark, SparkSession):
    print("SparkSession is active and ready to use.")
else:
    print("SparkSession is not active. Please create a SparkSession.")
    
# Reads the COVID-19 data from the provided URL
vaccination_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/KpHDlIzdtR63BdTofl1mOg/owid-covid-latest.csv')

print("Displaying the first 5 records of the vaccination data:")
columns_to_display = ['continent', 'total_cases', 'total_deaths', 'total_vaccinations', 'population']
# Show the first 5 records
print(vaccination_data[columns_to_display].head())

# Converts to Spark DataFrame directly
# Defines the schema
schema = StructType([
    StructField("continent", StringType(), True),
    StructField("total_cases", LongType(), True),
    StructField("total_deaths", LongType(), True),
    StructField("total_vaccinations", LongType(), True),
    StructField("population", LongType(), True)
])

# Converts the columns to the appropriate data types
vaccination_data['continent'] = vaccination_data['continent'].astype(str)  # Ensures continent is a string
vaccination_data['total_cases'] = vaccination_data['total_cases'].fillna(0).astype('int64')  # Fill NaNs and convert to int
vaccination_data['total_deaths'] = vaccination_data['total_deaths'].fillna(0).astype('int64')  # Fill NaNs and convert to int
vaccination_data['total_vaccinations'] = vaccination_data['total_vaccinations'].fillna(0).astype('int64')  # Fill NaNs and convert to int
vaccination_data['population'] = vaccination_data['population'].fillna(0).astype('int64')  # Fill NaNs and convert to int

spark_df = spark.createDataFrame(vaccination_data[schema.fieldNames()])  # Use only the specified fields
# Show the Spark DataFrame
spark_df.show()

print("Schema of the Spark DataFrame:")
spark_df.printSchema()
# Print the structure of the DataFrame (columns and types)

# Lists the names of the columns I want to display
columns_to_display = ['continent', 'total_cases', 'total_deaths', 'total_vaccinations', 'population']
# Display the first 5 records of the specified columns
spark_df.select(columns_to_display).show(5)

print("Displaying the 'continent' and 'total_cases' columns:")
# Show only the 'continent' and 'total_cases' columns
spark_df.select('continent', 'total_cases').show(5)

print("Filtering records where 'total_cases' is greater than 1,000,000:")
 # Show records with more than 1 million total cases
spark_df.filter(spark_df['total_cases'] > 1000000).show(5) 

from pyspark.sql import functions as F

spark_df_with_percentage = spark_df.withColumn(
    'death_percentage', 
    (spark_df['total_deaths'] / spark_df['population']) * 100
)
spark_df_with_percentage = spark_df_with_percentage.withColumn(
    'death_percentage',
    F.concat(
        # Format to 2 decimal places
        F.format_number(spark_df_with_percentage['death_percentage'], 2), 
        # Append the percentage symbol 
        F.lit('%')  
    )
)
columns_to_display = ['total_deaths', 'population', 'death_percentage', 'continent', 'total_vaccinations', 'total_cases']
spark_df_with_percentage.select(columns_to_display).show(5)

print("Calculating the total deaths per continent:")
# Group by continent and sum total death rates
spark_df.groupby(['continent']).agg({"total_deaths": "SUM"}).show()  

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
# Function definition
def convert_total_deaths(total_deaths):
    return total_deaths * 2
# Defines any transformation you want
# Registers the UDF with Spark
spark.udf.register("convert_total_deaths", convert_total_deaths, IntegerType())

# Drops the existing temporary view if it exists
spark.sql("DROP VIEW IF EXISTS data_v")

# Creates a new temporary view
spark_df.createTempView('data_v')

# Executes the SQL query using the UDF
spark.sql('SELECT continent, total_deaths, convert_total_deaths(total_deaths) as converted_total_deaths FROM data_v').show()

spark.sql('SELECT * FROM data_v').show()

print("Displaying continent with total vaccinated more than 1 million:")
# SQL filtering
spark.sql("SELECT continent FROM data_v WHERE total_vaccinations > 1000000").show()