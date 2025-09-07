
import json
from .student import Student
from .role import Admin,Super

class Classroom:
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
    def addStudent(self,student:Student):
        # This will be handled by the DB
        pass
    def removeStudent(self,student:Student):
        # This will be handled by the DB
        pass
    def isManaged(self,user:Admin|Super):
        return user in self.managers

def from_json(json_str):
    data = json.loads(json_str)
    return Classroom(
        uuid=data.get("uuid"),
        name=data.get("name"),
        managers=data.get("managers"),
        data=data.get("data"),
    )