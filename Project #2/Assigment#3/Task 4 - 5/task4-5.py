from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Task3")

# Initialize Spark Context
sc = SparkContext(conf = conf)

# Reduce the amount of log output
sc.setLogLevel("INFO")

# Read the CSV file into an RDD
rdd = sc.textFile("customer-orders.csv")

# Split each line by comma
rdd = rdd.map(lambda line: line.split(","))

# Transform into (category, value) pairs with values as integers
rdd = rdd.map(lambda x: (x[0], float(x[2])))

# Group by category and find the minimum value for each category
result = rdd.reduceByKey(lambda x, y: x + y)

# Sort the results by the summed values in descending order
sorted_result = result.sortBy(lambda x: x[1], ascending=False)

# Collect and display the results
print("Grouped and Sorted Sum of Value by Customer:")
for key, total in sorted_result.collect():
    print(f"{key}: {total}")

# Stop Spark Context
sc.stop()