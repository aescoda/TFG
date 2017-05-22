import json
from email.mime.text import MIMEText
from smtplib import SMTP
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

# Buffer for capturing messages from Jasper
sbuffer = {"sessionId":"","roomId":"","message":"",
           "personId":"","personEmail":"","displayName":""}
# Buffer for capturing messages from email
abuffer = {"sessionId":"","confident":"", "message":"","action":"",

# Message Received from Jasper
@app.route('/webhook', methods=['POST','GET'])
def webhook():
    
    req = request.get_json(silent=True, force=True)
    #res = spark_webhook(req)

        from_address = "migsepulcre@gmail.com"
        to_address = "alejandro.escoda.umh@gmail.com"
        message = "Hello, world!"
        mime_message = MIMEText(message, "plain")
        mime_message["From"] = from_address
        mime_message["To"] = to_address
        mime_message["Subject"] = "Correo de prueba"
        smtp = SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        print "Conexion exitosa con Gmail"
        print "Concectado a Gmail"
        #
        smtp.login(from_address, "Ym2wlar!")
        smtp.sendmail(from_address, to_address, mime_message.as_string())
        smtp.quit()

         return none
