from flask import Flask
app = Flask(__name__)

@app.route('/on')
def on():
    return 'on'

@app.route('/off')
def off():
    return "off"

@app.route('/status')
def status():
    return "1024"
