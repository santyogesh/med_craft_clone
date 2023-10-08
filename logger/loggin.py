# filname: logging.py 
import datetime

def log(api_refrence : str = "", msg : str = "", data : any = {}):
    curr_time = datetime.datetime.now() 
    print(f"{curr_time} [*] LOG -> {api_refrence} msg : {msg} data : {data}")

def info(api_refrence: str = "", msg : str = "", data : any = {}): 
    curr_time = datetime.datetime.now()
    print(f"{curr_time} [*] INFO -> {api_refrence} msg : {msg} data : {data}")

def error(api_refrence: str = "", msg : str = "", data : any = {}) :
    curr_time = datetime.datetime.now()
    print(f"{curr_time} [*] EROR -> {api_refrence} msg : {msg} data : {data} ")
