import json
import boto3
import collections
import mysql.connector
import redis

    
def read(id,usecache,r): 
    id = str(id)
    retval1 = r.get(id)
    if retval1 and usecache == "True":
        return json.loads(retval1)
    cnx = mysql.connector.connect(user='', password='',
                                  host='',
                                  database='')
    
    cursor = cnx.cursor()
    query = ("SELECT * FROM mp11 "
             "WHERE id ={}".format(id))
    
    
    
    cursor.execute(query)
    retval = dict()
    retval["id"]= id
    for (f1,f2,f3,f4,f5,f6) in cursor:
        retval["hero"] =   f2
        retval["name"] =   f4
        retval["power"] =  f3
        retval["color"] =  f6
        retval["xp"] =     f5
        print(f1,f2,f3,f4,f5,f6)
    


   
 
    
    cursor.close()
    cnx.close()
    r[id]=json.dumps(retval)
    return retval
    
# hero power name xp color
def write(f2,f3,f4,f5,f6):
    cnx = mysql.connector.connect(user='admin', password='darmora123',
                              host='darmoraglobaldatabase-cluster-1.cluster-cc1lsummhvn7.us-east-1.rds.amazonaws.com',
                              database='mp11')
    cursorwrite = cnx.cursor()
    query2 = ("Insert into mp11(f2,f3,f4,f5,f6) values('"+f2+"','"+f3+"','"+f4+"','"+f5+"','"+f6+"')")
    print(query2)
    cursorwrite.execute(query2)
    cursorwrite.close()
    cnx.commit()
    cnx.close()

  
 
#hero power name xp color      
def write_helper(sqls,usecache,r):
    print("starting write_helper")
    for sql in sqls:
        id = r.get("number")
        id = int(id)+1
        r.set("number",id)
        if(usecache=="True"):
            tempdict = {
                 "id"    : id,
                 "hero"  : sql["hero"],
                 "name"  : sql["name"],
                 "color" : sql["color"],
                 "power" : sql["power"],
                 "xp"    : str(sql["xp"])
            }
            print("putting into dictionary")
            r.set(id,json.dumps(tempdict,indent = 2))
        write(sql["hero"],sql["power"],sql["name"],str(sql["xp"]),sql["color"])
        


def read_helper(sqls,usecache,r):
    retval = list()
    for id in sqls:
        temp = read(id,usecache,r)
        retval.append(temp)
        
    return retval
    
  

def lambda_handler(event, context):
    # TODO implement
    r = redis.Redis(host="172.30.0.81")
    #r["number"] = "25"

    
    #input = event['queryStringParameters']['graph']
    usecache = event['USE_CACHE']
        
        
    
    request = event['REQUEST']
    sqls = event['SQLS']
    
    #print(sqls)
    
    if(request=='read'):
       retvallist = read_helper(sqls,usecache,r)
       retval = dict()
       retval["body"] = retvallist
       
    
    if(request=='write'):
        write_helper(sqls,usecache,r)
        retvallist = "write success"
        
    
    
 
    #print(input)
    
    if(request==write):
        return {
        'statusCode': 200,
        'body' : "write success"
        }
    
    b = {'statusCode' : 200, 
        'body' : retvallist
        
    }
    
    
    return {
        'statusCode' : 200,
        'body' : retvallist
        }
