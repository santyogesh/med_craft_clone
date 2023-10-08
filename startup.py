import pymysql 
from config import database_config

### * SQL Server Connection 
try:
    sql_server = pymysql.connect(
            user    = database_config['username'], 
            host    = database_config['host'],
            passwd  = database_config['password'], 
            db      = database_config['db']
    )
    print("######### Mysql Server Connected #############")
except Exception as e: 
    print("######### Error in Connecting SQL Server ######")