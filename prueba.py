from flask import Flask
from flask import request
from flask import make_response
import os
from xml.etree import ElementTree


app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    # Every message from Spark is received here. I will be analyzed and sent to
    # api.ai response will then sent back to Spark
    print "email"
    req = request.data
    print type(req)
    print req
    data = ElementTree.ElementTree(ElementTree.fromstring(req))
    print "ha hecho el XML"
    nombre = data.findall('comida/nombre')
    print "ha encontrado"
    print nombre
    print "caca"
    return None

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
