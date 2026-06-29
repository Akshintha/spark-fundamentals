from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MapVsFlatMap").getOrCreate()
sc = spark.sparkContext

data = ["Hello World", "Apache Spark"]

rdd = sc.parallelize(data)

map_result = rdd.map(lambda x: x.split()).collect()
flatmap_result = rdd.flatMap(lambda x: x.split()).collect()

print("Map Result:")
print(map_result)

print("FlatMap Result:")
print(flatmap_result)

spark.stop()
