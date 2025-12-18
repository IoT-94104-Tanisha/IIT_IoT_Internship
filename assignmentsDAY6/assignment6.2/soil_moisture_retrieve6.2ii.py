import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

query = "select * from soil_moisture;"

cursor = connection.cursor()
cursor.execute(query)

records = cursor.fetchall()

for record in records:
    print(record)

cursor.close()
connection.close()
