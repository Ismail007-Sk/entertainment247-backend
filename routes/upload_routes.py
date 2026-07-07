from fastapi import APIRouter, File, UploadFile
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()




cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

router = APIRouter()


@router.post("/upload_file")
def upload_file(file: UploadFile = File(...)):

    result = cloudinary.uploader.upload(file.file)

    return {
        "message": "File Uploaded Successfully",
        "filename": file.filename,
        "image_url": result["secure_url"],
        "public_id": result["public_id"]
    }