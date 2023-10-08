# filename : user_validators.py
from pydantic import BaseModel 
from typing import Optional
class UserValidator(BaseModel): 

    username    : str
    firstname   : str 
    middle_name : Optional[str]
    lastname    : Optional[str]
    password    : str 
    email       : str 
    phone       : str 
    user_type   : int 
