graph = dict()

citydata = "New York->New Jersey,New Jersey->Boston,Boston->Philadelphia,New York->Washington,New York->Miami,New Jersey->Houston,Boston->Houston,Miami->Austin,Los Angeles->New Jersey,Los Angeles->Philadelphia,San Francisco->Las Vegas,Las Vegas->Washington,Houston->Las Vegas,Chicago->New Jersey,Los Angeles->Chicago"

sourcedest = citydata.split(",")
for i in sourcedest:
    city = i.split("->")
    if not(city[0] in graph.keys()):
       graph[city[0]]=dict()
    if not(city[1] in graph.keys()):
       graph[city[1]]=dict()
    graph[city[0]][city[1]]=1
    #graph[city[0]][city[0]]=0
    #graph[city[1]][city[1]]=0
        







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

print(bfs(graph,"New York"))  
            
   

 
