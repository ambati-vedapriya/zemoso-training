from fastapi import FastAPI, Body, Form,File,UploadFile
from pydantic import BaseModel, Field
from typing import Optional,List,Set,Dict,Literal,Union



app = FastAPI()

@app.post("/files/")
async def create_files(files: List[bytes]=File(None,description="a file rea in bytes")):
    if not files:
        return{"message":"NO file send"}
    return{"file":[len(file) for file in files ]}


@app.post("/uploadfile/")
async def create_upload_files(file:UploadFile= File(...,description="files are the uploaded ones")):
    if not file:
        return{"message":"NO upload file send"} 
    cotent=await file.read()
    return{"filename":file.filename}


#request forms and files

@app.post("/filed/")
async def create_file(
    file:bytes=File(...),
    fileb:UploadFile=File(...),
    token:str=Form(...),):
    return {
        "file_size":len(file),
        "token":token,
        "file_content_type":fileb.content_type

    }
