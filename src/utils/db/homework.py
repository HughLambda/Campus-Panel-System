
import json
from .student import Student

class Homework:
    def __init__(self,uuid:str,time:str,subject:str,unfinishedStudents:list,data:str) -> None:
        self.uuid = uuid
        self.time = time
        self.subject = subject
        self.unfinishedStudents = unfinishedStudents
        self.data = data
    def to_json(self):
        return json.dumps({
            "uuid": self.uuid,
            "time": self.time,
            "subject": self.subject,
            "unfinishedStudents": self.unfinishedStudents,
            "data": self.data
        })

def from_json(json_str):
    data = json.loads(json_str)
    return Homework(
        uuid=data.get("uuid"),
        time=data.get("time"),
        subject=data.get("subject"),
        unfinishedStudents=data.get("unfinishedStudents"),
        data=data.get("data"),
    )