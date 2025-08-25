import json

class User:
    def __init__(self, username, password, email, data):
        self.username = username
        self.password = password
        self.email = email
        self.data = data
    def to_json(self):
        return json.dumps({
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "data": self.data
        })
def from_json(json_str):
    data = json.loads(json_str)
    return User(
        username=data.get("username"),
        password=data.get("password"),
        email=data.get("email"),
        data=data.get("data"),
    )