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

url = "https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar"

payload = "{\n  \"task_id\": \"74f4c926-250c-43ca-9c53-453e87ceacd1\",\n  \"group_id\": \"8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e\",\n  \"data\": {\n    \"uam_number\": \"UDYAM-MH-33-0006866\"\n   }\n}"
headers = {
    'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
    'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
    'User-Agent': 'PostmanRuntime/7.28.4'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
