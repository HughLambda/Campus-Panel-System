
import json
#record is a list of score uuid
#manage is a list of user uuid
class Student:
    def __init__(self,uuid:str,name:str,classroom:str,dorm:str,group:str,record:list[str],manage:list[str],score:float,data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.data = data
        #uuid
        self.classroom = classroom
        self.dorm = dorm
        self.group = group
        #float
        self.score = score
        #uuid list
        self.record = record
        #homework uuid list
        self.manage = manage
    def toJson(self):   
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "classroom": self.classroom,
            "dorm": self.dorm,
            "group": self.group,
            "score": self.score,
            "record": json.dumps(self.record),
            "manage": json.dumps(self.manage),
            "data": self.data
        })
    def fromJson(json_str):
        data = json.loads(json_str)
        return Student(
          data.uuid,
          data.name,
          data.classroom,
          data.dorm,
          data.group,
          json.loads(data.record),
          json.loads(data.manage),
          data.score,
          data.data
       )
