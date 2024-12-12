from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("Task2")

# Initialize Spark Context
sc = SparkContext(conf = conf)

# Reduce the amount of log output
sc.setLogLevel("ERROR")

# Load the text file into an RDD
rdd = sc.textFile("Book")

# Line number to start processing from (e.g., start from line 3, zero-indexed)
start_line = 34

# Filter RDD to keep only lines starting from the specified line
filtered_rdd = rdd.zipWithIndex().filter(lambda x: x[1] >= start_line).map(lambda x: x[0])

# Count the frequency of each word
word_counts = (
    filtered_rdd.flatMap(lambda line: line.split())  # Split each line into words
    .map(lambda word: (word.lower(), 1))  # Convert words to lowercase and map to (word, 1)
    .reduceByKey(lambda x, y: x + y)  # Sum up counts for each word
)

# Sort by frequency in descending order
sorted_word_counts = word_counts.sortBy(lambda x: x[1], ascending=True)

# Collect and display the results
print(f"Word Frequency starting from line {start_line + 1} (sorted by frequency):")
for word, count in sorted_word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark Context
sc.stop()
