from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return {"error": "শুধু ছবি ফাইল আপলোড করা যাবে।"}

    if os.path.exists("input.jpg"):
        os.remove("input.jpg")

    with open("input.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "ছবি সফলভাবে আপলোড হয়েছে এবং 'input.jpg' নামে সংরক্ষিত হয়েছে।"}
