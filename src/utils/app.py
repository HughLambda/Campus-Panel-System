from page import Page
from task import Task
from typing import Dict
from flask import Flask,render_template_string,request
from flask_socketio import SocketIO, emit
import json
import uuid


class SimpApp:
    """Web application class combined the page and task solving"""
    def __init__(self, tag: str, task: Task, page: Page):
        self.tag = tag
        self.task = task
        self.page = page
        
    def handle_request(self, **context) -> str:
        """Handle the http request and then return the rendered view"""
        return self.page.render(** context)
        
    def handle_ws_message(self, data: Dict) -> Dict:
        """Handle the websocket message ,and then return the result"""
        return self.task.invoke(data)


class WebAppCollection:
    """Web Application collection manager ,due to mount and manage the app"""
    def __init__(self, app: Flask, socketio: SocketIO):
        self.app = app
        self.socketio = socketio
        self.apps: Dict[str, SimpApp] = {}
        self._setup_routes()
        self._setup_socket_handlers()
        
    def mount_app(self, simp_app: SimpApp) -> None:
        """mount a web app"""
        if simp_app.tag in self.apps:
            raise ValueError(f"Tag '{simp_app.tag}' has been already used")
            
        self.apps[simp_app.tag] = simp_app
    
        endpoint_name = f"app_route_{simp_app.tag}_{uuid.uuid4().hex[:8]}"
        
        @self.app.route(f'/{simp_app.tag}', endpoint=endpoint_name)
        def app_route(tag=simp_app.tag):
            return self.apps[tag].handle_request(tag=tag)
            
        print(f"The App '{simp_app.tag}' has been mounted to the route: /{simp_app.tag}")
        
    def get_app(self, tag: str) -> SimpApp:
        """Get an app by tag"""
        return self.apps.get(tag)
        
    def _setup_routes(self) -> None:
        """Set up the main routes"""
        @self.app.route('/')
        def index():

            apps_list = [{"tag": tag, "title": app.page.title} for tag, app in self.apps.items()]
            return render_template_string("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Web App collection</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .app-list { list-style: none; padding: 0; }
                    .app-item { margin: 10px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
                    .app-link { text-decoration: none; color: #2c3e50; font-size: 1.2em; }
                    .app-link:hover { color: #3498db; }
                </style>
            </head>
            <body>
                <h1>Application Collection</h1>
                <h2>apps mounted:</h2>
                <ul class="app-list">
                    {% for app in apps_list %}
                    <li class="app-item">
                        <a href="/{{ app.tag }}" class="app-link">{{ app.title }}</a>
                    </li>
                    {% else %}
                    <li>None of applications,mount the app first,please</li>
                    {% endfor %}
                </ul>
            </body>
            </html>
            """, apps_list=apps_list)
            
    def _setup_socket_handlers(self) -> None:
        """Set up the websocket handle function"""
        @self.socketio.on('connect')
        def handle_connect():
            print('client connected')
            emit('response', {'status': 'connected', 'message': '成功连接到服务器'})
            
        @self.socketio.on('disconnect')
        def handle_disconnect():
            print('client closed')
            
        @self.socketio.on('message')
        def handle_message(data):
            """Handle the message from the client"""
            try:
                
                if isinstance(data, str):
                    data = json.loads(data)
                    
                
                if 'tag' not in data:
                    emit('response', {'status': 'error', 'message': 'the lack of Tag'})
                    return
                    
                tag = data['tag']
                app = self.get_app(tag)
                
                if not app:
                    emit('response', {'status': 'error', 'message': f'Not found the app with the tag "{tag}"'})
                    return
                    
                
                result = app.handle_ws_message(data)
                
                
                emit('response', {
                    'status': 'success',
                    'tag': tag,
                    'result': result
                })
                
            except Exception as e:
                emit('response', {'status': 'error', 'message': str(e)})