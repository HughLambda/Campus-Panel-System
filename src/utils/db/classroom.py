
import json
#manage is a list of user uuid
#students is a list of student uuid
class Classroom:
    def __init__(self,uuid:str,name:str,managers:list[str],students:list[str],data:str) -> None:
        self.uuid = uuid
        self.name = name
        self.managers = managers
        self.students = students
        self.data = data
    def isManaged(self,user:str):
        return user in self.managers

    def toJson(self):
        return json.dumps({
            "uuid": self.uuid,
            "name": self.name,
            "managers": json.dumps(self.managers),
            "students": json.dumps(self.students),
            "data": self.data
        })
    def fromJson(json_str):
        data = json.loads(json_str)
        return Classroom(
          data.uuid,
          data.name,
          json.loads(data.managers),
          json.loads(data.students),
          data.data
       )
