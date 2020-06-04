from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F
from pyspark.sql import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType, FloatType
from pyspark.ml.feature import VectorAssembler

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # TODO:
    vecAssembler = VectorAssembler(inputCols=["count1", "count2","count3","count4","count5","count6","count7","count8","count9","count10","count11"], outputCol="features")
    new_df = vecAssembler.transform(df)
    #new_df.show()

    kmeans = KMeans(k=NUM_CLUSTERS, seed=0,maxIter = MAX_ITERATIONS,initMode=INITIALIZATION_MODE) 
    model = kmeans.fit(new_df.select('features'))
    transformed = model.transform(new_df)
    #transformed.show() 
    grouped = transformed.groupby('prediction').agg(F.collect_list('id'))
    mvv = grouped.select("collect_list(id)").rdd.flatMap(lambda x: x).collect()

    # Use the given data and the cluster pparameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    return mvv


def parse_line(line):
    # TODO: Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    return []


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(lambda row: row.split(","))
    parsed_rdd = rdd.map(lambda r: Row(
    id=r[0], 
    count1= float(r[1]),
    count2= float(r[2]),
    count3= float(r[3]),
    count4= float(r[4]),
    count5= float(r[5]),
    count6= float(r[6]),
    count7= float(r[7]),
    count8= float(r[8]),
    count9= float(r[9]),
    count10= float(r[10]),
    count11= float(r[11])
    )
    )

    myschema = StructType([StructField("id", StringType(), True),
                 StructField("count1", FloatType(), True),
                 StructField("count2", FloatType(), True),
                 StructField("count3", FloatType(), True),
                 StructField("count4", FloatType(), True),
                 StructField("count5", FloatType(), True),
                 StructField("count6", FloatType(), True),
                 StructField("count7", FloatType(), True),
                 StructField("count8", FloatType(), True),
                 StructField("count9", FloatType(), True),
                 StructField("count10", FloatType(), True),
                 StructField("count11", FloatType(), True),
                 ])

    # TODO: Convert RDD into a dataframe
    df = sqlContext.createDataFrame(parsed_rdd,schema=myschema)
    #df.show(10)

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)
    for cluster in clusters:
        print(','.join(cluster))
