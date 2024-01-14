import requests
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a connection to the database
cnx = mysql.connector.connect(user='root', password='admin',
                              host='localhost',
                              database='my_database')

# Create a cursor object
cursor = cnx.cursor()

@app.route('/check-msme', methods=['POST'])
def check_msme():
    reg_Number = request.json['msmeRegNumber']
    print(reg_Number)

    # Check if the result is in the database
    query = "SELECT * FROM msme WHERE reg_Number = %s"
    cursor.execute(query, (reg_Number,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return jsonify(isValid=True)
        headers = {
            'Authorization': '579b464db66ec23bdd00000179ec49507d7a418a5d124f84f00be28f'
        }

        response = requests.get('https://data.gov.in/catalog/2c1fd4a5-67c7-4672-a2c6-a0a76c2f00da', headers=headers, params={'reg_Number': reg_Number})


    # Check the API response
    if response.status_code == 200:
        data = response.json()

        # Store the result in the database, regardless of whether it's valid
        insert_query = "INSERT INTO msme (reg_Number, is_valid) VALUES (%s, %s)"
        cursor.execute(insert_query, (reg_Number, data['isValid']))
        cnx.commit()

        if 'isValid' in data:
            return jsonify(isValid=data['isValid'])

    return jsonify(isValid=False)

if __name__ == '__main__':
    app.run(port=3001)