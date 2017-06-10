from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
from threading import Thread



app = Flask(__name__)

def send_email(xml):
    data = ET.fromstring(xml)
    iccid = req[0]
    get_email
    return None
    


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    print "webhook"
    req = request.form
    xml = req['data']    
    t = Thread(target=send_email, args=(xml,))
    t.start()
    print "acabando"
    #Jasper resend the notification unless it receives a status 200 confirming the reception
    return '',200
    
    
#app.route('/response', methods=['POST','GET'])
#def response:
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
