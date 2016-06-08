from flask import Flask

import common

app = Flask(__name__)

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
    return common.status()
