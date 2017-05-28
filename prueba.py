from flask import Flask
import os
from email.mime.text import MIMEText
from smtplib import SMTP


app = Flask(__name__)

@app.route("/webhook", methods=["POST","GET"])
def webhook():
    print "Email1"
    from_address = "migsepulcre@gmail.com"
    print"Email1"
    print "email2"
    to_address = "alejandro.escoda.umh@gmail.com"
    print "email2"
    message = "Hello, world!"
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
    print "Ha salido"
    return None

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
