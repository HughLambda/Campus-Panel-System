
import json

class Student:
    def __init__(self,uuid:str,name:str,classroom:str,dorm:str,group:str,score:float,data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.data = data
        #uuid
        self.classroom = classroom
        self.dorm = dorm
        self.group = group
        #float
        self.score = score
    def to_json(self):
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "classroom": self.classroom,
            "dorm": self.dorm,
            "group": self.group,
            "score": self.score,
            "data": self.data
        })

def from_json(json_str):
    data = json.loads(json_str)
    return Student(
        uuid=data.get("uuid"),
        name=data.get("name"),
        classroom=data.get("classroom"),
        dorm=data.get("dorm"),
        group=data.get("group"),
        score=data.get("score"),
        data=data.get("data"),
    )
    def getScore(self):
        return self.score
