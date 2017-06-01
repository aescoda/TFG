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
    print "email"
    req = request.form
    xml = req['data']
    print "TENEMOS LOS DATOS"    
    print "INTENTAMOS FROMSTRING"
    doc = ET.fromstring(xml)
    print "INTENTAMOS PARSE"
    tu = ET.parse(xml)
    print "AHORA CON DOBLE ET."
    doc1 = ET.ElementTree(ET.fromstring(xml))
    tu1 = Et.ElementTree(ET.parse(xml))
    print "PRUEBO A IMPRIMIR EL XML"
    nombre = xml.findall('SimStateChange/iccid')
    for c in nombre:
        print c.text
    print "ha encontrado"
    return None

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
