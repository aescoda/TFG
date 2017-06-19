from flask import Flask
from flask import request
import os
import xml.etree.ElementTree as ET
from threading import Thread
import email_lib
import jasper_lib


app = Flask(__name__)

xml = ""

def send_email(xml):
    return None
    
@app.route('/alert', methods=['POST','GET'])
def alert():
    #We will extract the data to use it for the application communications as unicode
    req = request.form
    event = req['eventType']
    print event
    if event == "SIM_STATE_CHANGE":
        print "va"
    else:
        print "nova"
    print type(event)
    data = req['data']  
    #We open a new thread to process the xml data receive as we need to answer Jasper to stop receiving messages
    t = Thread(target=send_email, args=(data,))
    t.start()
    #Jasper will resend the notification unless it receives a status 200 confirming the reception
    return '',200
    
    
@app.route('/response', methods=['POST','GET'])
def response():
    Terminals().prueba() #Comprobar como comparto la variable.
    return "Acabamos de procesar su peticion, en breve recibira un email con los detalles"
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
