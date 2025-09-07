import json
from typing import Dict, Any
from task import Task
from page import Page
from app import SimpApp
from db.user import User
from db.userDB import registerUser

def getApp() -> SimpApp:
    task = RegisterTask()
    page = Page(register_html, "Register Application")
    app = SimpApp("register", task, page,visible=False)
    return app

class RegisterTask(Task):
    def invoke(self, data):
        try:
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            
            if not username or not password:
                return {'error': 'Username and password are required'}
                
            user = User(username, password, email, "{}")
            if registerUser(user):
                return {'result': 'Registration successful', 'username': username}
            else:
                return {'error': 'Username already exists'}
        except Exception as e:
            return {'error': str(e)}

register_html = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .register { border: 1px solid #ccc; padding: 20px; border-radius: 5px; }
        .input-group { margin: 10px 0; }
        input { padding: 8px; margin: 0 5px; width: 200px; }
        button { padding: 8px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 3px; cursor: pointer; }
        .result { margin: 15px 0; padding: 10px; border: 1px solid #eee; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <div class="register">
        <div class="input-group">
            <input type="text" id="username" placeholder="Username">
        </div>
        <div class="input-group">
            <input type="password" id="password" placeholder="Password">
        </div>
        <div class="input-group">
            <input type="email" id="email" placeholder="Email (optional)">
        </div>
        <div class="input-group">
            <button onclick="register()">Register</button>
        </div>
        <div class="result" id="result">Registration result will appear here</div>
    </div>

    <script>
        // Connect to WebSocket server
        const socket = io.connect('http://' + document.domain + ':' + location.port);
        const tag = '{{ tag }}';
        
        // Handle server response
        socket.on('response', function(data) {
            console.log('Received response:', data);
            const resultDiv = document.getElementById('result');
            
            if (data.status === 'success' && data.tag === tag) {
                if (data.result.error) {
                    resultDiv.textContent = 'Error: ' + data.result.error;
                    resultDiv.style.color = 'red';
                } else {
                    resultDiv.textContent = data.result.result + ' for ' + data.result.username;
                    resultDiv.style.color = 'green';
                }
            } else if (data.status === 'error') {
                resultDiv.textContent = 'Error: ' + data.message;
                resultDiv.style.color = 'red';
            }
        });
        
        // Registration function
        function register() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const email = document.getElementById('email').value;
            
            if (!username || !password) {
                alert('Please enter both username and password');
                return;
            }
            
            // Send data to server
            socket.emit('message', {
                tag: tag,
                username: username,
                password: password,
                email: email
            });
        }
    </script>
</body>
</html>
"""