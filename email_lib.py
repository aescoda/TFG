#!/usr/bin/env python
# -*- coding: utf-8 -*-

##This file contains functions to interact with the customer with email in the main.py file##
import geocode #Por ahora no lo uso
from email.mime.text import MIMEText
from smtplib import SMTP
import os

#For security reasons we storage all the private information in Heroku server as system variables. We will read them for functions 
sender_email = os.environ.get('MAIL_USER', None)
sender_pass = os.environ.get('MAIL_PASS', None)
server_email = os.environ.get('MAIL_SERVER', None)
port_email = os.environ.get('MAIL_PORT', None)
SSL_email = os.environ.get('MAIL_SSL', None)   

#This funcion is used to send an email notification to the customer and check if the IMEI change was unauthorized.
def email_alert(recipient, iccid, event):
    #We create the email for customer's name and iccid
    if event == "SIM_STATE_CHANGE":
        message = "<br>Estimado usuario,<br><br> Se ha detectado una cambio de estado de su tarjeta SIM con numero de identificacion = %s<br><br> Si este cambio ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para reactivar su tarjeta SIM: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Reactivar SIM </a><br><br></center>    Atentamente,<br><br>    Equipo de Cisco Jasper<br>" % (iccid)
        subject = "Alerta desactivacion de SIM"
    elif event == "IMEI_CHANGE":
        message = "<br>Estimado usuario,<br><br> Se ha detectado una alerta de seguridad de cambio de IMEI de su tarjeta SIM con numero de identificacion = %s<br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su tarjeta SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>    Atentamente,<br><br>    Equipo de Cisco Jasper<br>" % (iccid)
        subject = "Alerta cambio de IMEI"
    elif event == "DATA_LIMIT"
        message =  "<br>Estimado usuario<br><br>, Se ha alcanzado el limite de datos disponibles en su contrato. Si desea contratar un paquete adicional, por favor, acceda al siguiente link: <br><br> Para obtener mas informacion del uso realizado de sus datos haga click aqui:<br><br>  <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center> 
        subject = "Alerta consumo de datos alcanzado"
    elif event == "CTD_SESSION_USAGE_EXCEEDED"
        message = "Estimado usuario, Se han detectado un numero elevado numero de conexiones en esta tarjeta SIM, con numero de identificación = %s. Por favor, revise la alerta identificada con el equipo de seguridad de Cisco Jasper, Atentamente,<br><br>, Equipo de Cisco Jasper<br>" % (iccid)
        subject = "Alerta de conexiones"
    else
        message = ""
        subject = ""
    #We create thebody with the message depending on the event
    body = MIMEText(message, "html", "uft-8")
    body["From"] = sender_email
    body["To"] = recipient
    body["Subject"] = subject
    #We try to make the conection with the SMTP server
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, body)
    smtp.quit()
    return "Mensaje enviado"

#This function is used to send the location and iccid of the SIM card that has been changed.
def email_action (recipient, data):
    #We create the email for customer's name, iccid and location of the SIM card
    if event == "SIM_STATE_CHANGE":
        message = 
        subject = "SIM state change alert"
    elif event == "IMEI_CHANGE":
        message = "<br>Hola %s,<br><br> Tras su confirmacion de que ha habido un acceso no autorizado a la SIM con iccid = %s hemos procedido a su localizacion y desactivacion. <br><br> Su ultima posicion antes de la desactivacion era %s, en las coordenadas exactas de %s, %s <br><br> Rogamos se ponga en contacto con el equipo de Jasper para investigar en profundidad el problema<br><br>   Muchas gracias,<br><br>    Equipo de Cisco Jasper<br>" % (customer, data[2], data[3], data[0],data[1])
        subject = "IMEI change alert"
    elif event == "DATA_LIMIT"
        message = 
        subject = "Data limit achived"
    else
        message = ""
        subject = ""
    #We create thebody with the message depending on the event
    body = MIMEText(message, "html", "uft-8")
    body = MIMEText(message, "html", "uft-8")
    body["From"] = sender_email
    body["To"] = recipient
    body["Subject"] = subject
    #We try to make the conection with the SMTP server
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, body)
    smtp.quit()
    return "Mensaje enviado"



