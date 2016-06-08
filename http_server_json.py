from flask import Flask, jsonify

import common
import datetime

app = Flask(__name__)

@app.route('/')
def available_methods():
    return jsonify(["on","off","status"])

@app.route('/on')
def on():
    common.on()
    return 'on'

@app.route('/off')
def off():
    common.off()
    return "off"

@app.route('/status')
def status():
    return jsonify(**{"humidity": common.status(), "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
