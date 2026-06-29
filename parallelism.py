from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ParallelismExample").getOrCreate()
sc = spark.sparkContext

data = [1, 2, 3, 4, 5, 6, 7, 8]

rdd = sc.parallelize(data, 4)

print("Number of partitions:")
print(rdd.getNumPartitions())

result = rdd.map(lambda x: x * 2).collect()

print("Result after parallel processing:")
print(result)

spark.stop()
