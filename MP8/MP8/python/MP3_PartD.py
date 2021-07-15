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
#print(raw_rdd.take(5))
####

csv_rdd = raw_rdd.map(lambda row: row.split("\t"))
#print(csv_rdd.take(2))
#print(type(csv_rdd))
#print(len(csv_rdd.take(1)[0]))

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
df = sqlContext.sql("SELECT word, count(*) from myview GROUP BY word ORDER BY count(1) desc").show(3)

####
# 2. Counting (10 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL 



# +--------+                                                                              
# |count(1)|
# +--------+
# |86618505|
# +--------+




####
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL

# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+

