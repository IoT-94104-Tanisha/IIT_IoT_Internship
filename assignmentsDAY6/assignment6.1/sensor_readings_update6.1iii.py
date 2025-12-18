import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

id = int(input("enter sensor id to update : "))
temperature = float(input("enter new temperature : "))
humidity = float(input("enter new humidity : "))

query = f"update sensor_readings set temperature = {temperature}, humidity = {humidity} where id = {id};"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
