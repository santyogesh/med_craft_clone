from fastapi import APIRouter 
from .validators import HospitalLoginModel
import logger
from . import services

hospitals_rounter = APIRouter(
    prefix = "/hospital",
    tags = ["hospital"]
)

@hospitals_rounter.post('/hospital_login')
async def hospital_login(hospital_login_details : HospitalLoginModel): 
    try: 
        hospital_login_details = hospital_login_details.dict()
        print(hospital_login_details)
        res =  await services.hospital_login(login_details =hospital_login_details)
        return res
    except Exception as e: 
        logger.error(msg = str(e))
