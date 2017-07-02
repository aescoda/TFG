#!/usr/bin/env python
# -*- coding: utf-8 -*-

##This file contains functions to interact with the customer with email in the main.py file##
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import os

#For security reasons we storage all the private information in Heroku server as system variables. We will read them for functions 
sender_email = os.environ.get('MAIL_USER', None)
sender_pass = os.environ.get('MAIL_PASS', None)
server_email = os.environ.get('MAIL_SERVER', None)
port_email = os.environ.get('MAIL_PORT', None)


##This file contains functions to interact with the customer with email in the main.py file##
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import os

#For security reasons we storage all the private information in Heroku server as system variables. We will read them for functions 
sender_email = os.environ.get('MAIL_USER', None)
sender_pass = os.environ.get('MAIL_PASS', None)
server_email = os.environ.get('MAIL_SERVER', None)
port_email = os.environ.get('MAIL_PORT', None)


#This funcion is used to send an email notification to the customer and check if the IMEI change was unauthorized.
def email_alert(recipient, iccid, event):
    #We create the email for customer's name and iccid
    if event == "SIM_STATE_CHANGE":
        message = "<br>Estimado usuario,<br><br> Se ha detectado una cambio de estado de su <b> tarjeta SIM con numero de identificacion = %s</b><br><br> Si este cambio ha sido voluntario, por favor, ignore este mensaje. De lo contrario, por favor acceda al siguiente link para reactivar su tarjeta SIM: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Reactivar SIM </a><br><br></center> Atentamente,<br><br> Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (iccid)
        subject = "Alerta desactivacion de SIM"
    elif event == "IMEI_CHANGE":
        message = "<br>Estimado usuario,<br><br> Se ha detectado una <b>alerta de seguridad de cambio de IMEI de su tarjeta SIM con numero de identificacion = %s</b><br><br> Si este cambio de IMEI ha sido voluntario, por favor, ignore este mensaje. De lo contrario por favor hago acceda al siguiente link para localizar su tarjeta SIM y desactivarla: <br><br> <center><a href='https://jasper-alert.herokuapp.com/response'> Localizar y desactivar SIM </a><br><br></center>Atentamente,<br><br>Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (iccid)
        subject = "Alerta cambio de IMEI"
    elif event == "DATA_LIMIT":
        message = "<br>Estimado usuario,<br><br> Se ha alcanzado el limite de datos disponibles en su contrato de su <b> tarjeta SIM con numero de identificacion = %s.</b><br><br> Si desea contratar un paquete adicional, por favor, acceda al siguiente link: <br><br>   <left><a href='https://nj.jasperwireless.com/provision/ui/billing/rateplans/manage/details.html?detailFbRatePlanId=975801&popup=true'> Ampliar suscripcion </a><br><br></left>  Para obtener mas informacion del uso realizado de sus datos haga click aqui:<br><br>  <left><a href='https://jasper-alert.herokuapp.com/response'> Uso de datos </a><br><br></left> Atentamente,<br><br> Equipo de Cisco Jasper<br> <img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" %(iccid)
        subject = "Alerta consumo de datos alcanzado"
    elif event == "CTD_SESSION_USAGE_EXCEEDED":
        message = "<br>Estimado usuario,<br><br> Se han detectado un numero elevado numero de conexiones en la <b> tarjeta SIM, con numero de identificación = %s.</b><br><br> Por favor, revise la alerta identificada con su equipo de seguridad de Cisco Jasper, Atentamente,<br><br>, Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (iccid)
        subject = "Alerta de conexiones"
    #We create thebody with the message depending on the event
    body = MIMEText(message, "html", "uft-8")
    body["From"] = sender_email
    body["To"] = recipient
    body["Subject"] = subject
    #We try to make the conection with the SMTP server
    smtp = SMTP_SSL(server_email, port_email)
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, body)
    smtp.quit()
    return "Mensaje enviado"

#This function is used to send the location and iccid of the SIM card that has been changed.
def email_action (recipient, data):
    #We create the email for customer's name, iccid and location of the SIM card
    if event == "SIM_STATE_CHANGE":
        message = "<br>Estimado usuario,<br><br> Su tarjeta SIM con numero de identificación = %s ha sido reactivada<br><br> Atentamente,<br><br>    Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (data)
        subject = "Tarjeta SIM reactivada correctamente"
    elif event == "IMEI_CHANGE":
        message = "<br>Estimado usuario,<br><br> Tras su confirmacion de un acceso no autorizado a la SIM con iccid = %s hemos procedido a su localizacion y desactivacion. <br><br> La ultima posicion previa a la desactivacion era %s, en las coordenadas exactas de %s, %s <br><br> Rogamos se ponga en contacto con el equipo de seguridad de Jasper para investigar en detalle el evento ocurrido<br><br>   Atentamente,<br><br>    Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (data[3], data[2], data[0],data[1])
        subject = "Localizacion y desactivacion exitosas"
    elif event == "DATA_LIMIT":
        message = "<br>Estimado usuario, Encuentre a continuacion los datos de consumo solicitados previamente: <br><br> Volmen de datos usados: %s <br><br> Fecha de incio: %s <br><br> Volmen de datos usados (SMS): %s <br><br> Volmen de datos usados (Voz): %s<br><br> Atentamente,<br><br>    Equipo de Cisco Jasper<br><img src ='https://assets.sdxcentral.com/cisco-jasper-control-center-product.png'>" % (data[0], data[1], data[2], data[3])
        subject = "Detalles de consumo"
    #We create thebody with the message depending on the event
    body = MIMEText(message, "html", "uft-8")
    body["From"] = sender_email
    body["To"] = recipient
    body["Subject"] = subject
    #We try to make the conection with the SMTP server
    smtp = SMTP_SSL(server_email, port_email)
    #We introduce the credentials of the sender in the SMTP server and send the email.
    smtp.login(sender_email, sender_pass)
    smtp.sendmail(sender_email, recipient, body)
    smtp.quit()
    return "Mensaje enviado"

