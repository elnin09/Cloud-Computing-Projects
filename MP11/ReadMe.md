#### Implementation of Write Through Cache using Redis,MYSQL and AWS Lamda. Cache used Redis Server(Docker Container) and DBServer used MySQL

* The code is in lamda.py wherein Read and Write functions are implemented.
* To test whether the cache is fulfilling read requests at a faster rate we have a flag if we should use cache or DB to read any particular request.
* test.py and test2.py are just to check whether the connection to redis server and MYSQL server is working fine.
