
import json
from .student import Student

#unfinishedStudents is a list of student uuid
class Homework:
    def __init__(self,uuid:str,time:str,subject:str,unfinishedStudents:list[str],data:str) -> None:
        self.uuid = uuid
        self.time = time
        self.subject = subject
        #uuid
        self.unfinishedStudents = unfinishedStudents
        self.data = data
    
    def toJson(self):
        return json.dumps({
            "uuid": self.uuid,
            "time": self.time,
            "subject": self.subject,
            "unfinishedStudents": json.dumps(self.unfinishedStudents),
            "data": self.data
        })
    
    def fromJson(json_str):
        data = json.loads(json_str)
        return Homework(
          data.uuid,
          data.time,
          data.subject,
          json.loads(data.unfinishedStudents),
          data.data
       )