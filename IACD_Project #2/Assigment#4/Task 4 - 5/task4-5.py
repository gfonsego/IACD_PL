from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create a Spark session
spark = SparkSession.builder.appName("TotalAmountSpent").getOrCreate()

# Path to your CSV file (update the path to match your file's location)
csv_file_path = "customer-orders.csv"

# Read the CSV file without headers
df = spark.read.csv(csv_file_path, header=False, inferSchema=True)

# Assign column names manually
column_names = ["Customer_ID", "Product_ID", "Amount"]  # Replace with your actual column names
df = df.toDF(*column_names)

# Register the DataFrame as a temporary SQL table
df.createOrReplaceTempView("sales")

# Use Spark SQL to group the data and calculate the total amount spent by each customer
query = """
SELECT Customer_ID, SUM(Amount) AS Total_Amount
FROM sales
GROUP BY Customer_ID
ORDER BY Total_Amount DESC
"""

# Execute the SQL query
result = spark.sql(query)

# Show the result
result.show()