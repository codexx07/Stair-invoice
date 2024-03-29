from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio
import boto3
from fastapi import FastAPI, UploadFile, File
import shutil


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

class ResponseFoundException(Exception):
    pass

s3 = boto3.client('s3')

last_uploaded_file_url = None

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global last_uploaded_file_url

    with open(f"{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    s3.upload_file(file.filename, 'stairdigital', file.filename, ExtraArgs={'ACL':'public-read'})

    last_uploaded_file_url = f"https://stairdigital.s3.ap-south-1.amazonaws.com/{file.filename}"

    return {"filename": file.filename, "message": "File successfully uploaded to S3 bucket"}

@app.get("/get-last-uploaded-file-url")
async def get_last_uploaded_file_url():
    global last_uploaded_file_url

    if last_uploaded_file_url is None:
        return {"error": "No file has been uploaded yet"}

    return {"url": last_uploaded_file_url}

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
        isValid = False
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"POST task ID: {task_id}")
            print(f"POST response: {response.json()}")

            # Use the request_id from the POST response in the GET request URL
            request_id = response.json().get('request_id')
            get_url = f"https://eve.idfy.com/v3/tasks?request_id={request_id}"

            while True:
                get_response = await client.get(get_url, headers=headers2)
                get_response.raise_for_status()
                print(f"GET request ID: {request_id}")
                print(f"GET response: {get_response.json()}")

                if isinstance(get_response.json(), list):
                    print("Found a list")
                    for item in get_response.json():
                        if isinstance(item, dict) and 'result' in item:
                            print("Found a result")
                            isValid = True
                            print("Isvalid set as True")
                            raise ResponseFoundException
                else:
                    if 'result' in get_response.json():
                        print("Found a result")
                        isValid = True
                        raise ResponseFoundException

                # Wait for 5 seconds before the next request
                await asyncio.sleep(5)
        except ResponseFoundException:
            pass

        return {"isValid": isValid}
