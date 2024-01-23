from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
import httpx

app = FastAPI()

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

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url}.")
            raise HTTPException(status_code=500, detail="An error occurred while making the request")