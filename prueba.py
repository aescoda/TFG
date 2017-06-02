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
    type (xml)
    print type (ET.fromstring(xml))
    doc = ET.ElementTree(ET.fromstring(xml))
    print type(doc)
    nombre = doc.find('iccid')
    nombre3 = doc.find('complexType/sequence/element')
    print nombre3
    nombre2 = doc.findall('iccid')
    print nombre
    nombre4 = doc.findall('complexType/sequence/element')
    for c in nombre4:
        print c.text
    print nombre4
    for c in nombre2:
        print c.text
    print "AHORA CON DOBLE ET."
    return None

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
