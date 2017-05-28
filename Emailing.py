    #!/usr/bin/env python
    # -*- coding: utf-8 -*-


from email.mime.text import MIMEText
from smtplib import SMTP



def mail_checking():
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
    smtp.login(from_address,)
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
    print "fin"
    return "Hello"
