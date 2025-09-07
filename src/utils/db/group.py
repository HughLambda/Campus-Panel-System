
import json
from .student import Student
from .role import Admin,Super

class Group:
    def __init__(self,uuid:str,name:str,managers:list,students:list,score:float,data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.managers = managers
        self.students = students
        self.data = data
        self.score = score
    def to_json(self):
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "managers": self.managers,
            "students": self.students,
            "score": self.score,
            "data": self.data
        })
    def addStudent(self,student:Student):
        # This will be handled by the DB
        pass
    def removeStudent(self,student:Student):
        # This will be handled by the DB
        pass
    def getScore(self):
        # This will be handled by the DB
        return self.score
    def isManaged(self,user:Admin|Super):
        return user in self.managers

def from_json(json_str):
    data = json.loads(json_str)
    return Group(
        uuid=data.get("uuid"),
        name=data.get("name"),
        managers=data.get("managers"),
        students=data.get("students"),
        score=data.get("score"),
        data=data.get("data"),
    )