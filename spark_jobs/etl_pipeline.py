from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

#1: Start Spark
spark = SparkSession.builder \
    .appName("COVID-19 Data Integration") \
    .getOrCreate()

#2: Load dataset
df = spark.read.csv("data/epidemiology.csv", header=True, inferSchema=True)

#3: Clean data
df_clean = df.dropna(subset=["date", "location_key", "new_confirmed"])

#4: Filter for key countries
filtered = df_clean.filter(col("location_key").isin("DE", "IT", "US"))

#5: Compute average daily confirmed cases per country
result = filtered.groupBy("location_key").agg(avg("new_confirmed").alias("avg_daily_cases"))

#6: Save results to Parquet
result.write.mode("overwrite").parquet("output/avg_daily_cases.parquet")

spark.stop()

