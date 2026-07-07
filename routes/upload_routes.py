from fastapi import APIRouter,File,UploadFile
import shutil
import os


router = APIRouter()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)


# Upload File
@router.post("/upload_file")
                # variable name -> file ,should be used as key 
def upload_file(file:UploadFile=File(...)):
    file_path = os.path.join(UPLOAD_DIR,file.filename)

    with open(file_path,"wb") as output_file:
        # file.file-> orginal uploaded file
        # output_file-> copy of original file which is actually stored in server.
        shutil.copyfileobj(file.file,output_file)

    return{
        "meesage":"File Uploaded Successfully",
        "filename":file.filename,
        "path":file_path
    }