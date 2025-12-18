import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

id = int(input("enter id : "))
temperature = float(input("enter temperature : "))
humidity = float(input("enter humidity : "))
timestamp = input("enter timestamp (YYYY-MM-DD HH:MM:SS) : ")

query = f"INSERT INTO sensor_readings (id, temperature, humidity, timestamp) VALUES ({id}, {temperature}, {humidity}, '{timestamp}');"


cursor = connection.cursor()
cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
