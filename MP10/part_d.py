from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors
from pyspark.sql import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType, FloatType
from pyspark.ml.feature import VectorAssembler

sc = SparkContext()
sqlContext = SQLContext(sc)


def predict(df_train, df_test):
    # TODO: Train random forest classifier
    vecAssembler = VectorAssembler(inputCols=["count1", "count2","count3","count4","count5","count6","count7","count8"], outputCol="features")
    new_df = vecAssembler.transform(df_train)
    rf = RandomForestClassifier(numTrees=5, maxDepth=5, labelCol="id", seed=0)
    model = rf.fit(new_df)

    new_df_test = vecAssembler.transform(df_test)
    prediction = model.transform(new_df_test)
     
    #prediction.show()
    mvv = prediction.select("prediction").rdd.flatMap(lambda x: x).collect()

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use

    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    return mvv


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(lambda row: row.split(","))
    parsed_rdd_train = rdd_train.map(lambda r: Row(
    count1= float(r[0]),
    count2= float(r[1]),
    count3= float(r[2]),
    count4= float(r[3]),
    count5= float(r[4]),
    count6= float(r[5]),
    count7= float(r[6]),
    count8= float(r[7]),
    id= int(r[8])
    )
    )

    trainschema = StructType(
                [
                 StructField("count1", FloatType(), True),
                 StructField("count2", FloatType(), True),
                 StructField("count3", FloatType(), True),
                 StructField("count4", FloatType(), True),
                 StructField("count5", FloatType(), True),
                 StructField("count6", FloatType(), True),
                 StructField("count7", FloatType(), True),
                 StructField("count8", FloatType(), True),
                 StructField("id", IntegerType(), True)
                 ]
                )


    

    # TODO: Create dataframe from the RDD
    df_train = sqlContext.createDataFrame(parsed_rdd_train,schema=trainschema)

    #df_train.show()

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map(lambda row: row.split(","))
    
    parsed_rdd_test = rdd_test.map(lambda r: Row(
    count1= float(r[0]),
    count2= float(r[1]),
    count3= float(r[2]),
    count4= float(r[3]),
    count5= float(r[4]),
    count6= float(r[5]),
    count7= float(r[6]),
    count8= float(r[7])
    )
    )

    testschema = StructType(
                [
                 StructField("count1", FloatType(), True),
                 StructField("count2", FloatType(), True),
                 StructField("count3", FloatType(), True),
                 StructField("count4", FloatType(), True),
                 StructField("count5", FloatType(), True),
                 StructField("count6", FloatType(), True),
                 StructField("count7", FloatType(), True),
                 StructField("count8", FloatType(), True)
                 ]
                )

    # TODO:Create dataframe from RDD
    df_test = sqlContext.createDataFrame(parsed_rdd_test,schema=testschema)
    #df_test.show()

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
