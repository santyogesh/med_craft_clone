from pydantic import BaseModel

class HospitalLoginModel(BaseModel): 

    hospital_name       : str
    hospital_password   : str