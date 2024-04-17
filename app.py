from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Password for accessing the terminal
PASSWORD = "Momwhyareyouhere"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terminal', methods=['POST'])
def terminal():
    password = request.form.get('password')

    # Check if the password is correct
    if password == PASSWORD:
        return render_template('terminal.html')
    else:
        return "Incorrect password. Access denied.", 403

@socketio.on('execute_command')
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        emit('command_output', output)
    except Exception as e:
        emit('command_output', str(e))

if __name__ == '__main__':
    socketio.run(app, debug=True)
