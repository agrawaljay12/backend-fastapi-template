import os 
import cloudinary
from dotenv import load_dotenv

if os.getenv("ENVIRONMENT")=="development":
    load_dotenv('.env.development')
else:
    load_dotenv()

# configuration 
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)