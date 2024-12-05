from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Task6")

# Initialize Spark Context
sc = SparkContext(conf = conf)

# Reduce the amount of log output
sc.setLogLevel("INFO")

# Step 1: Count the frequencies in the first dataset
# Load the first dataset
numbers_rdd = sc.textFile("Marvel+Graph")

# Count the frequency of each number
number_frequencies = (
    numbers_rdd.flatMap(lambda line: line.split())  # Split each line into numbers
    .map(lambda num: (int(num), 1))  # Map each number to (number, 1)
    .reduceByKey(lambda x, y: x + y)  # Sum up counts for each number
)

# Step 2: Load the second dataset with number-to-name mappings
names_rdd = sc.textFile("Marvel+Names")

# Convert to (number, name) pairs
number_names = names_rdd.map(lambda line: line.split(" ", 1)).map(lambda x: (int(x[0]), x[1].strip()))

# Step 3: Join the datasets on the number
joined_rdd = number_frequencies.join(number_names)

# Step 4: Map to (name, frequency) and sort by frequency
name_frequencies = (
    joined_rdd.map(lambda x: (x[1][1], x[1][0]))  # Map to (name, frequency)
    .sortBy(lambda x: x[1], ascending=True)  # Sort by frequency in descending order
)

# Collect and display the results
print("Name Frequencies (sorted):")
for name, frequency in name_frequencies.collect():
    print(f"{name}: {frequency}")

# Stop Spark Context
sc.stop()

