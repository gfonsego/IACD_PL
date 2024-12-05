from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create a Spark session
spark = SparkSession.builder.appName("TotalAmountSpent").getOrCreate()

# Path to your CSV file (update the path to match your file's location)
csv_file_path_1 = "Marvel+Graph"

# Path to your CSV file (update the path to match your file's location)
csv_file_path_2 = "Marvel+Names"

# Read the CSV file without headers
df_graph = spark.sparkContext.textFile(csv_file_path_1)
df_names = spark.sparkContext.textFile(csv_file_path_2)

# Count the frequency of each number and organize into (number, frequency) pairs
number_frequencies = (
    df_graph.flatMap(lambda line: line.split())  # Split each line into numbers
    .map(lambda num: (int(num), 1))  # Map each number to (number, 1)
    .reduceByKey(lambda x, y: x + y)  # Sum up counts for each number
)

#Transform and print into a df
df_graph = number_frequencies.toDF(["Number", "Frequency"])
df_graph.show()

#Creathing the schema for the names
schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Name", StringType(), True)
])

#Transform and print into a df
df_names = df_names.map(lambda line: line.split()).map(lambda line: (int(line[0]), line[1])).toDF(schema)
df_names.show()

df_graph.createOrReplaceTempView("df_graph")
df_names.createOrReplaceTempView("df_names")

# Use Spark SQL to join the two tables and sort by frequency
query = """
SELECT df_names.Name, df_graph.Frequency
FROM df_names, df_graph
WHERE df_names.ID = df_graph.Number
ORDER BY df_graph.Frequency ASC
"""

# Execute the SQL query
result = spark.sql(query)

# Show the result
result.show()
