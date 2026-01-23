from core import http_status
def success_response(message:str, data=None,status=http_status.OK):
    return {
        "status": status,
        "message": message,
        "data": data
    }

def create_success_response(message:str, data=None,status=http_status.CREATED):
    return {
        "status": status,
        "message": message,
        "data": data
    }