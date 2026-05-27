from fastapi import UploadFile,HTTPException,status
from typing import List
import cloudinary.uploader
# import os
# import uuid


allowed_type =["image/jpeg","image/jpg","image/png","application/pdf","image/webp"]

async def save_file(file:UploadFile):
    try:

        if file.content_type not in allowed_type:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type, only allowed file type jepg, jpg, png, pdf, webp"
            )
        
        content = await file.read()
        
        result = cloudinary.uploader.upload(content)

        return result["secure_url"]
        
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"failed to upload the file on cloundinary:{str(e)}"
        )
    
def save_files(files:List[UploadFile])->List[str]:
    try:
        
        files_Path =[]

        for file in files:

            file_path = save_file(file)

            files_Path.append(file_path)

        return files_Path
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# upload_dir = "static/uploads"

# async def save_file(folder:str,file:UploadFile):
#     try:
#         # full path of upload file 
#         full_path = os.path.join(upload_dir,folder)

#         if not os.path.exists(full_path):
#             os.makedirs(full_path,exist_ok=True)

#         # extract the file extension using split method 
#         file_extension = file.filename.split(".")

#         # give the unique filename to each file with file extension
#         unique_filename = f"{uuid.uuid4()}.{file_extension}"

#         file_path = os.path.join(full_path,unique_filename)

#         with open (file_path,"wb") as f:

#             content = await file.read()
#             f.write(content)

#         file_location = f"static/uploads/{folder}/{unique_filename}"

#         return file_location



#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=str(e)
#         )
    
# async def save_files(files:List[UploadFile],folder:str)->List[str]:
#     try:
        
#         files_Path =[]

#         for file in files:

#             file_path = await save_file(file,folder)

#             files_Path.append(file_path)

#         return files_Path
    
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=str(e)
#         )
