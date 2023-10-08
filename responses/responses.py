def send_error(msg : str = "", data: any = {}, status_code: int = 400):
    return {
        'status_code': status_code,
        'data': data,
        'message': msg
    }

def send_response(msg: str = "", data: any = {}, status_code : int = 200):
    return {
        'status_code': status_code,
        'data': data,
        'message': msg
    }