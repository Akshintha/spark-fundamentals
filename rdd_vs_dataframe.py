from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDDVsDataFrame").getOrCreate()
sc = spark.sparkContext

data = [
    ("Akshintha", 27),
    ("John", 25),
    ("Sara", 30)
]

# RDD
rdd = sc.parallelize(data)
print("RDD Result:")
print(rdd.collect())

# DataFrame
df = spark.createDataFrame(data, ["name", "age"])
print("DataFrame Result:")
df.show()

spark.stop()
