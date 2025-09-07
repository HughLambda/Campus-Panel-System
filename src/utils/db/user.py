import json

class User:
    def __init__(self, username, password, role, phone, data):
        self.username = username
        self.password = password
        self.role = role
        self.phone = phone
        self.data = data
    
    def fromJson(json_str):
        data = json.loads(json_str)
        return User(
        username=data.get("username"),
        password=data.get("password"),
        role=data.get("role"),
        phone=data.get("phone"),
        data=data.get("data"),
        )

    def toJson(self):
        return json.dumps({
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "phone": self.phone,
            "data": self.data
        })
