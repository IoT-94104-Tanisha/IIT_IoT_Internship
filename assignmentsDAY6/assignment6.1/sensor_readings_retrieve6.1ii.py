import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

query = "select * from sensor_readings;"

cursor = connection.cursor()
cursor.execute(query)

records = cursor.fetchall()

for record in records:
    print(record)

cursor.close()
connection.close()
