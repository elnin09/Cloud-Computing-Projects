import redis
import requests
import json

redis = redis.Redis(host="",port=6379)

result = redis.get("check")
print(result)

if not result:
    result = "this"
    redis.setex("check",120,"this")
e

print (result)

resultnew = redis.get("check")
print(resultnew)



