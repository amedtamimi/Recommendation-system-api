from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os
import datetime
import cloudinary
import cloudinary.uploader
from fastapi import Depends, FastAPI, HTTPException, status, File, UploadFile
import model
from tensorflow.keras.models import load_model
import numpy as np
import urllib
import cv2
import urllib.request
import tensorflow as tf

model = load_model('model/indoorCalssfication.h5')
app = FastAPI()

cloudinary.config(
    cloud_name="dmrf3fisu",
    api_key="192614787258478",
    api_secret="r8WJ7msJBDQ-PsktSxsrNrJ202Q"
)


origins = ["*"]
methods = ["*"]
headers = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Food Vision API!"}

img = []


@app.post("/Upload_Image")
async def Upload_Image(image: UploadFile = File(...)):
    result = cloudinary.uploader.upload(image.file)
    img.append(result["url"])
    return {"url": result["url"]}


@app.get("/Get_Image")
async def Get_Image():
    if img != None:
        resp = urllib.request.urlopen(img[len(img)-1])
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        resize = tf.image.resize(image, (256, 256))
        predication = model.predict(np.expand_dims(resize/255, 0))
        if predication > 0.5:
            return {"predication": "Room"}
        else:
            return {"predication": "Balcony"}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    run(app, host="0.0.0.0", port=port)
