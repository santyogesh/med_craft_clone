from sql_services.services import execute_query
from responses import responses 
import logger

async def hospital_login(login_details : any) -> any: 
    try:
        print("** " * 10)
        hospital_name = login_details['hospital_name']
        print("####" * 10)
        hospital_password = login_details['hospital_password']
        sql_query = f"SELECT hospital_id, hospital_access_token  \
                    FROM hospital WHERE hospital_name = '{hospital_name}' AND \
                    hospital_password = '{hospital_password}'" 
        logger.info(msg = {'sql query' : sql_query})
        sql_response = await execute_query(api_refrence="hospital_login", sql_query=sql_query, commit_operation=False)
        logger.info(msg = {'Response' : sql_response, 'sql_query' : sql_query})
        if len(sql_response) == 0:
            return responses.send_error(msg = "Invalid Credentials", data = {}, status_code=400)
        user_obj = {
            'hospital_id' : sql_response[0][0],
            'hospital_access_token' : sql_response[0][1]
        }
        return responses.send_response(
            msg = "Sucessfull",
            data = user_obj, 
            status_code = 200
        )
    except Exception as e:
        print("#####" * 20)
        print(e)
        print("####" * 20)
        logger.error(msg = str(e))
        raise e
