# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from smtplib import SMTP

sender_email = "migsepulcre@gmail.com"
sender_pass = 
server_email = 
port_email =
SSL_email =     



def email_alert(recipient):
    message = "<P>Hola %s,</P>
    <P>Se ha detectado una alerta de seguridad de cambio de IMEI en la SIM con iccid = %s. 
    Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje.
    De lo contrario por favor hago acceda al siguiente link para localizar su SIM y desactivarla </P><br>

    <a href="https://jasper-alert.herokuapp.com/response"> Localizar y desactivar SIM </a><br><br>

    Muchas gracias,<br><br>

    Equipo de Cisco Jasper<br>"
    message = MIMEText(message, "html", "uft-8")
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = "IMEI change alert"
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print "Conexion exitosa con Gmail"
    print "Concectado a Gmail"
    #
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, to_address, message)
    smtp.quit()
    print "fin"
    return "Hello"


<img = 

