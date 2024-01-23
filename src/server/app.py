from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Item(BaseModel):
    msmeRegNumber: str

@app.post("/check-msme")
async def check_msme(item: Item):
    url = "https://eve.idfy.com/v3/tasks/async/verify_with_source/udyam_aadhaar"

    task_id = str(uuid4())
    group_id = str(uuid4())

    payload = {
        "task_id": task_id,
        "group_id": group_id,
        "data": {
            "uam_number": item.msmeRegNumber
        }
    }

    headers = {
        'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
        'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
    }
    headers2 = {
        'api-key': '4c71388e-79d5-4c84-a111-a8f35a93605e',
        'account-id': '6d014c04f254/b95e280a-0c6c-47ac-b518-70b89cd82f88',
        'content-type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"POST request ID: {task_id}")
            print(f"POST response: {response.json()}")

            # Use the request_id from the POST response in the GET request URL
            request_id = response.json().get('request_id')
            get_url = f"https://eve.idfy.com/v3/tasks/{request_id}"
            get_response = await client.get(get_url, headers=headers2)
            get_response.raise_for_status()
            print(f"GET request ID: {request_id}")
            print(f"GET response: {get_response.json()}")

            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url}.")
            raise HTTPException(status_code=500, detail="An error occurred while making the request")