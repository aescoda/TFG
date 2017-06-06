from flask import Flask
from flask import request
from flask import make_response #Este no se si lo necesito
import os
import xml.etree.ElementTree as ET
from threading import Thread



app = Flask(__name__)

def send_email():
    print "Funciona el hilo"
    return None
    


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    req = request.form
    xml = req['data']
    t = Thread(target=send_email, args=(xml,))
    t.start()
    print xml
    return '',200
    
    
@app.route('/response', methods=['POST','GET'])
def response:
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
