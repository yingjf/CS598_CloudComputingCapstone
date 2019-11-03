file = sc.textFile('part-r-00000')
rdd = file.map(lambda line: line.split())
rdd2 = rdd.map(lambda tuple: (tuple[0], tuple[1], float(tuple[2])))
from pyspark.sql import Row
rdd3 = rdd2.map(lambda row: Row(airport=row[0], carrier=row[1], dep_delay=row[2]))
df = spark.createDataFrame(rdd3)
df.write\
    .format("org.apache.spark.sql.cassandra")\
    .mode('append')\
    .options(table="airport_carrier_departure", keyspace="aviation")\
    .save()