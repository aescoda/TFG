from flask import Flask
from flask import request
from flask import make_response #Este no se si lo necesito
import os
import xml.etree.ElementTree as ET
from threading import Thread



app = Flask(__name__)

def get_email(xml):
    data = ET.fromstring(xml)
    iccid = req[0]
    get_admin()
    


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    req = request.form
    xml = req['data']
    t = Thread(target=emailing, args=(xml,))
    t.start()
    return '',200
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
