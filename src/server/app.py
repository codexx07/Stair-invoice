import requests
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Create a connection to the database
cnx = mysql.connector.connect(user='root', password='admin',
                              host='localhost',
                              database='my_database')

# Create a cursor object
cursor = cnx.cursor()

# @app.before_request
# def log_request_info():
#     print('Headers: %s', request.headers)
#     print('Body: %s', request.get_data())

@app.route('/check-msme', methods=['GET'])
def check_msme():
    try:
        reg_Number = request.json.get('msmeRegNumber')
        print(f"Received reg_Number: {reg_Number}")

        # # Check if the result is in the database
        # query = "SELECT * FROM msme WHERE reg_Number = %s"
        # cursor.execute(query, (reg_Number,))
        # rows = cursor.fetchall()
        # print(f"Database query returned {len(rows)} rows")

        # if len(rows) > 0:
        #     print("Found record in database")
        #     return jsonify(isValid=True)
        
        # else:
        #     print("No record found in database")
        
        headers = {
            'api-key': 'your-api-key',
            'account-id': 'your-account-id'
        }
        data = {
            "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
            "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
            "data": {
                "uam_number": reg_Number
            }
        }
        response = requests.post('https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar', headers=headers, data=json.dumps(data))
        print(f"External API response status: {response.status_code}")

        # Check the API response
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            print(f"External API response data: {data}")

        #     # Store the result in the database, regardless of whether it's valid
        #     insert_query = "INSERT INTO msme (reg_Number, is_valid) VALUES (%s, %s)"
        #     cursor.execute(insert_query, (reg_Number, data['isValid']))
        #     print("Inserted record into database")
        # else:
        #     print("External API request failed")
        #     return jsonify(isValid=False)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(port=3001)