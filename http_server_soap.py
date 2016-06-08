from pysimplesoap.server import SoapDispatcher, SOAPHandler, WSGISOAPHandler
import logging
import const
from BaseHTTPServer import HTTPServer
dispatcher = SoapDispatcher(
'TransServer',
location = "http://%s:8050/" % const.TARGET_IP,
action = 'http://%s:8050/' % const.TARGET_IP, # SOAPAction
namespace = "http://example.com/sample.wsdl", prefix="ns0",
trace = True,
ns = True)

def on():
    return "on"
def off():
    return "off"

def status():
    return "1024"

# register the user function

dispatcher.register_function('on', on,
    args={},
    returns={'result': str} 
    )

dispatcher.register_function('off', off,
    args={},
    returns={'result': str} 
    )

dispatcher.register_function('status', status,
    args={},
    returns={'humidity': str} 
    )

logging.info("Starting server...")
httpd = HTTPServer(("", 8050),SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

