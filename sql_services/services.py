 from .validators import OrganizationValidator, OrganizationLoginValidator
from sql_services.services import execute_query
import logger.logging as logger
import secrets
from responses import responses
from typing import List

async def register_organization(organization_data: OrganizationValidator): 
    try:
        if await validate_email(organization_data['organization_email']) == False: 
            return responses.send_error(msg = "Email Already Registered", data = {})
        access_token = secrets.token_hex(25)
        sql_query = "INSERT INTO organizations(org_name, org_address, org_country,"
        sql_query += "org_state, org_city, phone, email, passwd, access_token)"; 
        sql_query += f"VALUES('{organization_data['organization_name']}', '{organization_data['organization_address']}',"
        sql_query += f"'{organization_data['organization_country']}', '{organization_data['organization_state']}', '{organization_data['organization_city']}',"
        sql_query += f"'{organization_data['organization_phone']}', '{organization_data['organization_email']}',"
        sql_query += f"'{organization_data['organization_password']}', '{access_token}')"
        await execute_query(api_refrence="register organization", sql_query=sql_query, commit_operation=True)
        return responses.send_response(msg = "Organization Created SuccessFully", data = {
            'access_token': access_token,
            'email': organization_data['organization_email']
        })
    except Exception as e:
        logger.error(api_refrence="register organization", msg = "Error While Execution", data = e)
        raise e

async def validate_email(email: str): 
    try: 
        if email == '':
            logger.log(api_refrence="validate email", msg = "Blank Email Address", data = {})
            return False ## not valid. 
        sql_query = f"SELECT organization_id FROM organizations WHERE email = '{email}'"
        sql_response = await execute_query(api_refrence="validate email", sql_query=sql_query)
        print(sql_response)
        if len(sql_response) == 0:
            return True 
        else:
            return False
    except Exception as e: 
        logger.error(api_refrence="validate email", msg = "Error While validating Email", data = e)
        raise e
    
async def validate_access_token(access_token: str): 
    try: 
        if access_token.strip() == "":
            return ()
        sql_query = f"SELECT organization_id FROM organizations WHERE access_token = '{access_token}'"
        sql_response = await execute_query(api_refrence="validate access token", sql_query=sql_query, commit_operation=False)
        logger.info(api_refrence="validate access token", msg = "validate organization access token", data = sql_response)
        return sql_response
    except Exception as e:
        logger.error(api_refrence="validate access token", msg = "Error While validating access token", data = e)
        raise e

async def register_doctor():
    pass

async def organization_login(organization_login_details : OrganizationLoginValidator):
    try: 
        user_details = await get_organization(organization_email=organization_login_details['organization_email'], organization_password=organization_login_details['organization_password'], attributes=['access_token, organization_id'])
        if len(user_details) == 0: 
            return responses.send_error(msg = "invalid credentails", status_code=400)
        user_details = {
            'access_token': user_details[0][0],
            'organization_id': user_details[0][1]
        }
        return responses.send_response(msg = "Successfull", data = user_details)       
    except Exception as e:
        logger.error("Organization Login", msg = "Error While Execution", data = e)
        raise e

async def get_organization(organization_email: str, organization_password : str, attributes : List = []):
    try: 
        attr = ",".join(attributes)
        sql_query = f"SELECT {attr or '*'} FROM organizations WHERE email = '{organization_email}' and password = '{organization_password}'"
        sql_response = await execute_query(api_refrence="get_organization", sql_query=sql_query, commit_operation=False)
        return sql_response
    except Exception as e: 
        logger.error("Get Organization", msg = "Error while Fetching Organization Details", data = e)        
        raise e

async def hospital_registration(hospital_data : any): 
    try:
        hospital_access_token = secrets.token_hex(25)
        sql_query = f"INSERT INTO hospital(hospital_name,  \
                      hospital_addr, phone, organizations_id, hospital_state, \
                      hospital_country, hospital_city, hospital_access_token, hospital_password) \
                      VALUES('{hospital_data['hospital_name']}', '{hospital_data['hospital_addr']}', \
                      '{hospital_data['phone']}', {hospital_data['organization_id']}, \
                      '{hospital_data['hospital_state']}', '{hospital_data['hospital_country']}', '{hospital_data['hospital_city']}', \
                      '{hospital_access_token}', '{hospital_data['hospital_password']}')"

        print(sql_query)
        sql_response = await execute_query(api_refrence="hospital_registartion", sql_query=sql_query)
        logger.log(api_refrence="register_hospital", msg = sql_query, data = {})
        return sql_response
    except Exception as e: 
        logger.error(api_refrence="register_hospital", msg = str(e), data = {})
        raise e

async def hospital_list_view(organization_detalis: any): 
    try: 
        attribute_list = ["hospital_name", "hospital_addr", "hospital_state", "hospital_country", "hospital_city"]
        attribute_str = " , ".join(attribute_list)
        print(attribute_str)
        sql_query = f"SELECT {attribute_str} FROM hospital WHERE  organizations_id = {organization_detalis['organization_id']}"
        print(sql_query)
        sql_response = await execute_query(api_refrence="hopital list view", sql_query=sql_query, commit_operation=False)
        print(sql_query)
        hospital_data_list = {
        }
        hospital_data_list['count'] = len(sql_response)
        hospital_data_list['hospital_details'] = []
        for details in sql_response: 
            hospital_data = {}
            for i in range(len(attribute_list)):
                hospital_data[attribute_list[i]] = details[i]
            hospital_data_list['hospital_details'].append(hospital_data)
        return hospital_data_list
                
    except Exception as e:
        logger.error(api_refrence="hospital list view", msg = str(e), data = organization_detalis)
        raise e


