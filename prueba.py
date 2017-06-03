from flask import Flask
from flask import request
from flask import make_response
import os
import xml.etree.ElementTree as ET
import Emailing


app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    req = request.form
    print type(req)
    xml = req['data']
    doc0 = ET.fromstring(xml)
    print doc0[0].text
    print doc0[1].text
    print doc0[2].text
    print doc0[3].text
    
    print "VAMOS A SACAR LOS PUTOS DATOS"
    return "hola"
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
