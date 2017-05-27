    #!/usr/bin/env python
    # -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import make_response
from email.mime.text import MIMEText
from smtplib import SMTP

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
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
    print "fin"
    return None
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)
    
    
