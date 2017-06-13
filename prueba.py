from flask import Flask
from flask import request
import os
import xml.etree.ElementTree as ET
from threading import Thread
import email_lib



app = Flask(__name__)

xml = ""

def send_email(xml):
    print "2"
    email_lib.prueba()
    print xml
    email_lib.email_alert(customer_email,iccid, admin_details[1])
    return None
    
@app.route('/webhook', methods=['POST','GET'])
def webhook():
    print "webhook"
    global xml
    xml = "hola"    
    t = Thread(target=send_email, args=(xml,))
    t.start()
    print "acabando"
    #Jasper resend the notification unless it receives a status 200 confirming the reception
    return '',200
    
    
@app.route('/response', methods=['POST','GET'])
def response():
    print xml #Comprobar como comparto la variable.
    return "Acabamos de procesar su peticion, en breve recibira un email con los detalles"
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
