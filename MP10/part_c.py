from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *
from pyspark.sql.functions import explode

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id,v_list):
    # TODO
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    #ids = graphframe.select("id").rdd.flatMap(lambda x: x).collect()
    results = graphframe.shortestPaths(landmarks=v_list)
    newresults = results.select("id", explode("distances"))
    #newresults.show()
    newdf = newresults.select("id","value").where(newresults.key == dst_id)
    #newdf.show()
    retval = dict()
    for i in v_list:
        retval[i]=-1
    
    rdd_data = newdf.select("id","value").rdd.flatMap(lambda x: x).collect()
    i = 0
    while i<len(rdd_data):
        retval[rdd_data[i]]=rdd_data[i+1]
        i+=2



    return retval


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    v_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            # TODO: Parse line to get vertex id
            words = (line.rstrip("\n")).split(" ")
            src = words[0]
            # TODO: Parse line to get ids of vertices that src is connected to
            dst_list = words[1:]
            vertex_list.append((src,src))
            v_list.append(src)
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list,["id"]) # TODO: Create dataframe for vertices
    edges = spark.createDataFrame(edge_list,["src", "dst"]) # TODO: Create dataframe for edges

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")

    # We want the shortest distance from every vertex to vertex 1
    for k, v in get_shortest_distances(g, '1',v_list).items():
        print(k, v)
