from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Task1")

# Initialize Spark Context
sc = SparkContext(conf = conf)

# Reduce the amount of log output
sc.setLogLevel("ERROR")

# Read the CSV file into an RDD
rdd = sc.textFile("1800.csv")

# Split each line by comma
rdd = rdd.map(lambda line: line.split(","))

# Transform into (category, value) pairs with values as integers
rdd = rdd.map(lambda x: (x[0], int(x[3])))

# Group by category and find the minimum value for each category
result = rdd.reduceByKey(lambda x, y: min(x, y))

# Collect and display the results
print("Grouped Data with Min Values:")
for category, min_value in result.collect():
    print(f"{category}: {min_value}")

# Stop Spark Context
sc.stop()

