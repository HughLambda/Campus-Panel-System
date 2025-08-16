from flask import Flask, render_template_string, request
from flask_socketio import SocketIO, emit


from utils.page import Page
from utils.task import Task
from utils.app import SimpApp,WebAppCollection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

app_collection = WebAppCollection(app, socketio)

if __name__ == "__main__":
    socketio.run(app,port=15529,host="0.0.0.0")
    print("starting CPS")