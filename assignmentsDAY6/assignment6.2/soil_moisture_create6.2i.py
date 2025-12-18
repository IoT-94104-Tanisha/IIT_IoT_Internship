import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

sensor_id = int(input("Enter Sensor ID : "))
moisture = float(input("Enter Moisture Level : "))
date_time = input("enter date and time (YYYY-MM-DD HH:MM:SS) : ")

query = f"INSERT INTO soil_moisture (sensor_id, moisture_level, reading_time) VALUES ({sensor_id}, {moisture}, '{date_time}');"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
