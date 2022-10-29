from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os
import datetime
import cloudinary
import cloudinary.uploader
from fastapi import Depends, FastAPI, HTTPException, status,File, UploadFile
import model
from tensorflow.keras.models import load_model
import numpy as np

app = FastAPI()

cloudinary.config(
    cloud_name= "dmrf3fisu",
    api_key= "192614787258478",
    api_secret ="r8WJ7msJBDQ-PsktSxsrNrJ202Q"
)


origins = ["*"]
methods = ["*"]
headers = ["*"]


app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Food Vision API!"}



if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8000))
	run(app, host="0.0.0.0", port=port)