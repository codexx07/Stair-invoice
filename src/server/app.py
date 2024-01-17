from flask import Flask, request
import requests
import uuid
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/check-msme', methods=['POST'])
def check_msme():
    # Extract msmeregnumber from the client's request
    msmeRegNumber = request.json.get('msmeRegNumber')

    # POST request
    url = "https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar"

    task_id = str(uuid.uuid4())
    group_id = str(uuid.uuid4())

    payload = {
        "task_id": task_id,
        "group_id": group_id,
        "data": {
            "uam_number": msmeRegNumber
        }
    }

    headers = {
        'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
        'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
    }

    headers2 ={
        'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
        'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    # Extract request_id from the response
    response_data = json.loads(response.text)
    request_id = response_data.get('request_id')

    # GET request
    get_url = f"https://eve.idfy.com/v3/tasks?request_id={request_id}"

    get_response = requests.request("GET", get_url, headers=headers2)

    # Parse the GET response
    get_response_data = json.loads(get_response.text)
    print(get_response_data)

    # Check the status field and set isValid accordingly
    isValid = get_response_data[0]['status'] == 'completed'

    # Send isValid back to the client
    return {'isValid': isValid}

if __name__ == '__main__':
    app.run(port=3001)