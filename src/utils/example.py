from flask import Flask, render_template_string, request
from flask_socketio import SocketIO, emit


from page import Page
from task import Task
from app import SimpApp, WebAppCollection

# Initialize Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Create web application collection manager
app_collection = WebAppCollection(app, socketio)



# Register example applications
if __name__ == '__main__':
    # Create calculator application
    import exampleCalc as calc
    app_collection.mount_app(calc.getApp())
    
    # Create text processing application
    import exampleTextProcessor as text
    app_collection.mount_app(text.getApp())
    
    # Run the application
    socketio.run(app, port=15555, host="0.0.0.0")
