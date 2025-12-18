import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

sensor_id = int(input("enter sensor id to update : "))
moisture = float(input("enter new moisture Level : "))

query = f"update soil_moisture set moisture_level = {moisture} where sensor_id = {sensor_id};"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
