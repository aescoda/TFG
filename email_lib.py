#!/usr/bin/env python
# -*- coding: utf-8 -*-

##This file contains functions to interact with the customer with email in the main.py file##
import geocode
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
def email_alert(recipient, iccid, customer):
    #We create the email for customer's name and iccid
    message = "<br>Hola %s,<br><br> Se ha detectado una alerta de seguridad de cambio de IMEI en la SIM con iccid = %s<br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>    Muchas gracias,<br><br>    Equipo de Cisco Jasper<br>" % (customer, iccid)
    message = MIMEText(message, "html", "uft-8")
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = "IMEI change alert"
    #We try to make the conection with the SMTP server
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print "Conexion exitosa con Gmail"
    print "Concectado a Gmail"
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, message)
    smtp.quit()
    print "fin"
    return "Mensaje enviado"

#This function is used to send the location and iccid of the SIM card that has been changed.
def email_action (recipient, customer, coordenadas, iccid):
     #We create the email for customer's name, iccid and location of the SIM card
    message = "<br>Hola %s,<br><br> Se ha detectado una alerta de seguridad de cambio de IMEI en la SIM con iccid = %s<br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>    Muchas gracias,<br><br>    Equipo de Cisco Jasper<br>" % (customer, iccid)
    message = MIMEText(message, "html", "uft-8")
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = "Alert responsed"
    #We try to make the conection with the SMTP server
    smtp = SMTP(server_email, port_email)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print "Conexion exitosa con Gmail"
    print "Concectado a Gmail"
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, message)
    smtp.quit()
    print "fin"
    return "Mensaje enviado"



