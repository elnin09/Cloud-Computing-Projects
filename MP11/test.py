import mysql.connector

cnx = mysql.connector.connect(user='admin', password='darmora123',
                              host='darmoraglobaldatabase-cluster-1.cluster-cc1lsummhvn7.us-east-1.rds.amazonaws.com',
                              database='mp11')

print("success")
cursor = cnx.cursor()


id = 28;
query = ("SELECT * FROM mp11 "
        "WHERE id ={}".format(id))



cursor.execute(query)

for (f1,f2,f3,f4,f5,f6) in cursor:
    print(f1,f2,f3,f4,f5,f6)

cursor.close()


cursorwrite= cnx.cursor()

tid = "26"
f2 = "data"
f3 = "data"
f4 = "data"
f5 = "10"
f6 = "data"



#query = ("Insert into mp11 values("+tid+",'"+f2+"','"+f3+"','"+f4+"',"+f5+",'"+f6+"')")
query2 = ("Insert into mp11(f2,f3,f4,f5,f6) values('"+f2+"','"+f3+"','"+f4+"',"+f5+",'"+f6+"')")
print(query2)
cursorwrite.execute(query2)
cursorwrite.close()


cnx.commit()

cnx.close()














