from datetime import datetime
from pydantic import BaseModel
from typing import List, Union



class User(BaseModel): 
    id: int
    name: str = "kessin"
    lastlogin: Union[datetime, None] = None
    friends: List[str] = []

fake_data = {
    "id" : 1213, 
    "lastlogin" : "2022-12-01 22:21",
    "friends" : {"Nigger1", "Nigger2", "Nigger3"}
}

user = User(**fake_data)
print(user.id)

