from pydantic import BaseModel 


class OrganizationValidator(BaseModel): 

    organization_name       : str
    organization_address    : str
    organization_country    : str 
    organization_state      : str 
    organization_city       : str
    organization_phone      : str 
    organization_email      : str
    organization_password   : str

class HospitalModel(BaseModel):
    access_token            : str
    hospital_name           : str 
    hospital_addr           : str 
    phone                   : str 
    organization_id         : int
    hospital_state          : str
    hospital_country        : str
    hospital_city           : str
    hospital_pincode        : str
    hospital_password       : str 

class DoctorModel(BaseModel): 
    pass

class OrganizationLoginValidator(BaseModel): 
    
    organization_email      : str
    organization_password   : str


class UserAccessTokenValidator(BaseModel): 
    access_token            : str

class HospitalListViewValidator(BaseModel): 
    access_token             : str
    organization_id          : int


class DoctorRegistrationValidator(BaseModel): 
    fullname                 : str 
    phone                    : str 
    specialization           : str
