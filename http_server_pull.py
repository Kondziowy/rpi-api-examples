from flask import Flask, request

status_val = "-1"
commands = []

app = Flask(__name__)

@app.route('/on')
def on():
    commands.append("on")
    return "on"

@app.route('/off')
def off():
    commands.append("off")
    return "off"

@app.route('/status')
def status():
    return status_val

@app.route('/update_status', methods=['POST'])
def update_status():
    global status_val
    status_val = request.form["status"]
    return "ok"

@app.route('/get_command')
def get_command():
    if len(commands) == 0:
        return ""
    return commands.pop()

