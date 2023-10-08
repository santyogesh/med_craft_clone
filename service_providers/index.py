from fastapi import APIRouter 
import service_providers.services as service_providers_services
from service_providers.validators import (
        OrganizationValidator, 
        OrganizationLoginValidator, 
        HospitalModel, 
        UserAccessTokenValidator, 
        HospitalListViewValidator, 
        DoctorRegistrationValidator
    )
from responses import responses
from .services import validate_access_token, hospital_list_view
import logger

service_providers_router = APIRouter(
    prefix="/providers",
    tags=["providers"]
)

@service_providers_router.post('/organization_register')
async def register_organization(organization_data: OrganizationValidator):
    try:
        organization_data = organization_data.dict()
        res = await  service_providers_services.register_organization(organization_data=organization_data)
        return res
    except Exception as e: 
        return responses.send_error(msg = "Error Occured While Execution", data = e)

@service_providers_router.post('/register_hospital')
async def register_hospital(hospital_details : HospitalModel): 
    try: 
        hospital_details = hospital_details.dict()
        user_details = await validate_access_token(hospital_details['access_token'])
        if len(user_details) == 0:
            return responses.send_response(msg = "Invalid Access Token", data = "Invalid Access Token", status_code=400)
        hospital_details['organization_id'] = user_details[0][0]
        reigster_hospital_response = await service_providers_services.hospital_registration(hospital_details)
        return responses.send_response(msg = "Hospital Created SuccessFully", data = "Hospital Created SuccessFully")
    except Exception as e:
        logger.log(msg = str(e),level=1)
        print(e)
        return responses.send_error(msg = "Error Occured While Execution", data = "Error Occured", status_code=400)


@service_providers_router.post('/organization_login')
async def organization_login(organization_login_details : OrganizationLoginValidator):
    try: 
        organization_login_data = organization_login_details.dict() 
        res = await service_providers_services.organization_login(organization_login_data)
        return res
    except Exception as e: 
        return responses.send_error(msg = "Error Occured While Execution", data = e)


@service_providers_router.post('/validate_access_token')
async def validate_accesss_token(user_access_token_details : UserAccessTokenValidator):
    try:
        user_access_token_details = user_access_token_details.dict()
    except: 
        pass 

@service_providers_router.post('/hospital_list')
async def get_list_of_hospitals(hospital_list_view_details : HospitalListViewValidator):
    try: 
        print("############# - > ")
        print(hospital_list_view_details)
        hospital_list_view_details = hospital_list_view_details.dict()
        print("--------------------------------------------------")
        print(hospital_list_view_details)
        print("---------------------------------------------------")
        user_details = await validate_access_token(hospital_list_view_details['access_token'])
        if len(user_details) == 0:
            return responses.send_response(msg = "Invalid Access Token", data = {}, status_code=400)
        hospital_data = await hospital_list_view(hospital_list_view_details)
        return responses.send_response(msg = "", data = hospital_data, status_code = 200)
    except Exception as e:
        return responses.send_error(msg = "Some Error Occured", data = {}, status_code = 400)

@service_providers_router.post('/register_doctors') 
async def register_doctors(doctor_details : DoctorRegistrationValidator): 
    try:
        pass 
    except Exception as e: 
        logger.error(msg = str(e))
        return responses.send_error(msg = "Some Error Occured", data = {}, status_code=400)


