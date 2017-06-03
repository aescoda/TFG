from flask import Flask
from flask import request
from flask import make_response
import os
import xml.etree.ElementTree as ET


app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    # Every message from Spark is received here. I will be analyzed and sent to
    # api.ai response will then sent back to Spark
    req = request.form
    print type(req)
    xml = req['data']
    print xml;
    print type (xml)
    print len(xml)
    print type (ET.fromstring(xml))
    doc0 = ET.fromstring(xml)
    doc1 = ET.ElementTree(ET.fromstring(xml))
    print type(doc1)
    print doc0[0][1].text
    print doc1[0][1].text
    print "VAMOS A SACAR LOS PUTOS DATOS"
    return "hola"
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
