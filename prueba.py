from flask import Flask
from flask import request
from flask import make_response #Este no se si lo necesito
import os
import xml.etree.ElementTree as ET
from threading import Thread
from suds.client import Client
from suds.wsse import Security,UsernameToken


app = Flask(__name__)

def send_email(xml):
    
    service = 'terminal'
    wsdlurl= os.environ.get('WSDL_FILE', None)
    username= os.environ.get('USER_NAME', None)
    password= os.environ.get('USER_PASS', None)
    license_key= os.environ.get('LICENSE_KEY', None)


    print("***** create the SOAP client")
    clientService = Client(wsdlurl)
    #print clientService

    print("***** compose the SOAP security header")
    # add WSSE
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    clientService.set_options(wsse=security)

    print("***** compose the SOAP body")
    #define imsi as a complext type
    iccid =  dict(iccid = '89302720396916796910')
    getTerminalsDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid)

    print("***** SOAP request is:")
    #print getTerminalsDetailsRequest

    getTerminalsDetailsResponse = clientService.service.GetTerminalDetails(**getTerminalsDetailsRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    iccid = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    print(iccid)
    return None
    


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    print "webhook"
    xml = "Funciona el hilo"
    t = Thread(target=send_email, args=(xml,))
    t.start()
    print "acabando"
    return '',200
    
    
#app.route('/response', methods=['POST','GET'])
#def response:
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
