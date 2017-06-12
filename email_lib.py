# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from smtplib import SMTP

sender_email = os.environ.get('MAIL_USER', None)
sender_pass = os.environ.get('MAIL_PASS', None)
server_email = os.environ.get('MAIL_SERVER', None)
port_email = os.environ.get('MAIL_PORT', None)
SSL_email = os.environ.get('MAIL_SSL', None)   

def prueba():
    print "INCLUIDO"

def email_alert(recipient, iccid, customer):
    message = "<br>Hola %s,<br><br> Se ha detectado una alerta de seguridad de cambio de IMEI en la SIM con iccid = %s<br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>    Muchas gracias,<br><br>    Equipo de Cisco Jasper<br>" % (customer, iccid)
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
    smtp.sendmail(sender_email, recipient, message)
    smtp.quit()
    print "fin"
    return "Mensaje enviado"

def email_action (recipient, customer, coordenadas, iccid)
    message = "<br>Hola %s,<br><br> Se ha detectado una alerta de seguridad de cambio de IMEI en la SIM con iccid = %s<br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>    Muchas gracias,<br><br>    Equipo de Cisco Jasper<br>" % (customer, iccid)
    message = MIMEText(message, "html", "uft-8")
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = "Alert responsed"
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print "Conexion exitosa con Gmail"
    print "Concectado a Gmail"
    #
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, message)
    smtp.quit()
    print "fin"
    return "Mensaje enviado"




