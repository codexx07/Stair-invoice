# import requests
# import json

# # Define the URL
# url = "https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar"

# # Define the headers
# headers = {
#     "api-key": "4c71388e-79d5-4c84-a111-a8f35a93605e",
#     "account-id": "6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88"
# }

# # Define the data
# data = {
#   "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
#   "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
#   "data": {
#     "uam_number": "UDYAM-MH-33-420866"
#    }
# }
# print(n:=str(data))
# #     # Make the POST request


# response = requests.post(url, headers=headers, data=n)
# # response = requests.post(url, headers=headers, data=data)

# # Print the response
# # print(response.content)
# print(response.text)

import requests
import uuid
import json

# POST request
url = "https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar"

task_id = str(uuid.uuid4())
group_id = str(uuid.uuid4())

payload = {
    "task_id": task_id,
    "group_id": group_id,
    "data": {
        "uam_number": "UDYAM-MH-33-0006866"
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

print(get_response.text)
