from fastapi import FastAPI 
import startup
from users.index import users_router
from service_providers.index import service_providers_router
from fastapi.middleware.cors import CORSMiddleware
from hospitals.index import hospitals_rounter

app = FastAPI() 
print("############################ Server Started ######################")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(service_providers_router)
app.include_router(hospitals_rounter)
