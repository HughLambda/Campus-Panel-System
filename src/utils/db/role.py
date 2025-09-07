
import json
from .student import Student

"""
anonymous/student
admin
super
"""
class Role:
    def __init__(self,role:str,data:str) -> None:
        self.role = role
        self.data = data
    def to_json(self):
        return json.dumps({
            "role": self.role,
            "data": self.data
        })

class Anonymous(Role):
    def __init__(self,student:Student) -> None:
        super().__init__("anonymous",student.uuid)
        self.student = student

class Manager:
    def __init__(self,uuid:str,name:str,data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.data = data
    def to_json(self):
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "data": self.data
        })

class Admin(Role):
    def __init__(self,admin:Manager) -> None:
        super().__init__("admin",admin.uuid)
        self.admin = admin

class Super(Role):
    def __init__(self) -> None:
        super().__init__("super","SUPER")
        self.super = super

def createRole(role:Role)->str:
    pass

def from_json(json_str):
    data = json.loads(json_str)
    return Role(
        role=data.get("role"),
        data=data.get("data"),
    )

def manager_from_json(json_str):
    data = json.loads(json_str)
    return Manager(
        uuid=data.get("uuid"),
        name=data.get("name"),
        data=data.get("data"),
    )