from flask import Flask, request
import requests
import uuid
import json
import time
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
        # 'Content-Type': 'application/json',
        # 'Content-Length': '<calculated when request is sent>',
        # 'Host': '<calculated when request is sent>',
        # 'User-Agent': 'PostmanRuntime/7.36.1',
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Connection': 'keep-alive'
    }

    headers2 = {
        'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
        'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
        'Content-Type': 'application/json',
        # 'Host': '<calculated when request is sent>',
        # 'User-Agent': 'PostmanRuntime/7.36.1',
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }


    response = requests.request("POST", url, headers=headers, json=payload)

    # Check if the response is not empty
    if response.text:
        # Extract request_id from the response
        response_data = json.loads(response.text)
        request_id = response_data.get('request_id')
        print(request_id)
    else:
        print("Empty response")
        return {'error': 'Empty response from POST request'}

    # GET request
    get_url = f"https://eve.idfy.com/v3/tasks?request_id={request_id}"

    # GET request
    get_response = requests.request("GET", get_url, headers=headers2)
    get_response_data = json.loads(get_response.text)
    # print(get_response_data[0]['status'])
    time.sleep(10)

    print(get_response_data)
    


    return '', 209

if __name__ == '__main__':
    app.run(port=3001)



    