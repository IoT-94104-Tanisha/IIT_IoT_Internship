from flask import Flask, request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Sensor Readings</h1></body></html>"

@server.post('/sensor')
def create_sensor_reading():
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    query = f"insert into sensor_readings VALUES ({id}, {temperature}, {humidity}, '{timestamp}');"
    executeQuery(query=query)

    return "Sensor reading added successfully"

@server.get('/sensor')
def retrieve_sensor_readings():
    query = "select * from sensor_readings;"
    data = executeSelectQuery(query=query)

    return f"Sensor Readings: {data}"

@server.put('/sensor')
def update_sensor_reading():
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')

    query = f"update sensor_readings SET temperature = {temperature}, humidity = {humidity} WHERE id = {id};"
    executeQuery(query=query)

    return "Sensor reading updated successfully"

@server.delete('/sensor')
def delete_sensor_reading():
    id = request.form.get('id')

    query = f"delete from sensor_readings where id = {id};"
    executeQuery(query=query)

    return "Sensor reading deleted successfully"

@server.get('/sensor/below')
def sensor_below_threshold():
    threshold = request.args.get('threshold')

    query = f"select * from sensor_readings where temperature < {threshold};"
    data = executeSelectQuery(query=query)

    return f"Sensor readings below threshold {threshold}: {data}"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
