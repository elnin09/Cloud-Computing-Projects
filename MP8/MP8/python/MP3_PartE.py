from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import Row

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
raw_rdd = sc.textFile('gbooks').cache()


csv_rdd = raw_rdd.map(lambda row: row.split("\t"))


parsed_rdd = csv_rdd.map(lambda r: Row(
    word=r[0], 
    count1=int(r[1]),
    count2=int(r[2]),
    count3=int(r[3]),
    label=r[-1]
    )
)

myschema = StructType([StructField("word", StringType(), True),
                 StructField("count1", IntegerType(), True),
                 StructField("count2", IntegerType(), True),
                 StructField("count3", IntegerType(), True)
                 ])

df = sqlContext.createDataFrame(parsed_rdd,schema=myschema)
#print(df.take(5))
#df.printSchema()
df.createOrReplaceTempView("myview")
#sqlContext.sql("SELECT word, count(*) from myview GROUP BY word ORDER BY count(1) desc").show(3)




df2 = df.select("word", "count1").distinct().limit(1000);
df2.createOrReplaceTempView('gbooks2')
df2.createOrReplaceTempView("myview2")

result = sqlContext.sql("SELECT A.word AS Word1, B.word AS Word2 FROM myview2 A, myview2 B where A.count1 = B.count1")
print(result.count())
#result.show()

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 9658

