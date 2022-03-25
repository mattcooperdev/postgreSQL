import psycopg2


#connect to chinook db
connection = psycopg2.connect(database="chinook")

#build a cursor object of the db
cursor = connection.cursor()

#Query 1 - select all recrds form thr Artist table
cursor.execute('SELECT * FROM Artist')

#fetch the results (multiple)
results = cursor.fetchall()

#fetch the results (single)
# results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)

 



