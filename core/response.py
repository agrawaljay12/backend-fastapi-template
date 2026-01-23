from fastapi.responses import JSONResponse
from core import http_status
def success_response(message:str, data=None,status=http_status.OK):
    return JSONResponse( 
        status_code=status,
        content={
            "status": status,
            "message": message,
            "data": data
        }
    )  

def created_response(message:str, data=None,status=http_status.CREATED):

    return JSONResponse(
    status_code=status,
        content={
            "status": status,
            "message": message,
            "data": data
        }
    )
