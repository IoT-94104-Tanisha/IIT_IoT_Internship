import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

threshold = float(input("enter moisture threshold value : "))

query = f"select * from soil_moisture where moisture_level < {threshold};"

cursor = connection.cursor()
cursor.execute(query)

records = cursor.fetchall()

print("records with moisture below threshold:")
for record in records:
    print(record)

cursor.close()
connection.close()
