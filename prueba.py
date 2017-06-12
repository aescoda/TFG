from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
from threading import Thread



app = Flask(__name__)

def send_email(xml):
    data = ET.fromstring(xml)
    iccid = req[0]
    admin_details = get_admin(iccid)
    customer_email = get_email(admin_details[0])
    email_alert(customer_email,iccid, admin_details[1])
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
    
    
app.route('/response', methods=['POST','GET'])
def response:
    print xml #Comprobar como comparto la variable.
    location = get_location(iccid)
    #Como conseguimos la fecha y hora actual
    deactivateSIM(iccid, admin_details[2], actual_date)
    email_action(customer_email,admin_details[1],location,iccid)
    
    return "Acabamos de procesar su petición, en breve recibirá un email con los detalles"
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
