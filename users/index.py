from fastapi import APIRouter 
from users.services import users_services 
from users.user_validators import UserValidator,UserLoginValidator
import responses.responses as responses

users_router = APIRouter(
    prefix = "/users", 
    tags   = ["users"]
)

@users_router.get("/test_connection")
async def get_connection():
    return {
        "status_code": 200,
        "data": [],
        "message": "SuccessFull"
    }

@users_router.post("/register_user")
async def register_user(user_details : UserValidator):
    try:    
        user_details = user_details.dict()
        user_register_response = await users_services.register_user(
            user_deatils = user_details
        )
        return user_register_response
    except Exception as e: 
        return responses.send_error(msg = "Something Went Wrong", data = e)

@users_router.post("/user_login")
async def user_login(user_login_details: UserLoginValidator):
    try: 
        user_login_details = user_login_details.dict()
        res =  await users_services.user_login(
            user_login_details=user_login_details
        )
        return dict(res)
    except Exception as e: 
        return responses.send_error(msg = "Something Wend Wrong", data = e)
