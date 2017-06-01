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
    print xml
    tip = type(xml)
    print tip
    doc = ET.parse(tip)
    print "ha hecho el XML"
    nombre = doc.findall('SimStateChange/iccid')
    for c in nombre:
        print c.text
    print "ha encontrado"
    return None

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
