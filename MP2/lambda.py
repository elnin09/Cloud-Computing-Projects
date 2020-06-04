import json
import boto3
import collections

def bfs(graph,node):
    visited = dict()
    distancearray = dict()
    queue = list()
    queue.append(node)
    visited[node]=True
    distance=0
    distancearray[node]=0
   
    while queue:
      temp = queue.pop(0)
      distance = distancearray[temp]+1
      for i in graph[temp].keys():
         if not(i in visited.keys()):
            queue.append(i)
            distancearray[i] = distance
            visited[i] = True
        
    
    return distancearray

def calculatedistance(citydata):
    graph = dict()
    node = dict()
    DistanceGraph = dict()
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('distanceTable')
    
    sourcedest = citydata.split(",")
    
    for i in sourcedest:
        city = i.split("->")
        #g.addEdge(city[0],city[1])
        if not(city[0] in graph.keys()):
            graph[city[0]]=dict()
        if not(city[1] in graph.keys()):
            graph[city[1]]=dict()
        graph[city[0]][city[1]]=1
        graph[city[0]][city[0]]=0
        graph[city[1]][city[1]]=0
        node[city[0]]=1
        node[city[1]]=1
        
    
    for i in node.keys():
        distance = bfs(graph,i)
        DistanceGraph[i]=distance
	
	
	
    for i in DistanceGraph.keys():
        for k in DistanceGraph[i].keys():
            #print(i)
            #print(k)
            #print(DistanceGraph[i][k]) 
            table.put_item(
            Item=
            {
             'Source':i,
             'Destination':k,
             'Distance': DistanceGraph[i][k]
            })
    return  DistanceGraph

def lambda_handler(event, context):
    # TODO implement
    
    
    #input = event['queryStringParameters']['graph']
    input = event['graph'];
    print(input)
    #print(input)
    DistanceGraph = calculatedistance(input)
    
   
    
    return {
        'statusCode': 200,
        'body': json.dumps(DistanceGraph)
    }




#The above code is for update graph



#The below is for distance called via lex



import json
import boto3

def lambda_handler(event, context):
  print(event)
    # TODO implement
  source = event['currentIntent']['slots']['source']
  destination = event['currentIntent']['slots']['destination']
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('distanceTable')
  db_response = table.get_item(
    Key={
            'Source': source,
            'Destination': destination
        }
        )
  print(db_response)
  print(db_response['Item']['Distance'])
  
  
  response = { 
    "dialogAction": {
    "type": "Close",
    "fulfillmentState": "Fulfilled",
    "message": {
      "contentType": "PlainText",
      "content": int(db_response['Item']['Distance'])
     }
            }
            }
            
            
  return response
    



