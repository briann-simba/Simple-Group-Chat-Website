from flask import Flask
from flask_socketio import SocketIO,send


app=Flask(__name__)
app.config['SECRET_KEY']='sisecret'
socket=SocketIO(app,cors_allowed_origins="*")

@socket.on('message')
def handleMessage(msg):
    print(msg)
    send(msg,broadcast=True)

@socket.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

if __name__=='__main__':
    socket.run(app)