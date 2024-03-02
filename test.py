import fastapi
from typing import List, Union
from pydantic import BaseModel

app = fastapi.FastAPI()
user_data = {
    "login" : "kessin",
    "password" : "sss",
    "info" : ["Sex"]
}


class User(BaseModel):
    login: str
    password: str
    info: List[str] = []
    
@app.post("/user")

async def PostInfo(login: str, password: str, info: List[str] = []): 
    current_data = {
        "login" : login,
        "password" : password,
        "info" : info
    }
    current_user = User(**current_data)
    if (current_user.login == "admin" and current_user.password == "nigga"):
        return {
            "Message: ", "admin lib"
        }
        

