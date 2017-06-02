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
    url = request.args
    head = request.headers
    url2 = request.url
    url3 = request.url_root
    print "esto es url.root"
    print url3
    print "esto es cabecera"
    print head
    print "esto es url"
    print url2
    print "esto es los args"
    print url
    print "esto es toda la info"
    print req
    xml = req['data']
    "esto es solo los datos
    print xml
    #No se si necesito un tipo elementtree o un element...
    doc = ET.fromstring(xml)
    doc1 = ET.ElementTree(ET.fromstring(xml))
    print type(doc1)
    nombre = doc1.findall('iccid')
    for c in nombre:
        print c.text
    #nombre2 = doc1.findall('SimStateChange/iccid') 
    #for c in nombre2:
        #print c.text
    print "AHORA CON DOBLE ET."
    
    return None

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
