
import json
#student is a uuid
#time is a string
#score is a float
#details is a string
class Score:
    def __init__(self,uuid:str,student:str,time:str,score:float,details:str) -> None:
        self.uuid = uuid
        self.student = student
        self.time = time
        self.score = score
        self.details = details
    def toJson(self):
        return json.dumps({
            "uuid": self.uuid,
            "student": self.student,
            "time": self.time,
            "score": self.score,
            "details": self.details
        })
    def fromJson(json_str):
        data = json.loads(json_str)
        return Score(
          data.uuid,
          data.student,
          data.time,
          data.score,
          data.details
       )