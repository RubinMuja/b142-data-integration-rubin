from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Step 1: Start Spark
spark = SparkSession.builder \
    .appName("COVID-19 Data Integration") \
    .getOrCreate()

# Step 2: Load dataset
df = spark.read.csv("data/epidemiology.csv", header=True, inferSchema=True)

# Step 3: Clean data
df_clean = df.dropna(subset=["date", "location_key", "new_confirmed"])

# Step 4: Filter for key countries
filtered = df_clean.filter(col("location_key").isin("DE", "IT", "US"))

# Step 5: Compute average daily confirmed cases per country
result = filtered.groupBy("location_key").agg(avg("new_confirmed").alias("avg_daily_cases"))

# Step 6: Save results to Parquet
result.write.mode("overwrite").parquet("output/avg_daily_cases.parquet")

spark.stop()

