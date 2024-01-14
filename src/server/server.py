from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/check-msme', methods=['POST'])
def check_msme():
    msmeregnumber = request.json.get('msmeRegNumber')
    print(msmeregnumber)

    cnx = mysql.connector.connect(user='root', password='admin',
                                  host='127.0.0.1',
                                  database='my_database')
    cursor = cnx.cursor()

    query = ("SELECT * FROM MSME2 WHERE reg_Number = \'{0}\'".format)(msmeregnumber)
    print(query)
    cursor.execute(query, (msmeregnumber,))

    isvalid = False
    if cursor.fetchone() is not None:
        isvalid = True

    cursor.close()
    cnx.close()

    return jsonify(isValid=isvalid)

if __name__ == '__main__':
    app.run(debug=True, port=3001)