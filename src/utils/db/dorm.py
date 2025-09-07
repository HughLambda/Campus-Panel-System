
import json
from .role import Admin,Super

class Dorm:
    def __init__(self,uuid:str,name:str,managers:list,data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.managers = managers
        self.data = data
    def to_json(self):
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "managers": self.managers,
            "data": self.data
        })
    def isManaged(self,user:Admin|Super):
        return user in self.managers

def from_json(json_str):
    data = json.loads(json_str)
    return Dorm(
        uuid=data.get("uuid"),
        name=data.get("name"),
        managers=data.get("managers"),
        data=data.get("data"),
    )