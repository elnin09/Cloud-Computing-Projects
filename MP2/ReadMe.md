#### DynamoDB , AWSLambda , RESTAPI (AWS) , AMAZON LEX
* Implement a REST API which takes JSON of distance between individual cities
* Process the input and create a graph use BFS to calculate distance(shortest) between various pairs and save/store it into DynamoDB
* The backed for the API that takes the graph as input parameter is AWS Lambda
* Create a Lex bot the backend to which is AWS Lambda (second lamda function) read the requests from Lex and send them to AWS Lambda which in turns read the data from DynamoDB
